from django.db import models

# Create your models here.
class stu(models.Model):
    s_userid = models.CharField(max_length=50, default="")
    s_age = models.CharField(max_length=20, default="")
    image= models.ImageField(upload_to="stu/images",default="")

    def __str__(self):
        return self.s_userid