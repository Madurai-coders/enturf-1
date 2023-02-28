from django.db import router
from django.urls import path, include
from .views import GetBookingByDate, GetAllAdminDataView,GetBookingByDateAll,AdminSettingViewset, AdminWithTurfDetailsViewset, BookingReportViewset, CanceledReportViewset, PaymentReportViewset, PlayerAccountViewset, UserListViewset, AdminListViewset, TurfDetailsViewset, TurfImageViewset, GroundDetailsViewset, GroundImagesViewset, GroundPricingViewset, CoachingTimeViewset, GetUserAccountList  # , UserCreateAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'create_user', UserListViewset, basename='crud_user')
router.register(r'create_admin', AdminListViewset, basename='crud_admin')
router.register(r'turf_details', TurfDetailsViewset,
                basename='add_turf_for_admin')
router.register(r'turf_image', TurfImageViewset,
                basename='add_image_for_admin')
router.register(r'add_ground', GroundDetailsViewset, basename='add_ground')
router.register(r'add_ground_images', GroundImagesViewset,
                basename='add_ground_images')
router.register(r'ground_pricing', GroundPricingViewset,
                basename='ground_pricing')
router.register(r'add_coaching_time', CoachingTimeViewset,
                basename='add_coaching_time')
router.register(r'player_acc', PlayerAccountViewset, basename='player_acc')

router.register(r'payment_report', PaymentReportViewset,
                basename='payment_report')
router.register(r'booking_report', BookingReportViewset,
                basename='booking_report')
router.register(r'canceled_report', CanceledReportViewset,
                basename='canceled_report')
router.register(r'admin_setting', AdminSettingViewset,
                basename='admin_setting')
router.register('GetBookingByDate', GetBookingByDate, basename='GetBookingByDate')
router.register('GetBookingByDateAll', GetBookingByDateAll, basename='GetBookingByDateAll')

                

urlpatterns = [
    path('', include(router.urls)),
    path('getuser', GetUserAccountList.as_view(), name='getuser'),
    path('vi', AdminWithTurfDetailsViewset.as_view(), name='vi'),
    path('get_admin_data/', GetAllAdminDataView.as_view(), name='get_admin_data'),
]
