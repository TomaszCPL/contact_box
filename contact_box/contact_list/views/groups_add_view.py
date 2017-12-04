from django.shortcuts import render
from django.views import View
from contact_list.models import Contact, Group
from django.http.response import HttpResponseRedirect


class GroupsAddView(View):
	def get(self,request):
		return render(request, "contact/groups_add.html")

	def post(self,request):
		#validate input from form
		group = Group()
		group.name = request.POST.get("name")
		group.save()
		return HttpResponseRedirect("/groups/list")