import sqlalchemy
#print sqlalchemy.__version__
from sqlalchemy import create_engine
engine=create_engine('sqlite:///:memory:',echo=True)
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
metadata=MetaData()
users_table=Table('users',metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String(50)),
    Column('fullname',String),
    Column('password',String),
)
metadata.create_all(engine)
class User(object):
    def __init__(self,name,fullname,password):
        self.name=name
        self.fullname=fullname
        self.password=password
    def __repr__(self):
        return "<User('%s','%s', '%s')>"%(self.name,self.fullname,self.password)
from sqlalchemy.orm import mapper
mapper(User,users_table)
ed_user=User('crackpot','Crackpot','password')
print 'username:',ed_user.name
print 'fullname:',ed_user.fullname
print 'password:',ed_user.password
print 'id:',str(ed_user.id)