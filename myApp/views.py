from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from .models import AccessRecord,Webpage,Topic
# Create your views here.
#def myApp(request):
 #   template=loader.get_template('myFirst.html')
  #  return HttpResponse(template.render())
   # return HttpResponse("Hello world")

def myApp(request):
    acc_rec = AccessRecord.objects.all()
     #template = loader.get_template('display_database.html')
    context = {
        'acc_rec':acc_rec,
    }
    #return HttpResponse(template.render(context, request))
    return render (request,'display_database.html',context)