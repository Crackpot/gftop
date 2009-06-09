#coding=utf-8
"""
    def _parse(url, defaultPort=None):  (source)
    Split the given URL into the scheme, host, port, and path.
    Parameters    url    An URL to parse. (type: str )
                  defaultPort    An alternate value to use as the port if the URL does not include one. (type: int or None )
    Returns    A four-tuple of the scheme, host, port, and path of the URL. All of these are str instances except for port, which is an int. 
"""
from twisted.web.client import _parse
value=_parse('http://www.google.cn/search?q=sp&btnG=Google+%E6%90%9C%E7%B4%A2&hl=zh-CN&client=firefox-a&rls=org.mozilla%3Azh-CN%3Aunofficial&hs=iZE&newwindow=1&sa=2')
print value
for item in value:
    print item