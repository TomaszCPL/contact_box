from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

class LandingView(View):
	def get(self,request):
		print("GET LandingView")
		return render(request, "landing.html")


	def post(self,request):
		return HttpResponse("Post request has come")
