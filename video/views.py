from django.shortcuts import render
from video.models import Video, OVideo
from django.contrib.auth.decorators import login_required
from .forms import VideoUploadForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def video_view(request):
    video = Video.objects.all()
    ovideo = OVideo.objects.all()

    context = {}
    context['videos'] = video.order_by('-date_posted')
    context['ovideos'] = ovideo
    context['is_paginated'] = 3
    return render(request, "video/index.html", context)

class VideoView(ListView):
    model = Video 
    template_name = 'video/index.html'
    context_object_name = 'videos'
    ordering = ['-date_posted']
    paginate_by = 5


'''
class VideoDetailView(DetailView):
    model = Video
'''
    
viewed_list = []
def VideoDetailView(request, *args, **kwargs):
    context = {}
    video_id = kwargs.get('pk')


    video = Video.objects.get(id=video_id)
    if request.user.is_authenticated:
        video.add_view()
        viewed_list.append(request.user)

    context['video'] = video

    return render(request, "video/video_detail.html", context)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    success_url = '/videos'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False 


@login_required
def VideoCreateView(request):

    if request.method == 'POST':
        u_form = VideoUploadForm(request.POST)
        u_form.instance.author = request.user
    else:
        u_form = VideoUploadForm()
        u_form.instance.author = request.user 



    if u_form.is_valid():
        u_form.save()
        messages.success(request, 'Video submission was successful')
        return redirect('video:videos-home')

    context = {
        'u_form': u_form,
    }
    return render(request, 'video/video_form.html', context)


    
 