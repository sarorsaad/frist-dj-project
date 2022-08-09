from django.http import HttpResponse
from django.shortcuts import render


#  views for httprespone.

# def index(request):
#          return HttpResponse ( ' welcome mlaz '  )
# def about(request):
#          return HttpResponse ( ' welcome saror '  )



#  views for render templates.

def index (request):
     x  =  {'name':'sarorsaad' , 
            'age':40 ,
            'file':18000000000 
            }
     return render (request,'pages/index.html',x)
        
def about (request):
     return render (request,'pages/about.html ')