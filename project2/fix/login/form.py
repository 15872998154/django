from django import forms
class UserForm(forms.Form):
    username = forms.CharField(label="用户名",\
                               max_length=16,
                               required = True,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"学号",
                                  
                                    }),
                               )
    password = forms.CharField(label="密码",
                                widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"密码",
                                  
                                    }),
                                required = True,
                                )