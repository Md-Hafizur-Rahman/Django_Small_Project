from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print('...............')
    print('login_success with signals')
    print('sender',sender)
    print('request',request)
    print('user',user)
    print('user_passwd: ',user.password)
    print(f'kwargs:{kwargs}')
    
@receiver(user_logged_out,sender=User)
def login_success(sender,request,user,**kwargs):
    print('...............')
    print('logout_success with signals')
    print('sender',sender)
    print('request',request)
    print('user',user)
    print('user_passwd: ',user.password)
    print(f'kwargs:{kwargs}')

@receiver(user_login_failed)
def login_success(sender,request,credentials,**kwargs):
    print('...............')
    print('login_failed with signals')
    print('sender',sender)
    print('request',request)
    print('credentials:',credentials)
    print(f'kwargs:{kwargs}')

# user_logged_in.connect(login_success,sender=User