import datetime
from django.db import models
from django.utils import timezone
import time

class Article(models.Model):
	article_tag1 =models.CharField('предмет' , max_length = 20 ,default='')
	article_tag2 =models.CharField('група' , max_length = 20, default='')
	article_title= models.CharField('назва статті', max_length =150)
	article_text= models.CharField(" головна формула", max_length = 100)

	article_var1= models.CharField("елемент1опис", max_length = 200, default='₀₁₂₃₄₅₆₇₈₉ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨαβγδζηθικλμνξοπρστυφχψω',blank=True)
	article_var2= models.CharField("елемент2опис", max_length = 200, default='',blank=True)
	article_var3= models.CharField("елемент3опис", max_length = 200, default='',blank=True)
	article_var4= models.CharField("елемент4опис", max_length = 200, default='',blank=True)
	article_var5= models.CharField("елемент5опис", max_length = 200, default='',blank=True)
	article_var6= models.CharField("елемент6опис", max_length = 200, default='',blank=True)
	article_var7= models.CharField("елемент7опис", max_length = 200, default='',blank=True)

	article_f1= models.CharField("формула1", max_length = 100, default='',blank=True)
	article_f2= models.CharField("формула2", max_length = 100, default='',blank=True)
	article_f3= models.CharField("формула3", max_length = 100, default='',blank=True)
	article_f4= models.CharField("формула4", max_length = 100, default='',blank=True)
	article_f5= models.CharField("формула5", max_length = 100, default='',blank=True)
	article_f6= models.CharField("формула6", max_length = 100, default='',blank=True)



	def __str__(self) :
		return self.article_title

	#def was_published_recently(self):
	#	return self.pub_date >= (timezone.now() - datetime.timedelta(day = 7))

	class Meta :
		verbose_name = "стаття"
		verbose_name_plural = "статті"


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

class Obj(models.Model) :
	obj_lesson = models.CharField("предмет", max_length = 30, default='',blank=True)
	obj_topic= models.CharField("тема", max_length = 30, default='',blank=True)


	def __str__(self) :
		return self.obj_lesson

	class Meta :
		verbose_name = "тема"
		verbose_name_plural = "теми"







'''	article_2text= models.CharField("головна формула2", max_length = 100 , blank=True )
	article_2var1= models.CharField("елемент1опис", max_length = 200, default='',blank=True)
	article_2var2= models.CharField("елемент2опис", max_length = 200, default='',blank=True)
	article_2var3= models.CharField("елемент3опис", max_length = 200, default='',blank=True)
	article_2var4= models.CharField("елемент4опис", max_length = 200, default='',blank=True)
	article_2var5= models.CharField("елемент5опис", max_length = 200, default='',blank=True)
	article_2var6= models.CharField("елемент6опис", max_length = 200, default='',blank=True)
	article_2var7= models.CharField("елемент7опис", max_length = 200, default='',blank=True)

	article_2f1= models.CharField("формула1", max_length = 100, default='',blank=True)
	article_2f2= models.CharField("формула2", max_length = 100, default='',blank=True)
	article_2f3= models.CharField("формула3", max_length = 100, default='',blank=True)
	article_2f4= models.CharField("формула4", max_length = 100, default='',blank=True)
	article_2f5= models.CharField("формула5", max_length = 100, default='',blank=True)
	article_2f6= models.CharField("формула6", max_length = 100, default='',blank=True)



	article_3text= models.CharField("головна формула3", max_length = 100 , blank=True )
	article_3var1= models.CharField("елемент1опис", max_length = 200, default='',blank=True)
	article_3var2= models.CharField("елемент2опис", max_length = 200, default='',blank=True)
	article_3var3= models.CharField("елемент3опис", max_length = 200, default='',blank=True)
	article_3var4= models.CharField("елемент4опис", max_length = 200, default='',blank=True)
	article_3var5= models.CharField("елемент5опис", max_length = 200, default='',blank=True)
	article_3var6= models.CharField("елемент6опис", max_length = 200, default='',blank=True)
	article_3var7= models.CharField("елемент7опис", max_length = 200, default='',blank=True)

	article_3f1= models.CharField("формула1", max_length = 100, default='',blank=True)
	article_3f2= models.CharField("формула2", max_length = 100, default='',blank=True)
	article_3f3= models.CharField("формула3", max_length = 100, default='',blank=True)
	article_3f4= models.CharField("формула4", max_length = 100, default='',blank=True)
	article_3f5= models.CharField("формула5", max_length = 100, default='',blank=True)
	article_3f6= models.CharField("формула6", max_length = 100, default='',blank=True)

	pub_date = models.DateTimeField("дата публікації" , defult= timezone.now())


















		obj_topic2= models.CharField("тема2", max_length = 30, default='',blank=True)
	obj_topic3= models.CharField("тема3", max_length = 30, default='',blank=True)
	obj_topic4= models.CharField("тема4", max_length = 30, default='',blank=True)
	obj_topic5= models.CharField("тема5", max_length = 30, default='',blank=True)
	obj_topic6= models.CharField("тема6", max_length = 30, default='',blank=True)
	obj_topic7= models.CharField("тема7", max_length = 30, default='',blank=True)
	obj_topic8= models.CharField("тема8", max_length = 30, default='',blank=True)
	obj_topic9= models.CharField("тема9", max_length = 30, default='',blank=True)'''


