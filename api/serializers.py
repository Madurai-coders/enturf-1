from dataclasses import fields
from rest_framework import serializers
from .models import Admin, BookingReport,AdminSettings, CanceledReport, PaymentReport, PlayersAccount, User, turfDetails, turfImages, GroundDetails, GroundImages, GroundPricing, CoachingTime
# from drf_extra_fields.fields import Base64ImageField

class GetUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')


# "create_user": "http://127.0.0.1:8000/crud_user/",
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]


class AdminSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)
    #user = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Admin
        fields = ['user', 'userName', 'id', 'firstName',
                  'lastName', 'mobileNumber', 'email', 'dateOfBirth']


class TurfDetailsSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='admin.firstName', read_only=True)

    class Meta:
        model = turfDetails
        # ['images','id','firstName','turfName','mobileNumber','openingTime','cloasingTime','addressOfTurf','aminities','admin',]
        fields = '__all__'


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            # 12 characters are more than enough.
            file_name = str(uuid.uuid4())[:12]
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class TurfImageSerializer(serializers.ModelSerializer):
    #generalTurfImages =serializers.ImageField()
    turfName = serializers.CharField(
        source='turfDetails.turfName', read_only=True)
    #turfDetails = serializers.CharField(source='turfDetails.id',read_only=True)
    generalTurfImages = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = turfImages
        # ['id','turfDetails','generalTurfImages','turfName']
        fields = '__all__'


class GroundDetailsSerializer(serializers.ModelSerializer):
    turfName = serializers.CharField(
        source='turfDetails.turfName', read_only=True)

    class Meta:
        model = GroundDetails
        fields = '__all__'


class GroundImagesSerializer(serializers.ModelSerializer):
    groundName = serializers.CharField(
        source='GroundDetails.groundName', read_only=True)
    groundImages = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = GroundImages
        fields = '__all__'


class GroundPricingSerializer(serializers.ModelSerializer):
    groundName = serializers.CharField(
        source='GroundDetails.groundName', read_only=True)

    class Meta:
        model = GroundPricing
        fields = '__all__'


class CoachingTimeSerializer(serializers.ModelSerializer):
    groundName = serializers.CharField(
        source='GroundDetails.groundName', read_only=True)

    class Meta:
        model = CoachingTime
        fields = '__all__'

class AdminSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminSettings
        fields = '__all__'

class GetGroundPricingSerializer(serializers.ModelSerializer):
    groundName = serializers.CharField(
        source='GroundDetails.groundName', read_only=True)

    class Meta:
        model = GroundPricing
        fields = '__all__'


class GetGroundDetailsSerializer(serializers.ModelSerializer):
    turfName = serializers.CharField(
        source='turfDetails.turfName', read_only=True)
    gimage = GroundImagesSerializer(
        read_only=True, many=True,source='GroundImages')
    gprice = GetGroundPricingSerializer(many=True,read_only=True, source = 'GroundPricing')
    Ctime = CoachingTimeSerializer(many=True,read_only=True, source = 'CoachingTime')
    setting = AdminSettingsSerializer(many=True,read_only=True, source = 'ground_setting')
    class Meta:
        model = GroundDetails
        fields = '__all__'


class GetTurfDetailSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='admin.firstName', read_only=True)
    timage = TurfImageSerializer(
        read_only=True, many=True, source='turfImages')
    gdetails = GetGroundDetailsSerializer(
        read_only=True, many=True, source='GroundDetails')

    class Meta:
        model = turfDetails
    
        fields = '__all__'
       


class GetAllAdminDataSerializer(serializers.ModelSerializer):
    tdetails = GetTurfDetailSerializer(read_only=True, source='turfDetails')

    class Meta:
        model = Admin
        fields = '__all__'


class PlayersAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersAccount
        fields = '__all__'


class PaymentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReport
        fields = '__all__'


class BookingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingReport
        fields = '__all__'


class GetAllBooking(serializers.ModelSerializer):
    # booking_userid = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = BookingReport
        fields = '__all__'
        depth = 1

class CanceledReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanceledReport
        fields = '__all__'
