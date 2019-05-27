from django import forms



class comment(forms.Form):
    name=forms.CharField(required=True,widget=forms.TextInput(attrs={'id':'id_name'}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'id':'id_email'}))
    url=forms.URLField(widget=forms.URLInput(attrs={'id':'id_url'}))
    comment=forms.CharField(required=True,widget=forms.Textarea(attrs={'id':'id_comment'}))