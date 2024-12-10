from django import forms

class QRCodeForm(forms.Form):
   restaurant_name= forms.CharField(max_length=50, label='Restuarant NAme',
                                    widget=forms.TextInput(attrs={
                                       'class':'form-control',
                                       'placeholder':'Enter Restuarant name'
                                    })
                                    )
   url = forms.CharField(max_length=200, label='Menu URL',
                         widget=forms.URLInput(attrs={
                            'class':'form-control',
                            'placeholder':'Enter the url of your online menu'
                         }))  