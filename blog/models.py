from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from PIL import Image
from django import forms




def find_topic(name):
    search_name = str(name).split(" ")

    topics = {"Space": ['spacex', 'star' "planets", "mars", "saturn", "Earth", "rocket", "nasa", "Star"]}
    Tesla = ['Tesla', "tesla", "ModelS", 'ModelX', 'Solar City', "model 3"]

    for name in search_name:
        if name in Tesla:
            return "Tesla"
    return "Undefined Topic "



class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='static/post_images')
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name='liked')
    topic = models.CharField(default=find_topic(title), max_length=50)
    type = models.CharField(default='image_post', max_length=20)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    
    @property
    def num_likes(self):
        self.liked.all().count()
        

    
    '''
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        pic = detect_face(self.image.path, self.image.path)

        for i in range(2):
            cv2.imwrite(f"{self.id}.jpg", pic)
        #print(face_detected)
        
        img.save(self.image.path)
    '''



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    content = models.TextField(max_length=300)

    def __str__(self):
        return str(self.pk)


    

LIKE_CHOICES = [
    ('like', 'like'),
    ('unlike', 'unlike')
]


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)


    def __str__(self):
        return f'{self.post.title}'


class Topic(models.Model):
    name = models.CharField(max_length=50)
    related_posts = models.QuerySet(Post.objects.filter(topic=name))
    image = models.ImageField(upload_to='static/topic_images', null=True)
    followers = models.QuerySet()


    def __str__(self):
        return f"{self.name} Topic"

