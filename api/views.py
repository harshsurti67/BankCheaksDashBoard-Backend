# import json
# from rest_framework.decorators import api_view
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated

# from rest_framework.response import Response
# from rest_framework import status
# from .models import UserData
# from .serializers import UserSerializer
# from django.contrib.auth.hashers import check_password
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import get_user_model 
# from django.http import JsonResponse

# User = get_user_model()

# #
# @api_view(['GET', 'PUT'])
# def user_profile(request):
#     user_id = request.headers.get('user-id')  # Custom simple auth method

#     if not user_id:
#         return Response({'error': 'User ID not provided.'}, status=400)

#     try:
#         user = UserData.objects.get(id=user_id)
#     except UserData.DoesNotExist:
#         return Response({'error': 'User not found.'}, status=404)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         user.name = request.data.get("name", user.name)
#         user.save()
#         return Response({'message': 'Profile updated successfully!'})
# @api_view(['POST'])
# def signup(request):
#     email = request.data.get('user_email')
#     password = request.data.get('password')
#     name = request.data.get('name')
#     print(request.data)
#     # # Check if email, password, and name are provided
#     # if email is None or password is None or  name is None:
#     if not email or not password or not name:
#         return Response({'msg': 'Email, password, and name are required.'}, status=status.HTTP_400_BAD_REQUEST)
#      # Check if the email is already registered
#     if UserData.objects.filter(user_email=email).exists():
#         return Response({'msg': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         # Create new user
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             #  Send confirmation email
#             subject = "Welcome to Movie Ticket Booking!"
#             message = f"Hello {name},\n\nThank you for signing up! Your account has been created successfully.\n\nBest Regards,\nMovie Ticket Booking Team"
#             from_email = settings.EMAIL_HOST_USER
#             recipient_list = [email]
#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#             return Response({'msg': 'User created successfully! Please check your email for confirmation.'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
       
# @api_view(['POST'])
# def login(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     # Check if email and password are provided
#     if not email or not password:
#         return Response({'msg': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         # Try to get the user by email
#         user = UserData.objects.get(user_email=email)

#         # Verify the password
#         if check_password(password, user.password):
#             # Send the matched user's data in the response
#             serializer = UserSerializer(user)
#             return Response({'msg': 'Login successful', 'user': serializer.data}, status=status.HTTP_200_OK)
#         else:
#             # Invalid password
#             return Response({'msg': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
#     except UserData.DoesNotExist:
#         # User not found (same error message for invalid email or non-existent user)
#         return Response({'msg': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)







from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserData
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password, make_password

# --- Signup ---
@api_view(['POST'])
def signup(request):
    email = request.data.get('user_email')
    password = request.data.get('password')
    name = request.data.get('name')

    if not email or not password or not name:
        return Response({'msg': 'Email, password, and name are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if UserData.objects.filter(user_email=email).exists():
        return Response({'msg': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Hash the password before saving
        request.data['password'] = make_password(password)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# --- Login ---
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'msg': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = UserData.objects.get(user_email=email)

        if check_password(password, user.password):
            serializer = UserSerializer(user)
            return Response({'msg': 'Login successful', 'user': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

    except UserData.DoesNotExist:
        return Response({'msg': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

# --- User Profile ---
@api_view(['GET', 'PUT'])
def user_profile(request):
    user_id = request.headers.get('user-id')  # Custom simple auth method

    if not user_id:
        return Response({'error': 'User ID not provided.'}, status=400)

    try:
        user = UserData.objects.get(id=user_id)
    except UserData.DoesNotExist:
        return Response({'error': 'User not found.'}, status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        user.name = request.data.get("name", user.name)
        user.save()
        return Response({'message': 'Profile updated successfully!'})
