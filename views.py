from django.shortcuts import render
from django.views import generic, View
from .models import SurgTreatment, TransgenicAnimalLog #SurgInfo, 
from .forms import SurgInfoForm
import django.urls as urls
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required


class index(generic.ListView):
    template_name = 'surgery/index.html'   # if use ListView class, default template_name is _list.html. So you have to revise it.
    model= TransgenicAnimalLog
    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['animals'] = TransgenicAnimalLog.objects.filter(~Q(cageid = 'terminated')).annotate(tnum = Count('surgtreatment')).filter(tnum__gt=0)
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
        
        animal = TransgenicAnimalLog.objects.filter(animalid = animalid)[0]
        
        treatments = animal.surgtreatment_set.all()
        context = {'animal': animal, 'treatments': treatments}
        return render(request, self.template_name, context)

"""class Addanimal(generic.CreateView):
    form_class = SurgInfoForm
    model = SurgInfo
    template_name = 'surgery/addanimal.html'

    def get_success_url(self):
        return urls.reverse('surgindex')
        #{% url 'app_name:app_url' %}"""


@login_required
def terminate(request, animalid):
    TransgenicAnimalLog.objects.filter(animalid = animalid).update(cageid='terminated')
    return HttpResponseRedirect(reverse('surgindex')) # reverse by this url name.
