#coding=utf8
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label = '主题', min_length = 3, max_length = 100)
    email = forms.EmailField(label = '电子邮箱(可选)', required = False)
    message = forms.CharField(label = '正文', widget = forms.Textarea)
    
    
    """
    Django的form系统自动寻找匹配的函数方法，该方法名称以clean_开头，并以字段名称结束。
    如果有这样的方法，它将在校验时被调用。
    """
    # 主题验证及处理
    def clean_subject(self):
        subject = self.cleaned_data['subject'].strip()
        if not len(subject):
            raise forms.ValidationError("这个字段是必填项。")
        """
        在函数的末尾显式地返回字段的值非常重要。 我们可以在我们自定义的校验方法中修改它的值（或者把它转换成另一种Python类型）。
        如果我们忘记了这一步，None值就会返回，原始的数据就丢失掉了。
        """
        return subject
    
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        return email
    
    # 正文验证及处理
    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        num_words = len(message.split())
        if num_words < 1:
            raise forms.ValidationError("没有足够的内容!")
        return message