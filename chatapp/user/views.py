from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer, GroupSerializer
from user.models import User, UsersLogin, Group, GroupMessage
from user.permission import IsAuthenticatedAdmin
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.db.models import F
from django.shortcuts import render
import json
import uuid


def index_view(request):
    '''Index view Function'''
    template = 'index.html'
    return render(request, template)

class UserViewSet(viewsets.ModelViewSet):
    """
    User Viewsets for all API methods.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAdmin]

class GroupViewSet(viewsets.ModelViewSet):
    """
    Group Viewsets for all API methods.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ListGroupchat(APIView):
    def get(self, request):
        """
        GET API to get chat messages of a group by providing group id.
        """
        groupID = request.GET.get('groupid')
        groupchat = list(GroupMessage.objects.filter(group=groupID).values())
        return Response(groupchat)


class LikeMessage(APIView):
    def post(self, request):
        """
        POST API to like a message by provind message id(mid).
        """
        request_data = json.loads(request.body)
        mid = request_data.get('mid')
        GroupMessage.objects.filter(id=mid).update(likes=F('likes')+1)
        return Response({'detail': 'Like done.'})




def UserLogin(request):
    if request.method == 'POST':
        """
        User login API.
        """
        request_data = json.loads(request.body)
        username = request_data.get("email")
        password = request_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            session_id = str(uuid.uuid4())
            UsersLogin.objects.create(
                        user=user,
                        session_id = session_id
                    )
            return JsonResponse({"Message": "Login Success.",
            "session_id": session_id})
        else:
            return JsonResponse({"Message": "Login Failed."})

 
def UserLogout(request):
    if request.method == 'POST':
        """
        Logout API.
        """
        request_data = json.loads(request.body)
        session_id = request_data.get("session_id")
        deleted_session = UsersLogin.objects.filter(session_id=session_id).delete()
        if deleted_session[0]:
            return JsonResponse({"Message":"User logged out."})
        else:
            return JsonResponse({"Message":"Session not present."}, status=500)


def SendMessage(request):
    if request.method == 'POST':
        """
        POST API to send message to a group.
        """
        request_data = json.loads(request.body)
        groupid = request_data.get("groupid")
        userid = request_data.get("userid")
        message = request_data.get("message")
        try:
            group = Group.objects.get(id=groupid, users=userid)
            user = User.objects.get(uid=userid)
        except Exception as e:
            return JsonResponse({"Message":"Please provide correct groupid and userid."}, status=500)
        if group:
            GroupMessage.objects.create(group = group, user = user, message=message)
            return JsonResponse({"Message":"Your message sent to group."})
        else:
            return JsonResponse({"Message":"Please provide group and user."}, status=500)

