from django import forms

class regist_form(forms.Form):
    category_name=forms.CharField(
        label="カテゴリー名",
        required=True,
        initial='',
        disabled=False,
        )
    heading_name=forms.CharField(
        label="カテゴリー名",
        required=True,
        initial='',
        disabled=False,
        )
    
    image_file=forms.ImageField(
        required=True,
        initial='',
        disabled=False,
        )
    
    
    comment=forms.CharField(
        label="コメント",
        required=False,
        initial='',
        widget = forms.Textarea(attrs={'rows':4, 'cols':15})
    )
 
 
    # comment = forms.CharField(widget=forms.Textarea) 
