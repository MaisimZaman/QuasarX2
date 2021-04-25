from django.db import models
from detectionfeat.algorithms import detect_face
from django.conf import settings
import cv2 
from PIL import Image
# Create your models here.


class Detector(models.Model):
    title = models.CharField(max_length=100)

    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    image = models.ImageField(null=True, upload_to='detection')


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        pic = detect_face(self.image.path, self.image.path)

        for i in range(2):
            cv2.imwrite(f"{self.id}.jpg", pic)
        #print(face_detected)
        
        img.save(self.image.path)



