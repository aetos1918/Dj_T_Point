from django.shortcuts import render
from django.http import HttpResponse
from .models import DreamReal

# Create your views here.

# Sending Parameters to Views
def viewArticle(request, articleID):
	text = "Displaying the article: %s"%articleID
	return HttpResponse(text)

def viewArticles(request, month, year):
	text = "Displaying the article: {}-{}".format(month, year)
	return HttpResponse(text)

def disdate(request):
	from datetime import date
	day = date.today()
	return render(request, "myapp/hello.html", {'today': day})

def crudops(request):
	# creating an Entry

	dreamreal = DreamReal(
		website = "www.n1tr0g3n.com", mail = "HackerOnline@net.com",
		name = "Aetos", phonenumber = "1918179940"
		)
	dreamreal.save()

	# Real all Entries
	objects = DreamReal.objects.all()
	res ='Printing all DreamReal entries in the DB : <br>'

	for elt in objects:
		res += elt.name + '<br>'

	# Read specific entry

	sorex = DreamReal.objects.get(name = 'aetos')
	res += 'Printing One entry <br>'
   	res += sorex.name

   	# Delete an entry
   	res += '<br> Deleting an entry <br>'
   	sorex.delete()

   	# Update
   	dreamreal = DreamReal(
      		website = "www.polo.com", mail = "sorex@polo.com", 
      		name = "sorex", phonenumber = "002376970"
   		)
   
   	dreamreal.save()
   	res += 'Updating entry<br>'

   	dreamreal = DreamReal.objects.get(name = 'sorex')
   	dreamreal.name = 'thierry'
   	dreamreal.save()

   	return HttpResponse(res)
