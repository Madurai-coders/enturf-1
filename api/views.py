from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import GetAllBooking,GetAllAdminDataSerializer,AdminSettingsSerializer, BookingRecordSerializer, CanceledReportSerializer, PaymentReportSerializer, PlayersAccountSerializer, UserSerializer, AdminSerializer, TurfDetailsSerializer, TurfImageSerializer, GroundDetailsSerializer, GroundImagesSerializer, GroundPricingSerializer, CoachingTimeSerializer, GetUserSerializer
from .models import Admin,AdminSettings, BookingReport, CanceledReport, PaymentReport, PlayersAccount, turfDetails, turfImages, GroundDetails, GroundImages, GroundPricing, CoachingTime
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import filters


class UserListViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #http_method_names =['get', 'post']

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(id=self.request.user.id)
        return query_set


class GetUserAccountList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    #permission_classes = [IsAuthenticated]
    #http_method_names = ['get']

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(id=self.request.user.id)
        return query_set


class AdminListViewset(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    #http_method_names = ['get', 'post']
    #permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = self.queryset
    #     user = self.request.user
    #     query_set = queryset.filter(user=user)
    #     return query_set


class AdminWithTurfDetailsViewset(generics.GenericAPIView):
    queryset = turfImages.objects.all()

    def get(self, request, *args, **kwargs):
        admin = Admin.objects.all()
        tdetails = turfDetails.objects.all()
        turfimages = turfImages.objects.all()
        gdetails = GroundDetails.objects.all()
        gimages = GroundImages.objects.all()
        context = {
            "request": request,
        }
        admin_serializer = AdminSerializer(admin, many=True, context=context)
        tdetails_serializer = TurfDetailsSerializer(
            tdetails, many=True, context=context)
        timage_serializer = TurfImageSerializer(
            turfimages, many=True, context=context)
        gdetails_serializer = GroundDetailsSerializer(
            gdetails, many=True, context=context)
        gimages_serializer = GroundImagesSerializer(
            gimages, many=True, context=context)
        gimages_serializer = GroundImagesSerializer(
            gimages, many=True, context=context)
        response = admin_serializer.data + tdetails_serializer.data + \
            timage_serializer.data + gdetails_serializer.data + gimages_serializer.data
        return Response(response)


class GetAllAdminDataView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = GetAllAdminDataSerializer
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        query_set = queryset.filter(user=user)
        return query_set

class TurfDetailsViewset(viewsets.ModelViewSet):
    queryset = turfDetails.objects.all()
    serializer_class = TurfDetailsSerializer


class TurfImageViewset(viewsets.ModelViewSet):
    queryset = turfImages.objects.all()
    serializer_class = TurfImageSerializer

class AdminSettingViewset(viewsets.ModelViewSet):
    queryset = AdminSettings.objects.all()
    serializer_class = AdminSettingsSerializer

class GroundDetailsViewset(viewsets.ModelViewSet):
    queryset = GroundDetails.objects.all()
    serializer_class = GroundDetailsSerializer


class GroundImagesViewset(viewsets.ModelViewSet):
    queryset = GroundImages.objects.all()
    serializer_class = GroundImagesSerializer


class GroundPricingViewset(viewsets.ModelViewSet):
    queryset = GroundPricing.objects.all()
    serializer_class = GroundPricingSerializer


class CoachingTimeViewset(viewsets.ModelViewSet):
    queryset = CoachingTime.objects.all()
    serializer_class = CoachingTimeSerializer


class PlayerAccountViewset(viewsets.ModelViewSet):
    queryset = PlayersAccount.objects.all()
    serializer_class = PlayersAccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['userName']
    


class PaymentReportViewset(viewsets.ModelViewSet):
    queryset = PaymentReport.objects.all()
    serializer_class = PaymentReportSerializer


class BookingReportViewset(viewsets.ModelViewSet):
    queryset = BookingReport.objects.all()
    serializer_class = BookingRecordSerializer


class CanceledReportViewset(viewsets.ModelViewSet):
    queryset = CanceledReport.objects.all()
    serializer_class = CanceledReportSerializer




class GetBookingByDate(viewsets.ModelViewSet):
    queryset = BookingReport.objects.all()
    serializer_class = BookingRecordSerializer

    def get_queryset(self):
        queryset = self.queryset
        from_date = self.request.query_params.get('from')
        to_date = self.request.query_params.get('to')
        query_set = queryset.filter(
            bookedAt__range=[from_date, to_date]).order_by('-bookedAt')
        return query_set

class GetBookingByDateAll(viewsets.ModelViewSet):
    queryset = BookingReport.objects.all()
    serializer_class = GetAllBooking

    def get_queryset(self):
        queryset = self.queryset
        from_date = self.request.query_params.get('from')
        to_date = self.request.query_params.get('to')
        query_set = queryset.filter(
            bookedAt__range=[from_date, to_date]).order_by('bookedAt')
        return query_set