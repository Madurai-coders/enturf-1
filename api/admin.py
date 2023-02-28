from django.contrib import admin
from .models import Admin, BookingReport,AdminSettings, CanceledReport, PaymentReport, PlayersAccount, turfDetails, turfImages, GroundDetails, GroundImages, GroundPricing, CoachingTime
# Register your models here.

admin.site.register(Admin)
admin.site.register(turfDetails)
admin.site.register(turfImages)
admin.site.register(GroundDetails)
admin.site.register(GroundPricing)
admin.site.register(GroundImages)
admin.site.register(CoachingTime)
admin.site.register(BookingReport)
admin.site.register(PaymentReport)
admin.site.register(PlayersAccount)
admin.site.register(CanceledReport)
admin.site.register(AdminSettings)
