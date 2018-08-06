from django.db import models
from django.utils import timezone

class Post(models.Model): 
	author = models.ForeignKey('auth.USER', on_delete = models.CASCADE)
	title = models.CharField(max_length=200) #Başlık için maksimum karakter girişi 200.
	text = models.TextField()
	created_day = models.DateTimeField(default=timezone.now) #Oluşturma tarihi için server'ın açılış saatiyle kabul görür.
	published_date = models.DateTimeField(blank=True, null=True) #Yayımlanma tarihi için yazı veya boşluk bırakılması hata vermez.
	
	def publish(self):
		self.published_day = timezone.now()
		self.save()

	def __str__ (self):
		return self.title
