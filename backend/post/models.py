from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name = "posts",null=True,unique = False)
    question = models.CharField(max_length=400, null=False)
    description = models.CharField(max_length=1000, null=True)
    createdAt = models.DateTimeField(null = True)
    modifiedAt = models.DateTimeField(null = True)

    def save(self,*args,**kwargs):

        if not self.id :
            self.createdAt = datetime.now()
            self.modifiedAt = datetime.now()

        else:
            self.modifiedAt = datetime.now()
            
        super(posts,self).save(*args,**kwargs)


    class Meta:
        verbose_name_plural = "posts"


    def __str__(self):
        return str(self.question)
