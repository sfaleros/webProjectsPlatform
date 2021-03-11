from django.http import Http404 , request
from django.shortcuts import render , redirect
#from django.urls import reverse
from .models import Test #, Obj
import json
import datetime
import math
import hashlib 



def index(request):

	test = Test.objects.order_by("-id")

	#num = '123456789'
	mainTests = []
	#chemestry_stuck_list = []
	#latest_articles_list = Article.objects.order_by("-id") #-pubdate

	for i in test :
		if i.test_tag1 in "10b 10б 10-b 10 b 10B 10-б 10 б" :
			mainTests.append(i)





	#a = Article.objects.all()
	#for i in a :
	#print(chemestry_list)
	return render(request , 'eng/tests.html' , {"mainTests" : mainTests}) #'latest_articles_list' : latest_articles_list ,

def detail(request , test_id ):
    	
	try :
		test = Test.objects.get(id = test_id)
	except :
		raise Http404("тест не знайдена")
    	


	if request.method=='POST':
		name = request.POST['sendName']
		ball = request.POST['ball']
		ballHash = request.POST['md']
		now = datetime.datetime.now()
		d = now.day
		h = now.hour
		m = now.minute

		timeBall = str(math.sqrt((d*h+1+m)/(float(ball)+1)))
		hashSert = hashlib.md5(timeBall.encode('utf-8')).hexdigest()

		print(hashSert)
		print(ballHash)

		if hashSert!=ballHash:
			raise Http404("нажаль ваш результат не збережено, через критичну помилку. будь ласка повідомте про неї розробнику \n" + str(d) +"."+ str(h) +":" + str(m) +"      " + ball + "\n \n          " + ballHash + "\n   !=     " + hashSert )
		
		print("ffffffff")
		test.mark_set.create(name = str(name) , ball = float(ball))
		return redirect('/tests/')



	#engStr = (((test.test_eng.replace(" ", "")).replace("\n", "")).replace("&", " ")).lower()
	#ukrStr = (((test.test_ukr.replace(" ", "")).replace("\n", "")).replace("&", " ")).lower()

	def delSpace(list, isEng):
		newlist = []
		for i in list :
			i = i.strip()
			if i != '' :
				if i.count(" ") > 1 and isEng :
					i  =  i.replace(" ", "", (i.count(" ")-1))
				newlist.append(i)
			
		return  newlist
    		
    		
	engWords = delSpace(test.test_eng.replace("\n", " ").lower().split(","), True)
	ukrWords = delSpace(test.test_ukr.replace("\n", " ").lower().split(","), False)

	
	#print(ukrWords)
	#print(engWords)

	if len(engWords) != len(ukrWords) :
		ukrWords=["помилка заповнення"]

	'''
		for i in engStr :	

		if i not in '.,;)':
			word+=i
		else :
			engWords.append(word)
			word = ''


		for i in ukrStr :	

		if i not in '.,;)':
			word+=i
		else :
			ukrWords.append(word)
			word = ''

	dict = {}
	cnt = 0
	#if ukrWords.count == engWords.count:
	for i in ukrWords :
		dict[i]=engWords[cnt]
		cnt +=1

	print(str(dict))
	print(str(ukrWords)+ str(engWords) + "fffffffffffffffffffffffffffffffffffffffffffffffffffffff")

	 { "dict" : json.dumps(dict)}
	 {"ukrWords" : json.dumps(ukrWords) , "engWords" : json.dumps(engWords) }
	 
	'''


	return render(request ,'eng/test.html' , {"ukrWords" : json.dumps(ukrWords) , "engWords" : json.dumps(engWords)  , "time" : test.test_time, "test" : test}  )












'''
"ukrWords" : ukrWords "engWords" : engWords 

def groupdetail(request , obj_id ):

	try :
		obj = Obj.objects.get(id = obj_id)
	except :
		raise Http404("стаття не знайдена")

	a = Article.objects.order_by('-id')
	topic_list = []


	for i in a :
		if i.article_tag1 == obj.obj_lesson  and i.article_tag2 == obj.obj_topic :

			titl_id = [i.id , i.article_title , i.article_text]
			topic_list.append(titl_id)

	return render(request , 'articles/groupdetail.html' , {'topic_list' : topic_list })



  // modelform.instance.field} //'''

