from django.shortcuts import render,redirect
from .models import Name
import random


# Create your views here.

def modify(request,num):

	if request.method=='GET':
		return render(request,'data.html')

	elif request.method=='POST':
		Nams = Name.objects.get(id=num)
		Nams.name=request.POST['topic']
		Nams.asdf=request.POST['asdf']
		Nams.save()
		return  redirect('/')
	else:
		return render(request,'data.html')



		

	

def delete(request,num):
	Nams=Name.objects.all()
	k=Nams[0].id-1
	Name.objects.filter(id=num+k).delete()
	return redirect('/')

def about(request):
	return render(request,'about.html')
def test(request):
	Nams=Name.objects.all()
	if len(Nams) is not 0:
		print(Nams[0].id)
		k=Nams[0].id-1
		for nam in Nams:
			nam.id=nam.id-k
	
	
	return render(request,'index.html',{'nams':Nams})



def data(request):
	Nams=Name.objects.all()
	if request.method=='POST':
		name=request.POST['topic']
		asdf=request.POST['asdf']
		r = Name(name=name,asdf=asdf)
		r.save()
		print(Nams)
		return  redirect('/')

	else:
		return render(request,'data.html')

