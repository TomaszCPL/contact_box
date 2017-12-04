from django.shortcuts import render
from django.views import View
from contact_list.models import Group,Contact

class GroupsSearchView(View):
	def get(self,request):
		#print("GET LandingView")
		return render(request, "contact/groups_search.html")

	def post(self, request):
		contact_name = request.POST.get("member")
		contacts = Contact.objects.filter(name= contact_name) | \
			Contact.objects.filter(surname= contact_name)
		groups = None
		if contacts:
			groups = contacts[0].groups.all()
		context = {"groups" : groups}
		return render(request, "contact/groups_search.html",context)