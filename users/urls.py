from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import MyObtainTokenPairView, RegisterView, CurrentUserView
urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path('login/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile/', CurrentUserView.as_view())
]