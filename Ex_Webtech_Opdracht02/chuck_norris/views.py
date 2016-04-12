from django.shortcuts import render
from django.views import generic
from .forms import NameForm
from .models import Quote

import redis

# Create your models here.
r = redis.StrictRedis(host='localhost', port=6379, db=0)

class IndexView(generic.ListView):
    template_name = 'chuck_norris/index.html'

    def get_queryset(self):
    	return "Hello I sok"


def get_first_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:
		form = NameForm()

	return render(request, 'name.html', {'form': form})