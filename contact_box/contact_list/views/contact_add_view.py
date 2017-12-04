from django.shortcuts import render
from django.views import View
from contact_list.models import Contact
from django.http.response import HttpResponseRedirect


class ContactAddView(View):
    def get(self, request):
        return render(request, "contact/contact_add.html")

    def post(self, request):
        # validate input from form
        contact = Contact()
        contact.name = request.POST.get("name")
        contact.surname = request.POST.get("surname")
        contact.description = request.POST.get("description")
        contact.save()

        return HttpResponseRedirect("/contact/show/" + str(contact.id))
