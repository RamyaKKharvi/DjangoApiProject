from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.MemberCreate.as_view(), name='create'),
    path('update<memberid>/', views.MemberUpdate.as_view(), name='update'),
    path('delpage<memberid>/', views.MemberDeletePage.as_view(), name='delpage'),
    path('delete<memberid>/', views.MemberDelete.as_view(), name='delete'),
]
