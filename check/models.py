from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Name(models.Model):
	
	name=models.CharField(max_length=50,blank=False)
	asdf=models.TextField(blank=False)
	test=models.DateField(default=timezone.now(),blank=False)
	
	def __str__(self):
		return  (self.name)
