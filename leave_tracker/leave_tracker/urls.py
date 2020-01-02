from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from leave_sys.views import StaffViewset, LeaveViewset, LeaveTypeViewset, HolidayViewset



router = routers.DefaultRouter()
router.register(r'staff', StaffViewset, 'staff')
router.register(r'leave', LeaveViewset, 'leave')
router.register(r'leavetype', LeaveTypeViewset, 'leavetype')
router.register(r'holiday', HolidayViewset, 'holiday')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth', include('rest_framework.urls', namespace='rest_framework'))
]
