from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('hospital/', views.HospitalView.as_view(), name='hospital'),
    path('hospital/<id>',views.SingleHospitalView.as_view(),name='singleHospital'),
    path('hospital/register',views.HospitalRegistrationView.as_view(),name='register'),
    path('hospital/login',views.HospitalLoginView.as_view(),name='login'),
    path('doctors/', views.DoctorDetailsView.as_view(), name='doctors'),
    path('doctorsdetail/<id>/', views.DoctorView.as_view(), name='doctordetail'),
    path('hospital-notifications/',views.HospitalNotificationView.as_view(), name='hospital-notification'),
    path('hospital-notifications/<id>/',views.HospitalNotificationDetailView.as_view(), name='hospital-notification-detail'),

   

]


if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)