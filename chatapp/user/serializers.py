from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import User, Group
from user.validators import validate_mobile_format, validate_email_format

class UserSerializer(serializers.Serializer):
    """
    User serializer to serialize request and response data.
    """
    uid = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(User.objects.all()), validate_email_format])
    mobile_no = serializers.CharField(required=True, validators=[UniqueValidator(User.objects.all()), validate_mobile_format])
    password = serializers.CharField(required=True, write_only=True)
    status = serializers.IntegerField(required=True)
    isAdmin = serializers.BooleanField(required=True)
    
    class Meta:
        model = User
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        fields = super().get_fields()
        for field in fields:
            if not fields[field].read_only and field in validated_data:
                try:
                    setattr(instance, field, validated_data[field])
                except TypeError:
                    getattr(instance, field).set(validated_data[field])
        instance.full_clean()
        instance.save()
        return instance

class GroupSerializer(serializers.Serializer):
    """
    Group serializer to serialize request and response data.
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    users = serializers.PrimaryKeyRelatedField(
        allow_empty=True, many=True, queryset=User.objects.all(), required=False)
    created_by = serializers.IntegerField(required=True)
    created_data = serializers.DateField(read_only=True)

    class Meta:
        model = Group

    def create(self, validated_data):
        """
        To create new Group.
        """
        users = validated_data.pop('users')
        group_instance = Group.objects.create(**validated_data)
        group_instance.users.add(*users)
        return group_instance
    
    def update(self, instance, validated_data):
        """
        M2M table Update.
        """
        fields = super().get_fields()
        for field in fields:
            if not fields[field].read_only and field in validated_data:
                try:
                    setattr(instance, field, validated_data[field])
                except TypeError:
                    getattr(instance, field).set(validated_data[field])
        instance.full_clean()
        instance.save()
        return instance

