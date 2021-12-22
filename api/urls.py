from django.urls import path
from .views import CompanyViews

urlpatterns = [
    path('companies/', CompanyViews.as_view(), name='company_list'),
    path('companies/<int:id>', CompanyViews.as_view(), name='company_process')
]