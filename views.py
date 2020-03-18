from django.shortcuts import render
from django.views import generic, View
from .models import SurgInfo, SurgTreatment, TransgenicAnimalLog
from .forms import SurgInfoForm
import django.urls as urls
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

# root = '/Users/Melody/Documents/expdata/SURG'
# Create your views here.

class index(generic.ListView):
    template_name = 'surgery/index.html'   # if use ListView class, default template_name is _list.html. So you have to revise it.
    queryset = sorted(SurgInfo.objects.select_related().filter(terminated = False), key = lambda t: t.animalid)   # default output variable. In template, use object_list to refer to this.
    # the default output to tmplate is object_list
    # It is ok if I don't define get_context_data, but I think if I don't use it, it always don't change page after I update the database.
    # And, in the index template, you need to use animals instead of object_list
    def get_context_data(self, **kwargs):
        # queryset is the default output, besides that, you can use get_context_data to add more in the dict.
        context = super(index, self).get_context_data(**kwargs)
        context['animals'] = sorted(SurgInfo.objects.select_related().filter(terminated = False), key = lambda t: t.animalid)
        return context

class Info(View):
    template_name = 'surgery/info.html'

    def get(self, request, **kwargs):
        
        # there are two different url request:
        # info/DL122
        # or
        # info/?animal=DL122
        # The first one goes in kwargs
        # The second one goes in request.GET object.
        if 'animalid' in kwargs.keys():
            animalid = kwargs['animalid']
        else:
            animalid = dict(request.GET.lists())['animalid'][0]

        print(animalid)
        
        animal = SurgInfo.objects.filter(animalid = animalid)[0]
        
        treatments = animal.surgtreatment_set.all()
        context = {'animal': animal, 'treatments': treatments}
        return render(request, self.template_name, context)

class Addanimal(generic.CreateView):
    form_class = SurgInfoForm
    model = SurgInfo
    template_name = 'surgery/addanimal.html'

    def get_success_url(self):
        return urls.reverse('surgindex')
        #{% url 'app_name:app_url' %}

    
@login_required
def terminate(request, animalid):
    SurgInfo.objects.filter(animalid = animalid).update(terminated=True)
    return HttpResponseRedirect(reverse('surgindex')) # reverse by this url name.
