from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('registration/', views.SignUpView.as_view(), name='registration'),
    path('change-password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('contact-us/', views.contact_view, name='contact'),
    path('book-details/<int:book_id>/', views.book_details, name='book_details'),
    path('book-issue/<int:book_id>/', views.book_issue, name='book_issue'),
    path('my-book-issue-list/', views.my_book_issue_list, name='my_book_issue_list'),
]
