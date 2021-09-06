from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

router.register('ceoapi', views.CeoModelViewSet,
basename = 'ceo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='obtainToken'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshToken'),

]
