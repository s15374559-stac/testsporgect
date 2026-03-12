from django.shortcuts import render
from .models import Book, Student
from .form import studentform
from django.views.generic import ListView



# Create your views here.
def get_ollbox(request):
    books = Book.objects.all()
    data = {"books": books}
    return render (request, "index.html", data)


def filter_book(request):
    allbook=Book.objects.filter(pubish_year=2003)

    # book = Book.objects.get(id=2)
    
    
    data = {"books":allbook}
    return render (request, "index.html", data)




def createdate(request):
    book = Book.objects.create(title="sa3ed" , author= "EL_magholy" ,pubish_year="2009")
    data = {"books": [book]}
    return render (request, "index.html", data)





def update_date(request):
    book=Book.objects.get(id=1)
    book.title="clean - Update"
    book.save ()
    data= {'books': book}
    return render (request, "index.html" , data)

def delete_date(request):
    book = Book.objects.filter(id=6)
    book.delete()
    data={"sa3ed":book }
    return render (request, "index.html" , data)










def create_student(request):
    form = studentform(request.POST or None)
    if form .is_valid():
        form.save()
    return render (request , "index.html", {"form":form})
    



class stydentlistview(ListView):
    model = Student        
    template_name = "index.html"



    