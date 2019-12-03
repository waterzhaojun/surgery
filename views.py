from django.shortcuts import render
from django.views import generic, View
from .models import SurgInfo, SurgTreatment

# root = '/Users/Melody/Documents/expdata/SURG'
# Create your views here.

class index(generic.ListView):
    template_name = 'surgery/index.html'   # if use ListView class, default template_name is _list.html. So you have to revise it.
    queryset = sorted(SurgInfo.objects.select_related().filter(terminated = False), key = lambda t: t.animalid)   # default output variable. In template, use object_list to refer to this.
    # the default output to tmplate is object_list
    # def get_context_data(self, **kwargs):
        # queryset is the default output, besides that, you can use get_context_data to add more in the dict.
    #     context = super(index, self).get_context_data(**kwargs)
    #     context['animals'] = sorted(SurgInfo.objects.all(), key = lambda t: t.animalid)
    #     return context

class Info(View):
    template_name = 'surgery/info.html'
    def get(self, request, **kwargs):
        animal = SurgInfo.objects.filter(animalid = kwargs['pk'])[0]
        treatments = animal.surgtreatment_set.all()
        context = {'animal': animal, 'treatments': treatments}
        return render(request, self.template_name, context)
