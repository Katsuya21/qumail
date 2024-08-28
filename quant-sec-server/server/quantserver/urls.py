from django.conf.urls import url
import quantserver.views as views


urlpatterns = [
    url("get-public-key", views.getUserPublicKey),
    url("post-email", views.postEmail),
    url("register-user", views.registerUser),
    url("check-uniqueness", views.checkForUniqueness),
    url("get-inbox", views.returnInbox),
    url("clear-inbox", views.clearInbox),
]
