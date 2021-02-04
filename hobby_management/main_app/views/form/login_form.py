from django import forms

class login_form(forms.Form):
    username=forms.CharField(
        label="ユーザー名",
        max_length=254,
        required=True,
        initial='',
        disabled=False,
        )
    password=forms.CharField(
        label="パスワード",
        max_length=254,
        required=True,
        initial='',
        disabled=False,
    ) 

