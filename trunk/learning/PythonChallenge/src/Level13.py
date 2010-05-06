#coding=utf-8
'''
http://www.pythonchallenge.com/pc/return/disproportional.html
'''
import xmlrpclib
url="http://www.pythonchallenge.com/pc/phonebook.php"  
phonebook=xmlrpclib.Server(url)
print phonebook.system.listMethods()
print phonebook.phone('Bert')
print phonebook.phone('Crackpot')