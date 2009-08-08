// 创建项目
crackpot@linux-Crackpot:/home/workspace/gftop> django-admin.py startproject cms

// 修改项目中的设置文件
crackpot@linux-Crackpot:/home/workspace/gftop/cms> vim settings.py

// 创建数据库文件
crackpot@linux-Crackpot:/home/workspace/gftop/cms> python manage.py syncdb
Creating table auth_permission
Creating table auth_group
Creating table auth_user
Creating table auth_message
Creating table django_content_type
Creating table django_session
Creating table django_site
Creating table django_admin_log

You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes
Username (Leave blank to use 'crackpot'):
E-mail address: gaofeitop@gmail.com
Password:
Password (again):
Superuser created successfully.
Installing index for auth.Permission model
Installing index for auth.Message model
Installing index for admin.LogEntry model
crackpot@linux-Crackpot:/home/workspace/gftop/cms>

// 验证是否正确
crackpot@linux-Crackpot:/home/workspace/gftop/cms> python manage.py validate
0 errors found

// 启动服务
crackpot@linux-Crackpot:/home/workspace/gftop/cms> python manage.py runserver
Validating models...
0 errors found

Django version 1.1, using settings 'cms.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

// 访问http://127.0.0.1:8000/admin/发现无法出现管理页面，修改settings.py和urls.py中关于admin的项目

