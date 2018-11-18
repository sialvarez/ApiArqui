from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User, Group

from comments.models import Comment


def index(request):
    if request.method == "GET":
        return return_all_comments(request)
    return HttpResponse("You should only use GET method here.")


# para index
def return_all_comments(request):
    try:
        comments = Comment.objects.all()
        comments_return = {}
        for msg in comments:
            comments_return[msg.id] = {
                "id": msg.id,
                "sender": msg.sender.id,
                "receiver": msg.receiver.id,
                "msg_content": msg.msg_content,
                "created_at": msg.created_at,
            }

        return JsonResponse(comments_return, status=200)

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# [GET] /inbox/
def inbox(request):
    try:
        user = request.user
        comments = Comment.objects.all()
        comments_return = {}
        for msg in comments:
            if int(msg.sender.id) == user.id:
                comments_return[msg.id] = {
                    "id": msg.id,
                    "sender": msg.sender.id,
                    "receiver": msg.receiver.id,
                    "msg_content": msg.msg_content,
                    "created_at": msg.created_at,
                }

        # cuando tenga lo de groups hechos (rodrigo esta avanzando)
        for msg in comments:
            if msg.receiver in user.groups.all():
                comments_return[msg.id] = {
                    "id": msg.id,
                    "sender": msg.sender.id,
                    "receiver": msg.receiver.id,
                    "msg_content": msg.msg_content,
                    "created_at": msg.created_at,
                }

        return JsonResponse(comments_return, status=200)

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# [GET] /inbox/received/
def inbox_r(request):
    try:
        user = request.user
        comments = Comment.objects.all()
        comments_return = {}
        # cuando tenga lo de groups hechos (rodrigo esta avanzando)
        for msg in comments:
            if msg.receiver in user.groups.all():
                comments_return[msg.id] = {
                    "id": msg.id,
                    "sender": msg.sender.id,
                    "receiver": msg.receiver.id,
                    "msg_content": msg.msg_content,
                    "created_at": msg.created_at,
                }

        return JsonResponse(comments_return, status=200)

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# [GET] /inbox/sent
def inbox_s(request):
    try:
        user = request.user
        comments = Comment.objects.all()
        comments_return = {}
        for msg in comments:
            if int(msg.sender.id) == user.id:
                comments_return[msg.id] = {
                    "id": msg.id,
                    "sender": msg.sender.id,
                    "receiver": msg.receiver.id,
                    "msg_content": msg.msg_content,
                    "created_at": msg.created_at,
                }

        return JsonResponse(comments_return, status=200)

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# [GET] /groups/{group_id}/messages
def group_messages(request, group_id):
    try:
        user = request.user
        group = Group.objects.get(id=int(group_id))
        comments_return = {}
        if group not in user.groups.all():
            return comments_return

        comments = Comment.objects.all()
        for msg in comments:
            if int(msg.receiver.id) == group_id:
                comments_return[msg.id] = {
                    "id": msg.id,
                    "sender": msg.sender.id,
                    "receiver": msg.receiver.id,
                    "msg_content": msg.msg_content,
                    "created_at": msg.created_at,
                }

        return JsonResponse(comments_return, status=200)

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# [GET] /inbox/{message_id}   # falta un poco
def specific_inbox_message(request, message_id):
    try:
        user = request.user
        comments = Comment.objects.all()
        comments_return = {}
        msg = Comment.objects.get(id=message_id)

        if int(msg.sender.id) == user.id or msg.receiver in user.groups.all():
            comments_return[msg.id] = {
                "id": msg.id,
                "sender": msg.sender.id,
                "receiver": msg.receiver.id,
                "msg_content": msg.msg_content,
                "created_at": msg.created_at,
            }

        return JsonResponse(comments_return, status=200)

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# [GET] /inbox/sent/{message_id}# falta un poco
def specific_inbox_s_message(request, message_id):
    try:
        user = request.user
        comments = Comment.objects.all()
        comments_return = {}
        msg = Comment.objects.get(id=message_id)

        if int(msg.sender.id) == user.id:
            comments_return[msg.id] = {
                "id": msg.id,
                "sender": msg.sender.id,
                "receiver": msg.receiver.id,
                "msg_content": msg.msg_content,
                "created_at": msg.created_at,
            }

        return JsonResponse(comments_return, status=200)

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# [GET] /inbox/recieved/{message_id}# falta un poco
def specific_inbox_r_message(request, message_id):
    try:
        user = request.user
        comments = Comment.objects.all()
        comments_return = {}
        msg = Comment.objects.get(id=message_id)

        if msg.receiver in user.groups.all():
            comments_return[msg.id] = {
                "id": msg.id,
                "sender": msg.sender.id,
                "receiver": msg.receiver.id,
                "msg_content": msg.msg_content,
                "created_at": msg.created_at,
            }

        return JsonResponse(comments_return, status=200)

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# [GET] /groups/{group_id}/messages/{message_id}
# la explicacion de esto esta raro en la API, aparte de eso no lo usaria
# #porque creo que es algo muy especifico que no tendria mucha utilidad.


def user_comments(request, user_id):
    print(f"{user_id} USUARIOOOOOOO\n\n")
    try:
        user = User.objects.get(id=user_id)
        comments = Comment.objects.all()
        comments_return = {}
        for msg in comments:
            if msg.sender == user_id:
                comments_return[msg.id] = {
                    "id": msg.id,
                    "sender": msg.sender,
                    "receiver": msg.receiver,
                    "msg_content": msg.msg_content,
                    "created_at": msg.created_at,
                }

        return JsonResponse(comments_return, status=200)

    except User.DoesNotExist as err:
        return JsonResponse(
            {"status": "User: {} does not exist".format(user_id)}, status=204
        )

    except:
        return JsonResponse({"status": "internal_server_error"}, status=500)


# POST

# [POST] /public/messages
# No aplica


# [POST] /inbox/sent
# No aplica


# [POST] /groups/{group_id}/messages

def create_group_comment(request, group_id):
    group_receiver = get_object_or_404(Group, id=group_id)
    user_sender = get_object_or_404(User, id=request.POST["sender"])
    content = request.POST.get["msg_content"]
    try:
        Comment.objects.create(
            receiver=group_receiver, sender=user_sender, msg_content=content
        )
        return JsonResponse(
            {"group_id": group_receiver.id, "msg_content": content}, status=201
        )
    except:
        return JsonResponse({"status": "Internal_server_error"}, status=500)


# [POST] /public/messages/{message_id}
# No aplica


# [POST] /inbox/recieved/{message_id}
# No aplica


# [POST] groups/{group_id}/messages/{message_id}

def create_group_comment_reply(request, group_id, comment_id):
    group_receiver = get_object_or_404(Group, id=group_id)
    parent_comment = Comment.objects.get(receiver=group_receiver)
    if parent_comment:
        user_sender = get_object_or_404(User, id=request.POST["sender"])
        content = request.POST.get["msg_content"]
        try:
            Comment.objects.create(
                receiver=group_receiver,
                sender=user_sender,
                msg_content=content,
                reply_to=parent_comment,
            )
            return JsonResponse(
                {"group_id": group_receiver.id, "msg_content": content}, status=201
            )
        except:
            return JsonResponse({"status": "Internal_server_error"}, status=500)
    else:
        return JsonResponse(
            {"status": "Given parameters do not match the correct ones"}, status=422
        )
