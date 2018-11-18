from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password
import json
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return return_all_users(request)
    elif request.method == 'POST':
        return create_user(request)


def return_all_users(request):
    try:
        users = User.objects.all()
        users_return = {}
        for usr in users:
            users_return[usr.id] = {
                'id': usr.id,
                'username': usr.username,
                'email': usr.email,
                'created_at': usr.date_joined,
                'updated_at': usr.last_login
            }

        return JsonResponse(users_return,
                            status=200)

    except:
        return JsonResponse({
            'status': 'internal_server_error'
        },
            status=500)


def create_user(request):
    try:
        # username: string # Nombre de cuenta
        # passwordHash: string # la password ya pasada por una función hash.
        # birthdate: date # Fecha de nacimiento del usuario.
        username = request.POST['username']
        password = request.POST['passwordHash']
        email = request.POST['email']
        if username and password and email:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password)

                return JsonResponse({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'created_at': user.date_joined,
                    'updated_at': user.last_login
                },
                    status=201)
            except IntegrityError as err:
                return JsonResponse({'status': 'data already exists'},
                                    status=422)

    except KeyError:
        return JsonResponse({
            'status': 'Given parameters do not match the correct ones'
        },
            status=422)


def specific_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return JsonResponse({user.id: {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.date_joined,
            'updated_at': user.last_login
        }},
            status=200)

    except User.DoesNotExist as err:
        return JsonResponse({
            'status': 'User: {} does not exist'.format(user_id)
        },
            status=204)

    except:
        return JsonResponse({
            'status': 'Internal_server_error'
        },
            status=500)


@csrf_exempt
def delete_user(request):
    try:
        user = User.objects.get(id=int(request.POST['id']))
        user.check_password(request.POST['passwordHash'])
        if not user.check_password(request.POST['passwordHash']):
            return JsonResponse({
                'status': 'Given data is incorrect'},
                status=204)
        else:
            user.delete()
            return JsonResponse({
                'status': 'Deleted user: {}'.format(request.POST['id'])
            },
                status=200)

    except User.DoesNotExist as err:
        return JsonResponse({
            'status': 'Given data is incorrect'},
            status=204)

    except ValueError as err:
        return JsonResponse({
            'status': 'Given data is incorrect'},
            status=204)

    except:
        return JsonResponse({
            'status': 'internal_server_error'
        },
            status=500)


def user_groups(request, user_id):
    
    try:
        user = User.objects.get(id=user_id)
        groups_return = {}
        for grp in user.groups.all():
            groups_return[grp.id] = {
                'id': grp.id,
                'name': grp.name
            }


        return JsonResponse(groups_return,
                            status=200)


    except User.DoesNotExist as err:
        return JsonResponse({
            'status': 'User: {} does not exist'.format(user_id)
        },
            status=204)

    except:
        return JsonResponse({
            'status': 'internal_server_error'
        },
            status=500)

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({user.id: {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.date_joined,
            'updated_at': user.last_login
        }}, status=200)
    else:
        return JsonResponse({
            'status': 'User does not exist or credentials are invalid'
        },
            status=204)

def user_logout(request):
    logout(request)
    return JsonResponse({'status': 'Logout successful'}, status=200)