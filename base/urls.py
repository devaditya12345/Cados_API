from django.urls import path
from .import views

#TOKEN lene ke 'token/' endpoint se
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns=[
    path('',views.endpoints),
    path('advocates',views.advocate_list),
    path('advocates/<str:username>',views.advocate_detail),

    path('companies',views.companies_list),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#we don't have to build a view for this
]