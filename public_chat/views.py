
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from public_chat.models import PublicChatRoom
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from public_chat.forms import ChatUploadForm


def find_chat_room(request, *args, **kwargs):
    context = {}

    context['chat_room'] = PublicChatRoom.objects.all().order_by("-date_created")

    return render(request, 'public_chat/find_chat_room.html', context)


def give_title(request, *args, **kwargs):
    context = {}
    try:
        room_id = request.GET.get("room_id")

        room = PublicChatRoom.objects.get(id=room_id)
        room_name = room.title 

        user_count = room.users.count()

        context['title'] = room_name
    except room.DoesNotExist:
        return redirect('public_chat:find-chat-room')

    return render(request, 'public_chat/snippets/public_chat_room.html')


@login_required
def create_chat_room(request):

    if request.method == 'POST':
        u_form = ChatUploadForm(request.POST)
        #u_form.instance.author = request.user
    else:
        u_form = ChatUploadForm()
        #u_form.instance.author = request.user 



    if u_form.is_valid():
        u_form.save()
        messages.success(request, 'Chat creation was successful')
        return redirect('public_chat:find-chat-room')

    context = {
        'u_form': u_form,
    }
    return render(request, 'public_chat/chat_form.html', context)








