from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Admin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='admin')

    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    mobileNumber = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    dateOfBirth = models.DateField()
    start_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.firstName)


class turfDetails(models.Model):
    admin = models.OneToOneField(
        Admin, on_delete=models.CASCADE, related_name='turfDetails')
    turfName = models.CharField(max_length=125)
    mobileNumber = models.CharField(max_length=12, unique=True)
    openingTime = models.TimeField(auto_now=False, auto_now_add=False)
    closingTime = models.TimeField(auto_now=False, auto_now_add=False)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    addressOfTurf = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    amenities = models.CharField(max_length=225)

    def __str__(self):
        return str(self.turfName)


class turfImages(models.Model):
    turfDetails = models.ForeignKey(
        turfDetails, on_delete=models.CASCADE, related_name='turfImages')
    generalTurfImages = models.ImageField(
        upload_to="images", blank=True, null=True)

    def __str__(self):
        return str(self.turfDetails.turfName)


class GroundDetails(models.Model):
    turfId = models.ForeignKey(
        turfDetails, on_delete=models.CASCADE, related_name='GroundDetails')
    groundName = models.CharField(max_length=225)
    description = models.CharField(max_length=225,null=True)
    groundOpeningTime = models.TimeField(
        blank=False, auto_now=False, auto_now_add=False)
    groundClosingTime = models.TimeField(
        blank=False, auto_now=False, auto_now_add=False)
    gamesToPlay = models.CharField(max_length=225, blank=False)
    numberOfPlayers = models.IntegerField()
    defaultPrice = models.IntegerField(null=True)

    def __str__(self):
        return str(self.groundName)


class GroundImages(models.Model):
    GroundDetails = models.ForeignKey(
        GroundDetails, on_delete=models.CASCADE, related_name='GroundImages')
    groundImages = models.ImageField(
        upload_to="groundImages", blank=True, null=True)

    def __str__(self):
        return str(self.GroundDetails.groundName)


class GroundPricing(models.Model):
    groundId = models.ForeignKey(
        GroundDetails, on_delete=models.CASCADE, related_name='GroundPricing')
    slotOpeningTime = models.TimeField(
        blank=False, auto_now=False, auto_now_add=False)
    slotClosingTime = models.TimeField(
        blank=False, auto_now=False, auto_now_add=False)
    price = models.IntegerField()
    day = models.CharField(max_length=225)

    def __str__(self):
        return str(self.groundId.groundName)


class CoachingTime(models.Model):
    groundId = models.ForeignKey(
        GroundDetails, on_delete=models.CASCADE, related_name='CoachingTime')
    startingTime = models.TimeField(blank=True)
    endingTime = models.TimeField(blank=True)

    def __str__(self):
        return str(self.groundId.groundName)


class AdminSettings(models.Model):
    groundId = models.ForeignKey(
        GroundDetails, on_delete=models.CASCADE, related_name='ground_setting')
    adv = models.IntegerField()
    paymentCompletion = models.CharField(max_length=225, default='Before')
    paymentMode = models.CharField(max_length=225, default='Online')
    bufferTime = models.IntegerField()
    paymentMethod = models.CharField(
        max_length=50, default='Advance')

    def __str__(self):
        return str(self.groundId.groundName)


class PlayersAccount(models.Model):
    userName = models.CharField(max_length=100)
    colorCode=models.CharField(max_length=100,default='#EFF0FF#656BFF')
    phoneNumber = models.CharField(max_length=125, unique=True)
    email = models.EmailField(max_length=254, unique=True, null=True)
    dateOfBirth = models.DateField(
        blank=False, auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return str(self.userName)


class PaymentReport(models.Model):
    otp = models.CharField(max_length=125)
    amount = models.CharField(max_length=125,default=0)
    playerId = models.ForeignKey(
        PlayersAccount, on_delete=models.CASCADE, related_name='payment_userid')
    paymentId = models.CharField(max_length=254, unique=True)
    paymentMethod = models.CharField(
        max_length=125, default='Advance')
    paymentType = models.CharField(
        max_length=125, default='online')
    paymentStatus = models.CharField(
        max_length=125, default='Pending')
    Status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.playerId.userName)


class BookingReport(models.Model):
    slotOpeningTime = models.TimeField(
        blank=False, auto_now=False, auto_now_add=False, default='00:00')
    slotClosingTime = models.TimeField(
        blank=False, auto_now=False, auto_now_add=False, default='00:00')
    playerId = models.ForeignKey(
        PlayersAccount, on_delete=models.CASCADE, related_name='booking_userid')
    bookingId = models.CharField(max_length=254, unique=True)
    turfId = models.ForeignKey(
        turfDetails, on_delete=models.CASCADE, related_name='turf_detailid')
    groundId = models.ForeignKey(
        GroundDetails, on_delete=models.CASCADE, related_name='ground_detailid')
    bookedAt = models.DateField(auto_now_add=False)
    updatedAt = models.DateTimeField(auto_now=True)
    bookingStatus = models.CharField(
        max_length=125, default='pending')
    slotPrice = models.CharField(
        max_length=125, default=0)
    paymentId = models.ForeignKey(
        PaymentReport, on_delete=models.CASCADE, related_name='paymentid_report')

    def __str__(self):
        return str(self.playerId.userName)


class CanceledReport(models.Model):

    playerId = models.ForeignKey(
        PlayersAccount, on_delete=models.CASCADE, related_name='cancel_report')
    cancellationId = models.CharField(unique=True, max_length=254)
    cancellationStatus = models.BooleanField(default=False)
    cancellationDate = models.DateTimeField(auto_now_add=True)
    cancellationFee = models.CharField(max_length=100)
    refund = models.CharField(max_length=100)
    paymentId = models.ForeignKey(
        PaymentReport, on_delete=models.CASCADE, related_name='paymentid_cancel')
    bookingId = models.ForeignKey(
        BookingReport, on_delete=models.CASCADE, related_name='bookinid_cancel')
