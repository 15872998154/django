from django import forms

class BookForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=20)
    user_tel = forms.CharField(label='联系电话', max_length=15)
    user_addr = forms.CharField(label='联系住址', max_length=50)
    car_brand = forms.CharField(label='品牌', max_length=30)
    car_broken_part = forms.CharField(label='损坏描述', max_length=50)

class FixListForm(forms.Form):
	main_broken_part = forms.CharField(label='主要损坏部位', max_length=40)
	# fix_man 

