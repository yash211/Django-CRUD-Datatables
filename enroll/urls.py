from django.urls import path
from . import views
urlpatterns=[
    path('sadd/',views.add_student,name="add"),
    path('delete/<int:id>',views.delete_info,name="delete_data"),
    path('<int:id>',views.update_info,name="update_data")
]