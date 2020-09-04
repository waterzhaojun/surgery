from django import forms
from .models import SurgTreatment, TransgenicAnimalLog #SurgInfo, 
from django.db.models import Q

class SurgInfoForm(forms.ModelForm):
    class Meta:
        model=SurgTreatment#SurgInfo
        fields = ['animalid']#, 'transgenic_id', 'ear_punch', 'species', 'strain', 'note']

        """def clean_jsonfield(self):
            jdata = self.cleaned_data['genotype']
            try:
                json_data = json.loads(jdata) #loads string as json
                #validate json_data
            except:
                raise forms.ValidationError("Invalid data in jsonfield")
                #if json data not valid:
                #raise forms.ValidationError("Invalid data in jsonfield")
            return jdata"""

    def check_transgenic_info(self):
        tid = self.cleaned_data['transgenic_id']
        print(tid)
        info = TransgenicAnimalLog.objects.filter(animalid = tid)[0]
        self.cleaned_data['gender'] = info.gender
        self.cleaned_data['birthday'] = info.dob
        self.cleaned_data['terminated'] = False

    #def save(self):
    #    self.check_transgenic_info()
    #    print(self.cleaned_data)
        
    def save(self, commit=True):
        m = super(SurgInfoForm, self).save(commit=False)
        print(m)
        #m.check_transgenic_info()
        tid = m.transgenic_id
        print(tid)
        info = TransgenicAnimalLog.objects.filter(animalid = tid)[0]
        m.gender = info.gender
        m.birthday = info.dob
        m.terminated = False
        print(m)
        if commit:
            m.save()
        return m
