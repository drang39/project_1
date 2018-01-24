from django import forms

class CommetForm(forms.Form):
    
    rating = forms.IntegerField(label='rating')
    comment = forms.CharField(label='comment',max_length=500)
    # food = forms.CharField(label='food',max_length=100)
    
    