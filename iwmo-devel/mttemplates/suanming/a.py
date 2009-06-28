import suanmingtype
import sys
sys.path.append('/home/workspace/gftop/iwmo-devel')
from utils import proxycache,common
for k,v in suanmingtype.type.items():
    print k,v
from twisted.web.client import getPage
from twisted.web import resource
class SuanmingType(resource.Resource):
    def render(self,request):
        d=proxycache.pcche.perform('getmtstep',mtstep_key)
        d.addCallback(self)
        pass