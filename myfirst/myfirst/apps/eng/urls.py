from django.urls import path
from . import views

app_name = 'eng'

urlpatterns = [
	path('' , views.index, name= 'index'),
	path('<int:test_id>/' , views.detail, name= "detail")

    #path('<int:article_id>/count/', views.count, name='count')

]