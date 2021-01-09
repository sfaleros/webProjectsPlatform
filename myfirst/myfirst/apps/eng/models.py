import datetime
from django.db import models
from django.utils import timezone
import time

class Test(models.Model):
	test_tag1 =models.CharField('клас' , max_length = 20 ,default='10B')
	test_title= models.CharField('назва', max_length =150)
	test_time =models.CharField('час' , max_length = 2 ,default='10')

	test_eng= models.TextField("переклад", max_length = 20000, default='',blank=True)
	test_ukr= models.TextField("українські слова", max_length = 20000, default='',blank=True)


	def __str__(self) :
		return self.test_title

	#def was_published_recently(self):
	#	return self.pub_date >= (timezone.now() - datetime.timedelta(day = 7))

	class Meta :
		verbose_name = "тест"
		verbose_name_plural = "тести"


'''class Comment(models.Model) :
	article = models.ForeignKey(Article , on_delete =  models.CASCADE)
	author_name = models.CharField('імя автора' , max_length = 50)
	comment_text = models.CharField('текст комента' , max_length = 200)

	def __str__(self) :
		return self.author_name

	class Meta : 
		verbose_name = "коментар"
		verbose_name_plural = "коментарі"
'''
