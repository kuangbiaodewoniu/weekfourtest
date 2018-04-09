# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: Models.py 
@time: 2018/04/08 
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('mysql+mysqldb://root:root@192.168.100.78:3306/51fanli_django?charset=utf8')
Base = declarative_base()


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), index=True)
    desc = Column(String(1024))
    users = Column(Integer)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    userlevel = Column(String(20))
    joindate = Column(String(50))


if __name__ == '__main__':
    Base.metadata.create_all(engine)