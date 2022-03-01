from django import forms
from nursery_ecommerce_app.models.category import Category
class CategoryForm(forms.ModelForm):
    class Meta:
        #cat_image = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
        model=  Category
        #fields = '__all__'
        fields=('category_name','slug','description','cat_image',)
        def __init__(self, *args, **kwargs):
            super(CategoryForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] ="form-control"
        
