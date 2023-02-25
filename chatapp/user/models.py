from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    """
    User model custom manager.
    """
    def create(self, **validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        userdemo = User(**validated_data)
        userdemo.save()
        return userdemo


class User(AbstractBaseUser):
    """
    User Model.
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('uid','password')
    uid = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=127)
    email = models.EmailField(max_length=63, unique=True)
    mobile_no = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=127)
    status = models.SmallIntegerField()
    isAdmin = models.BooleanField()

    objects = UserManager()
    
    class Meta:
        db_table = 'user'

class Group(models.Model):
    """
    Group Model.
    """
    name = models.CharField(max_length=63, unique=True)
    users = models.ManyToManyField(User)
    created_by = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'group'


class UsersLogin(models.Model):
    """
    login details model.
    """
    user = models.ForeignKey(
        User, related_name='login_details', on_delete=models.CASCADE, db_column='uid')
    login_date = models.DateField(auto_now=True)
    session_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'users_login'

class GroupMessage(models.Model):
    """
    Group chat model.
    """
    group = models.ForeignKey(
        Group, related_name='group_details', on_delete=models.CASCADE, db_column='gid')
    user = models.ForeignKey(
        User, related_name='user_details', on_delete=models.CASCADE, db_column='uid')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    class Meta:
        db_table = 'group_message'

