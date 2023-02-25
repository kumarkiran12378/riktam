
from django.urls import path, include
from user.views import UserViewSet, GroupViewSet, ListGroupchat, LikeMessage
from rest_framework.routers import DefaultRouter
from user.views import UserLogin, UserLogout, SendMessage

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLogin),
    path('logout/', UserLogout),
    path('send_message/', SendMessage),
    path('groupchat/', ListGroupchat.as_view(), name='groupchat'),
    path('likemessage/', LikeMessage.as_view(), name='likemessage')
]
