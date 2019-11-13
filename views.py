from django.shortcuts import render
import os
import json
from datetime import datetime
from django.views import generic, View
from .models import SurgInfo

# root = '/Users/Melody/Documents/expdata/SURG'
# Create your views here.

class index(generic.ListView):
    template_name = 'surgery/index.html'   # if use ListView class, default template_name is _list.html. So you have to revise it.
    queryset = SurgInfo.objects.filter(terminated = False)   # default output variable. In template, use object_list to refer to this.
    # the default output to tmplate is object_list
    def get_context_data(self, **kwargs):
        # queryset is the default output, besides that, you can use get_context_data to add more in the dict.
        context = super(index, self).get_context_data(**kwargs)
        return context
"""
def aav_inject(request):
    template = 'surgery/animalInfo.html'
    # form = RegisterForm()
    if request.method == "POST":
        context = copy_query_context(request.POST) #if no files
        animalid = context['animalid']
        context['inject_dose'] = ''.join([str(context['inject_dose']), 'ul'])
        [y,m,d] = context['date'].split('-')
        context['date'] = '-'.join([str(int(m)),str(int(d)),y])
        context['step'] = 'virus inject'
        update_info(animalid, context)

    return render(request, template, context)

def copy_query_context(context):
    new_context = {}
    keys = context.keys()
    keys = [x for x in keys if x not in ['csrfmiddlewaretoken']]
    for key in keys:
        new_context[key] = context[key]
    return(new_context)

def update_info(animalid, context):
    path = os.path.join(root, animalid+'.json')
    try:
        with open(path, "r") as read_file:
            info = json.load(read_file)
    except:
        info = {}
        info['id'] = animalid

    if 'treatment' not in info:
        info['treatment'] = []
    
    keys = context.keys()
    keys = [x for x in keys if x not in ['animalid', 'csrfmiddlewaretoken']]
    newtreat = {}
    for key in keys:
        newtreat[key] = context[key]
    
    info['treatment'].append(newtreat)

    with open(path, 'w') as f:
        json.dump(info, f, indent=4)"""