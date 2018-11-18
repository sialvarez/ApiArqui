from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return all_groups(request)
    elif request.method == 'POST':
        return create_group(request)


def all_groups(request):
    try:
        groups = Group.objects.all()
        groups_return = {}
        for grp in groups:
            member_count = len(
                list(User.objects.filter(groups__name=grp.name)))
            groups_return[grp.id] = {
                'id': grp.id,
                'name': grp.name,
                'member_count': member_count

            }

        return JsonResponse(groups_return,
                            status=200)

    except:
        return JsonResponse({
            'status': 'internal_server_error'
        },
            status=500)


def specific_group(request, group_id):
    if request.method == 'GET':
        return info_specific(request, group_id)
    elif request.method == 'POST':
        return add_specific(request, group_id)


def info_specific(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
        member_count = len(list(User.objects.filter(groups__name=group.name)))
        return JsonResponse({group.id: {
            'id': group.id,
            'name': group.name,
            'member_count': member_count
        }},
            status=200)

    except Group.DoesNotExist as err:
        return JsonResponse({
            'status': 'Group: {} does not exist'.format(group_id)
        },
            status=204)

    except:
        return JsonResponse({
            'status': 'Internal_server_error'
        },
            status=500)


@csrf_exempt
def add_specific(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
        members = request.POST['users']

        for member in members:
            user = User.objects.get(id=member)
            group.user_set.add(user)
        return JsonResponse({group.id: {
            'id': group.id,
            'name': group.name,
            'member_count': member_count
        }},
            status=200)

    except Group.DoesNotExist as err:
        return JsonResponse({
            'status': 'Group: {} does not exist'.format(group_id)
        },
            status=204)

    except:
        return JsonResponse({
            'status': 'Internal_server_error'
        },
            status=500)


def users_of_group(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
        members = list(User.objects.filter(groups__name=group.name))
        return JsonResponse({group.id: {
            'id': group.id,
            'name': group.name,
            'member_count': len(members),
            'members': [{
                'id': member.id,
                'username': member.username,
                'email': member.email
            } for member in members
            ]
        }},
            status=200)

    except Group.DoesNotExist as err:
        return JsonResponse({
            'status': 'Group: {} does not exist'.format(group_id)
        },
            status=204)

    except:
        return JsonResponse({
            'status': 'Internal_server_error'
        },
            status=500)


def create_group(request):
    group_name = request.POST['name']
    if group_name:
        try:
            group = Group.objects.get_or_create(
                name=group_name)

            return JsonResponse({
                'id': user.id,
                'name': group_name
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
    return JsonResponse({
                'status': 'Given parameters do not match the correct ones'
            }, status=500)


@csrf_exempt
def remove_users(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
        members = request.POST['users']

        for member in members:
            user = User.objects.get(id=member)
            group.user_set.remove(user)
        return JsonResponse({},
                            status=204)

    except User.DoesNotExist as err:
        return JsonResponse({
            'status': 'One or more user(s) do not exist'},
            status=204)

    except:
        return JsonResponse({
            'status': 'Internal_server_error'
        },
            status=500)


@csrf_exempt
def delete_group(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
        group.delete()
        return JsonResponse({},
                            status=204)

    except Group.DoesNotExist as err:
        return JsonResponse({
            'status': 'Group: {} does not exist'.format(group_id)
        },
            status=204)

    except:
        return JsonResponse({
            'status': 'Internal_server_error'
        },
            status=500)
