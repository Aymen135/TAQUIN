from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('AI',views.get_result_from_AI,name='getai'),
    path('ai',views.resolve,name='postai'),
]