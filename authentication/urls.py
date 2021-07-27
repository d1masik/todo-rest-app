from django.urls import path

from authentication.views import RegisterView, IpUsersListView

app_name = 'api/v1'
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('this_ip_users/', IpUsersListView.as_view())
]
