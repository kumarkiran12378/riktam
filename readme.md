RIKTAM GROUP CHAT APPLICATION:

Tech Stack: Python, Django, SqLite
Python Packages: Django 4.1, djangorestframework 3.14

Set up(Linux):
Virtual environment:
Create command: Python3 -m venv virtual_env_name
To activate: source virtual_env_name/bin/activate
Install Python Packages:
	pip install -r requirement.txt
To run Django server:
	Python manage.py makemigrations user
	Python manage.py migrate
	Python manage.py runserver 8000

API Server URL: http://localhost:8000/



Basic Auth
Username: kiran@gmail.com
Password: 123456

ADMIN/USER Related APIs:
To create Admin user(Authentication Required):
API: http://localhost:8000/api/users/
Method: POST
Request body:
{
   "full_name": "Kiran Pradhan",
   "email": "kiran@gmail.com",
   "mobile_no": "9040613000",
   "password": "123456",
   "status": 1,
   "isAdmin": 1
}


To create user(Authentication Required):
API: http://localhost:8000/api/users/
Method: POST
Request body:
{
   "full_name": "Kiran Pradhan",
   "email": "kiran1@gmail.com",
   "mobile_no": "9040613000",
   "password": "123456",
   "status": 1,
   "isAdmin": 0
}

To list users:
API: http://localhost:8000/api/users/
Method: GET

To Update Users:
API:localhost:8000/api/users/{user id}/
Method: PUT/PATCH
Request Body: 
{
   "full_name": "Kiran Pradhan",
   "email": "kiran4@gmail.com",
   "mobile_no": "9040613006",
   "password": "123456",
   "status": 1,
   "isAdmin": 0
}

To delete User:
API: localhost:8000/api/users/{user id}/
Method: DELETE

User/Admin Authentication API:

Login API:
API: http://localhost:8000/api/login/
Method: POST
Requires body
{
   "email": "kiran@gmail.com",
   "password": "123456"
}
Response:
{
   "Message": "Login Success.",
   "session_id": "4d435fea-748b-4948-89fd-bf52c415685e"
}

Logout API:
API: http://localhost:8000/api/logout/
Method: POST
Requires body:
{
   "email": "kiran@gmail.com",
   "session_id": "4d435fea-748b-4948-89fd-bf52c415685e"
}


GROUP Related APIs

To create Group:
API: http://localhost:8000/api/groups/
Method: POST
Request Body:
{
  "name": "group3",
  "created_by": 1,
  "users": [1,3,4]
}


To update Group:
API: http://localhost:8000/api/groups/1/
Method: PUT/PATCH
Request Body:
{
  "name": "group3",
  "created_by": 1,
  "users": [1,4,3]
}


To send Message:
API: http://localhost:8000/api/send_message/
METHOD: POST
Request Body:
{
   "groupid": 1,
   "userid": 1,
   "message": "Hi All"
}
To List Group Chat:
API: http://localhost:8000/api/groupchat/?groupid=1
Method: GET


To like a Message:
API: http://localhost:8000/api/likemessage/
Method: POST
Request Body:
{
   "mid":1,
   "userid":1
}

