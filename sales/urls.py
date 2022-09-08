from django.urls import path
from . import views
urlpatterns=[
    path('salesinfo/',views.sales_info,name="sinfo"),
    path('json/',views.sales_json,name="sales_json"),
    path('new/',views.display,name="new_record")
]