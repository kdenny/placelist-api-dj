from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from user_mgmt.views import *

urlpatterns = [
    url(r'^login/$', obtain_jwt_token),
    url(r'^verify_token/$', verify_jwt_token),
    url(r'^get_username/$', Username.as_view()),
    # url(r'^register/$', Register.as_view()),
]
