from twisted.internet import reactor
from twisted.web import static,server

root=static.File("/home/workspace/gftop/TwistedWebExample/learning/static/")
reactor.listenTCP(8080,server.Site(root))
reactor.run()

