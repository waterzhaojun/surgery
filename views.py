from django.shortcuts import render
import os
import json
from datetime import datetime

root = '/Users/Melody/Documents/expdata/SURG'
# Create your views here.
def index(request):
    #animals = TransgenicAnimalLog.objects.all()
    template = 'surgery/index.html' # loader.get_template('transgmice/index.html') 用了shortcut就不需要用loader了
    return render(request, template)#, context)

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
        json.dump(info, f, indent=4)