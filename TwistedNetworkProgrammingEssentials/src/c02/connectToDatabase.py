from twisted.web import server,resource,http
from twisted.internet import reactor
from twisted.enterprise import adbapi
import os
class dataprocess(object):
    def __init__(self):
        self.ListResult=[]
        self.dbpool=adbapi.ConnectionPool("psycopg2",
            host="localhost",
            password="15263748",
            database="test",
        )
    def getData(self,user):
        print 'getData'
        return self.dbpool.runQuery("SELECT * FROM users")
    def printResult(self,dataSet):
        print 'printResult'
        if dataSet:
            print 'DataSet:'
            for item in dataSet:
                print item
                self.ListResult.append(item)
            return self.ListResult
        else:
            print 'No data'
    def errorHandle(self,error):
        print 'An error has occurred:<%s>'%str(error)
class Simple(resource.Resource):
    isLeaf=True
    #allowedMethods=('GET')
    def __init__(self):
        pass
    def render_GET(self,request):
        #headers=request.getAllHeaders()
        uri=request.uri
        print uri
        print request.args,'\n',request.path
        pgsqldata=dataprocess()
        d=pgsqldata.getData('crackpot')
        d.addCallback(pgsqldata.printResult)
        d.addErrback(pgsqldata.errorHandle)
        #request.setResponseCode(http.NOT_FOUND)
        #return ''
        #request._sendError(404,'Can not found')
        return "<html>Hello,world!<br>Fetch succed!</html>"
        #equivalent of cursor.execute(statement),return cursor.fetchall()
if __name__=='__main__':
    site=server.Site(Simple())
    reactor.listenTCP(8000,site)
    print 'run'
    reactor.run()