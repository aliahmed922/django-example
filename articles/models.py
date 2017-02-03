from django.db import models

# Create your models here.
class Article(models.Model):
   title = models.CharField(max_length=50)
   description = models.TextField()
   # author = models.ForeignKey('Author', on_delete=models.CASCADE)
   pub_date = models.DateTimeField('date published')

   def __unicode__(self):
       return self.name
