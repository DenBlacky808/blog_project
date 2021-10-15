from django import forms
from blogapp.models import Post


class PostForm(forms.ModelForm):
    # user_id = forms.IntegerField(widget=forms.HiddenInput(), initial=self.)

    class Meta:
        model = Post
        fields = ['title', 'user_post', 'user_id']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''