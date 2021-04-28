from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Like, Post, Topic, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.views.generic.edit import FormView
from .forms import PostUploadForm, ImageUploadForm
from django.contrib import messages
from django.shortcuts import render, redirect
from friend.models import FriendList
from itertools import chain
from django.http import JsonResponse, request
from video.models import Video


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def topics(request):
    context = {}

    context['topics'] = Topic.objects.all()
    return render(request, "blog/topics.html", context)




def TopicView(request, *args, **kwargs):
    context = {}

    topic = kwargs.get('name')
    posts = Post.objects.filter(topic=topic).order_by('-date_posted')
    videos = Video.objects.filter(topic=topic).order_by('-date_posted')

    context['posts'] = posts
    context['paginate_by'] = 10 
    context['videos'] = videos
    context['topic_name'] = topic

    return render(request, 'blog/topic_view.html', context)


'''
def TopicView(request):
    context = {

    }
'''


class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10



'''
def PostListView(request):
    context = {}
    context['paginate_by'] = 10


    user = request.user 
    user_friend_list = FriendList.objects.get(user=user)
    friend_posts = []
    for post in Post.objects.all():
        if post.author in user_friend_list.friends.all():
            pass 
    return Post.objects.all().order_by("-date_posted")
'''




@login_required
def like_posts(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()

        # data = {
        #     'value': like.value,
        #     'likes': post_obj.liked.all().count()
        # }

        # return JsonResponse(data, safe=False)
    return redirect('blog:blog-home')




@login_required
def liked_posts(request):
    context = {}

    liked_posts = []
    for post in Post.objects.all().order_by("-date_posted"):
        if request.user in post.liked.all():
            liked_posts.append(post)

    context['liked_posts'] = liked_posts



    return render(request, 'blog/liked_posts.html', context)



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')





class PostDetailView(DetailView):
    model = Post

    '''
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        comments = Post.objects.all()
        context['comments'] = comments
    '''


'''
def PostDetailView(request, *args, **kwargs):
    context = {}
    post_id = kwargs.get('pk')
    post = Post.objects.get(id=post_id)
    #comments = Comment.objects.filter(post=post)
    context['object'] = post
    #context['comments'] = comments



    

    return render(request, "blog/post_detail.html", context)
'''

@login_required
def PostCreateView(request):

    if request.method == 'POST':
        u_form = PostUploadForm(request.POST, request.FILES)
        u_form.instance.author = request.user
    else:
        u_form = PostUploadForm()
        u_form.instance.author = request.user 



    if u_form.is_valid():
        u_form.save()
        messages.success(request, 'Post submission was successful')
        return redirect('blog:blog-home')

    context = {
        'u_form': u_form,
    }
    return render(request, 'blog/post_form.html', context)


'''
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False 
'''

def PostUpdateView(request, *args, **kwargs):
    post_id = kwargs.get('pk')
    if request.method == 'POST':
        u_form = PostUploadForm(request.POST, request.FILES, instance=Post.objects.get(id=post_id))
        u_form.instance.author = request.user
    else:
        u_form = PostUploadForm()
        u_form.instance.author = request.user 



    if u_form.is_valid():
        u_form.save()
        messages.success(request, 'Post submission was successful')
        return redirect('blog:blog-home')

    context = {
        'u_form': u_form,
    }
    return render(request, 'blog/post_update.html', context)



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/videos'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False 


def topic_search_view(request, *args, **kwargs):
	context = {}


    
	if request.method ==  "GET":
		search_query = request.GET.get("q")
		if len(search_query) > 0:
			search_results = Topic.objects.filter(name__icontains=search_query).distinct()
			user = request.user
			accounts = []
			for user in search_results:
				accounts.append(user)
			context['topics'] = accounts
    
	

	return render(request, "blog/topic_search_result.html", context)



def about(request):
    return render(request, 'blog/about.html', {'title': "About"})



