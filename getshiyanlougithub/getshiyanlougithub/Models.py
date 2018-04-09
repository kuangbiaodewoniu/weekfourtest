# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: Models.py 
@time: 2018/04/08 
"""
from sqlalchemy import create_engine
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('mysql+mysqldb://root:root@192.168.100.78:3306/51fanli_django?charset=utf8')
Base = declarative_base()


class Repository(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)


if __name__ == '__main__':
    Base.metadata.create_all(engine)