from django.http import Http404 , request
from django.shortcuts import render
#from django.urls import reverse
from .models import Article , Obj
from math import sqrt



def menu(request):
	return render(request , 'menu/menu.html' ) #'latest_articles_list' : latest_articles_list ,



def chem(request):
	return render(request , 'menu/chem1.html' ) #'latest_articles_list' : latest_articles_list ,


def index(request):

	obj = Obj.objects.order_by("-id")

	#num = '123456789'
	chemestry_list = []
	phis_list = []
	alg_list = []
	geo_list = []
	#chemestry_stuck_list = []
	#latest_articles_list = Article.objects.order_by("-id") #-pubdate

	for i in obj :
		if i.obj_lesson == 'фізика' :
			phis_list.append(i)


		if i.obj_lesson == 'хімія' :
			chemestry_list.append(i)


		if i.obj_lesson == 'алгебра' :
			alg_list.append(i)


		if i.obj_lesson == 'геометрія' :
			geo_list.append(i)





	#a = Article.objects.all()
	#for i in a :
	#print(chemestry_list)
	return render(request , 'articles/list.html' , {'chemestry_list' : chemestry_list  , 'phis_list' : phis_list , 'alg_list' : alg_list , 'geo_list' : geo_list}) #'latest_articles_list' : latest_articles_list ,

def detail(request , article_id ):

	try :
		article = Article.objects.get(id = article_id)
	except :
		raise Http404("стаття не знайдена")

	try :
		varlist = request.POST['sim1']
	except :

		simvols ='[()=+-**/^.,];1 2 34567890'
		longvar =''

		art =  article.article_text

		list(filter(None, art))

		art += ';'
		artvarSp = []
		for l in art :
			if l not in simvols and type(l) != int and l != '2' :
				longvar += l

			if l in simvols :
				if longvar != '':
					artvarSp.append(longvar)
					longvar = ''

		lenvar = len(artvarSp)
		#print(artvarSp)


		return render(request , 'articles/detail.html' , {"var": artvarSp , 'lenvar':lenvar , 'article' : article})
#------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------------

	allert = 'введіть всі елементи крім одного'
	artvarSp = []
	simvols ='[]()=+-*/^.,;1234567890'
	art =  article.article_text
	longvar =''
	art += ';' 										#костиль  a l i print
	for Lind in art :
		if Lind == ' ' :
			continue
		if Lind not in simvols :
			longvar += Lind

		if Lind in simvols :
			if longvar != '':
				artvarSp.append(longvar)
				longvar = ''


	lenvar = len(artvarSp)

	#print("fffffffffffff   lenvar" + str(lenvar) +'artvarSp'+str(artvarSp) )

	def save() :
		exec(str(artvarSp[0]) +'='+ str(varlist[0]) ,globals())
		exec(str(artvarSp[1]) +'='+ str(varlist[1]) ,globals())
		exec(str(artvarSp[2]) +'='+ str(varlist[2]) ,globals())
		if lenvar > 3 :
			exec(str(artvarSp[3]) +'='+ str(varlist[3]) ,globals())
			if lenvar > 4 :
				exec(str(artvarSp[4]) +'='+ str(varlist[4]) ,globals())
				if lenvar > 5 :
					exec(str(artvarSp[5]) +'='+ str(varlist[5]) ,globals())



	varlist = [request.POST['sim1'] , request.POST['sim2'] ,request.POST['sim3']]
	formula1 = article.article_f1
	formula2 = article.article_f2
	formula3 = article.article_f3
	if lenvar > 3 :
		varlist.append(request.POST['sim4'])
		formula4 = article.article_f4
		if lenvar > 4 :
			varlist.append(request.POST['sim5'])
			formula5 = article.article_f5
			if lenvar > 5 :
				varlist.append(request.POST['sim6'])
				formula6 = article.article_f6







	varlist1 = []
	for IRST in varlist :
		for ASTR in IRST :
			if ASTR not in '1234567890*()+-**^√//.() ,' :
				return render(request , 'articles/detail.html' , {"var": artvarSp , 'lenvar':lenvar , 'article' : article , 'endvar' : varlist , 'allert' : ('наявний заборонений символ : ' + str(ASTR))})

		IRST = IRST.replace('^' , 'sqrt')
		IRST = IRST.replace('√', 'sqrt')
		IRST = IRST.replace(',', '.')
		IRST = IRST.replace(' ', '')
		print(IRST)
		varlist1.append(IRST)

	varlist = varlist1

	if varlist.count('') != 1 :
		#print("не один пошуковий елемент")
		return render(request , 'articles/detail.html' , {"var": artvarSp , 'lenvar':lenvar , 'article' : article , 'allert' : allert , 'endvar' : varlist})

	elif '' in varlist:
		varlist [(varlist.index(''))] = '"?"'
		try :
		    save()
		except :
		    return render(request , 'articles/detail.html' , {"var": artvarSp , 'lenvar':lenvar , 'article' : article , 'allert' : 'помилка вводу'})




	if varlist.count('"?"') == 1 :		#перестраховка (мож викинути)
		endvar_list = []
		endvar_list.extend(varlist)

		#print("varlist" + str(varlist) + 'artvarSp' +str(artvarSp) + 'lenvar'+ str(lenvar))
		#print(artvarSp)

		if varlist[0] == '"?"':
			exec(art , globals())
			#print(str(eval(artvarSp[0])))
			endvar_list[0] = str(eval(artvarSp[0]))

		elif varlist[1]== '"?"' :
			exec(formula1 , globals())
			#print(str(eval(artvarSp[1])))
			endvar_list[1] = str(eval(artvarSp[1]))

		elif varlist[2]== '"?"' :
			exec(formula2 , globals())
			#print(str(eval(artvarSp[2])))
			endvar_list[2] = str(eval(artvarSp[2]))

		elif varlist[3]== '"?"' :
			exec(formula3 , globals())
			#print(str(eval(artvarSp[3])))
			endvar_list[3] = str(eval(artvarSp[3]))

		elif varlist[4]== '"?"' :
			exec(formula4 , globals())
			#print(str(eval(artvarSp[4])))
			endvar_list[4] = str(eval(artvarSp[4]))#--------------------------------------(форнути та адаптивізувати)

		elif varlist[5]== '"?"' :
			exec(formula5 , globals())
			#print(str(eval(artvarSp[5])))
			endvar_list[5] = str(eval(artvarSp[5]))

		elif varlist[6]== '"?"' :
			exec(formula6 , globals())
			#print(str(eval(artvarSp[6])))
			endvar_list[6] = str(eval(artvarSp[6]))



			#save()
			#print(str(sp))
			#exec(sp , globals())
			#print("varlist" + str(varlist) + 'artvarSp' +str(artvarSp) + 'lenvar'+ str(lenvar))
			#print('result' + str(eval(artvarSp[1])))
	#else  :
	#print(formula3)
	endvar_list1 = []
	for SSE in endvar_list :
		#if (int(SSE)).is_integer():
		#	SSE = str(int(SSE))
		SSE = SSE.replace('sqrt' , '√')
		endvar_list1.append(SSE)
	endvar_list = endvar_list1

	return render(request , 'articles/detail.html' , {"var": artvarSp , 'lenvar':lenvar , 'article' : article , 'endvar' : endvar_list})



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



