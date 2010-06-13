from os import system, chdir
from os.path import join
from shutil import rmtree, copytree

def system_echo(cmd):
    print cmd
    system(cmd)

class SVN:
    def __init__(self, url, rev):
        self.data = {'url':url, 'rev':rev}

    def checkout(self):
        system_echo('svn co %(url)s -r %(rev)d' % self.data)
        
class HG:
    def __init__(self, url, dst, rev):
        self.url = url
        self.dst = dst
        self.rev = rev

    def checkout(self):
        slash = self.url.rstrip('/').rindex('/') + 1
        src = self.url[slash:]
        rmtree(src, ignore_errors=True)
        rmtree(self.dst, ignore_errors=True)
        
        system_echo('hg clone %s' % self.url)
        chdir(src)
        system_echo('hg up -r %s' % self.rev)
        chdir('..')
        copytree(join(src,self.dst), self.dst)
        rmtree(src, ignore_errors=True)

class GIT:
    def __init__(self, url, folder, rev):
        self.url = url
        self.folder = folder
        self.rev = rev

    def checkout(self):
        base, app = self.folder.split('/')
        rmtree(base, ignore_errors=True)
        rmtree(app, ignore_errors=True)
        
        system_echo('git clone %s' % self.url)
        chdir(base)
        system_echo('git checkout %s' % self.rev)
        chdir('..')
        copytree(self.folder, app)
        rmtree(base, ignore_errors=True)

libs = (
    SVN('http://code.djangoproject.com/svn/django/trunk/django', 9524),
    SVN('http://django-tagging.googlecode.com/svn/trunk/tagging', 154),
    SVN('http://django-voting.googlecode.com/svn/trunk/voting', 69),
    SVN('http://django-simple-captcha.googlecode.com/svn/trunk/captcha', 18),
    HG('http://bitbucket.org/ubernostrum/django-registration/', 'registration', '00a5396be869'),
    HG('http://bitbucket.org/ubernostrum/django-profiles/', 'profiles', 'ff21fcacdb16'),
    GIT('git://github.com/jezdez/django-robots.git', 'django-robots/robots', '059c630'),
)

for lib in libs:
    lib.checkout()
