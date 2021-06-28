from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    img = models.ImageField(upload_to = "blog/", blank=True, null=True) 
    #upload_to는 업로드할 폴더를 설정하는 것. settign.py에 MEDIA_URL로 지정해둔 media 폴더 안에 blog 폴더를 만들어서 관리하겠다는 설정.

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
