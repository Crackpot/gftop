# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.contrib.auth.models import User
from ddtcms.news.models import News,Category
# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = { 'class': 'required' }

from attachments.forms import DynamicMultipleFileField
from ddtcms.forum.forms import NicEditor

class NewsForm(forms.ModelForm):
    category  = forms.ChoiceField(label=_(u"Category"),help_text="News Items Canot addto Top level Category")
    deliverer = forms.ModelChoiceField(label=_(u"Deliverer"),queryset=User.objects.all())   
    content   = forms.CharField(label=_(u"Content"), widget=NicEditor(attrs={'rows':15, 'cols':66}),required=True)   
    file      = forms.FileField(label=_("Files"),widget=DynamicMultipleFileField(), required=False)	

    class Meta:
        model = News
        #exclude = ('status', 'editor', 'attached_by', 'allow_comments','views','comments','pic')
        exclude = ('editor','views','comments')


    def __init__(self, data=None, initial=None, instance=None):
        super(NewsForm, self).__init__(data=data, initial=initial, instance=instance)
        if initial is None:
            initial = {}
        if data is None:
            data = {}
        #initial.update(self.category_choices())
        self.fields["category"].choices = self.category_choices()
        

    def category_choices(self):
        my_choices = [] 
        for root in Category.objects.get_all_roots():
            rc=root.name,tuple(root.get_children().values_list('id','name'))
            my_choices.append(rc)
        return my_choices
        
    def clean_title(self):
        # do something that validates your data
        return self.cleaned_data["title"]
    
    def clean_category(self):
        # do something that validates your data
        category_id = self.cleaned_data.get("category")

        #if Category.objects.filter(name__iexact=category).count() == 0:
        category = Category.objects.get(id__iexact=int(category_id))
        cc=category.child.count()
        if cc == 0:
            return category
        else:
            raise forms.ValidationError(_("The category has child(ren),you must select one of its child!"))
        return category