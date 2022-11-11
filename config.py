# -*- coding=utf-8 -*-
import os


class Config:
    SECRET_KEY = 'root'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass


# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/shop'
    DEBUG = True  # 打开调试端口


# define the config
config = {
    'default': DevelopmentConfig
}
