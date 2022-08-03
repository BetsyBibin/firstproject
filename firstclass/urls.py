from . import views
from django.urls import path

urlpatterns = [
    ##path('',views.load_add_page,name='load_add_page'),
    ##path('add_num',views.add_num,name='add_num'),
    ##path('',views.index,name='index'),
   

   path('',views.cal,name='cal'),
   path('calc',views.calc,name='calc'),
]