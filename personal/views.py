from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from public_chat.models import PublicChatRoom

DEBUG = False 

def home_screen_view(request, *args, **kwargs):
	room_id = request.GET.get("room_id")
	room = PublicChatRoom.objects.get(id=room_id)
	if room.users.count() <= room.max_members -1:

		context = {}
		room_name = PublicChatRoom.objects.get(id=room_id).title
		max_mebers = room.max_members
		context['debug_mode'] = settings.DEBUG
		context['debug'] = DEBUG
		context['room_id'] = room_id
		context['title'] = room_name
		context['max_members'] = max_mebers
		return render(request, "personal/home.html", context)
	else:
		return HttpResponse("<h1>Sorry this chat room is full</h1>")








