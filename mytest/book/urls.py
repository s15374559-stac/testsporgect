from django.urls import path
from . import views

urlpatterns = [
    path("get_ollbox/", views.get_ollbox),
    path("filter_book/", views.filter_book),
    path("createdate/", views.createdate),
    path("update_date/" , views.update_date),
    path("delete_date/" , views.delete_date),
    path("create_student/" , views.create_student),
    path("stydentlistview/" , views.stydentlistview.as_view())

]

