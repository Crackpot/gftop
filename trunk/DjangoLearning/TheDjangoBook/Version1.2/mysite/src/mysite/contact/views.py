#coding=utf8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from mysite.contact.forms import ContactForm
from mysite.settings import url_prefix

# 调用django自己的表单
def contact(request):
    if request.method == 'POST':
        # 已经提交表单
        form = ContactForm(request.POST) # request.POST是一个字典
        if form.is_valid(): # 表单有效
            cd = form.cleaned_data
            try:
                send_mail(
                    subject = cd['subject'], # 主题
                    message = 'Message:\n' + cd['message'], # 正文
                    from_email = cd.get('email', 'crackpot@localhost.site'), # 寄信人
                    recipient_list = ['crackpot@localhost.site'], # 收信人列表
                )
                return HttpResponseRedirect(url_prefix+'/contact/thanks/')
            except:
                print 'Can not send mail'
    else:
        # 未提交表单
        form  = ContactForm(
            initial = {
                       'subject': '测试主题',
                       'email': 'crackpot@localhost.site',
                       'message': '在此我通过对表单赋初值来实现此效果',
            }
        )
    return render_to_response(
        'contact/contact_form.html',
        {'form': form}
    )

def thanks(request):
    return render_to_response('contact/thanks.html')

# 原始的自己编写的表单
def contact_original(request):
    errors = []
    """
    确认request.method的值是’POST’。用户浏览表单时这个值并不存在，当且仅当表单被提交时这个值才出现。
    判断request.method的值很好地帮助我们将表单显示与表单处理隔离开来。
    """
    if request.method == 'POST':
        """
        这里，有两个必填项，subject 和 message，所以需要对这两个进行验证。
        注意，我们使用request.POST.get()方法，并提供一个空的字符串作为默认值；这个方法很好的解决了键丢失与空数据问题。
        """
        # request.POST是一个字典，从字典中获取值要用get方法
        if not request.POST.get('subject', '').strip(): # 去掉空格验证
            errors.append('Enter a subject.')
        if not request.POST.get('message', '').strip():
            errors.append('Enter a message.')

        """
        虽然email非必填项，但如果有提交她的值则我们也需进行验证。
        我们的验证算法相当的薄弱，仅验证值是否包含@字符。
        在实际应用中，需要更为健壮的验证机制（Django提供这些验证机制，稍候我们就会看到）。
        """
        if request.POST.get('email').strip() and '@' not in request.POST['email'].strip():
            errors.append('Enter a valid e-mail address.')

            """
            我们使用了django.core.mail.send_mail函数来发送e-mail。这个函数有四个必选参数： 主题，正文，寄信人和收件人列表。 send_mail是Django的EmailMessage类的一个方便的包装，EmailMessage类提供了更高级的方法，比如附件，多部分邮件，以及对于邮件头部的完整控制。

注意，若要使用send_mail()函数来发送邮件，那么服务器需要配置成能够对外发送邮件，并且在Django中设置出站服务器地址。 参见规范：http://docs.djangoproject.com/en/dev/topics/email/
            """
        if not errors:
            """
            未联机时填写邮件地址为外网地址时会出现异常，添加异常处理过程。
            """
            try:
                send_mail(
                    # 1 主题 2 正文 3 寄信人 4 收件人列表
                    subject=request.POST['subject'].strip(), # 主题
                    message='Message:\n' + request.POST['message'].strip(), # 正文
                    from_email=request.POST.get('email', 'crackpot@localhost.site').strip(), # 寄信人，未填时获取默认值
                    recipient_list=['crackpot@localhost.site'], # 收件人列表
                )
                """
                当邮件发送成功之后，我们使用HttpResponseRedirect对象将网页重定向至一个包含成功信息的页面。 包含成功信息的页面这里留给读者去编写（很简单一个视图/URL映射/一份模板即可），但是我们要解释一下为何重定向至新的页面，而不是在模板中直接调用render_to_response()来输出。
                原因就是： 若用户刷新一个包含POST表单的页面，那么请求将会重新发送造成重复。 这通常会造成非期望的结果，比如说重复的数据库记录；在我们的例子中，将导致发送两封同样的邮件。 如果用户在POST表单之后被重定向至另外的页面，就不会造成重复的请求了。
                我们应每次都给成功的POST请求做重定向。 这就是web开发的最佳实践。
                """
                return HttpResponseRedirect('/contact/thanks/')
            except:
                errors.append('Can not send email.')

    return render_to_response('contact_form_original.html', {
        'errors': errors,
        'subject': request.POST.get('subject', '').strip(),
        'message': request.POST.get('message', '').strip(),
        'email': request.POST.get('email', '').strip()
        }
    )
