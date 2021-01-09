from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
	path('' , views.menu, name= 'menu'),
	path('chem1/' , views.chem, name= 'chem'),
	path('articles/' , views.index, name= 'index'),
	path('<int:article_id>/' , views.detail, name= "detail"),
	path('topic/<int:obj_id>/' , views.groupdetail, name= "groupdetail"),

    #path('<int:article_id>/count/', views.count, name='count')

]