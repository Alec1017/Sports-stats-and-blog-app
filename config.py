import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '8$28#675@$'
    MONGO_URI = 'mongodb://root:password1234@ds145010.mlab.com:45010/wbl_data'
