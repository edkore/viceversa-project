from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user1_text = request.GET['user_text']
	reversed_text = user1_text[::-1]
	return render(request, 'reverse.html', {'user_text':user1_text, 'reversedtext':reversed_text})

	