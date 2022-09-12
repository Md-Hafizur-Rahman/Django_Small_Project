from urllib import request
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.db.models.signals import pre_init,pre_save,pre_delete,pre_migrate,post_init,post_save,post_delete,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
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
# user_logged_in.connect(login_success,sender=User)
    
@receiver(user_logged_out,sender=User)
def login_success(sender,request,user,**kwargs):
    print('...............')
    print('logout_success with signals')
    print('sender',sender)
    print('request',request)
    print('user',user)
    print('user_passwd:',user.password)
    print(f'kwargs:{kwargs}')

@receiver(user_login_failed)
def login_success(sender,request,credentials,**kwargs):
    print('...............')
    print('login_failed with signals')
    print('sender',sender)
    print('request',request)
    print('credentials:',credentials)
    print(f'kwargs:{kwargs}')
@receiver(pre_save,sender=User)
def at_brginning_save(sender,instance,**kwargs):
    print('...............')
    print('Pre_save signals')
    print('sender:',sender)
    print('Instance:',instance)
    print(f'kwargs:{kwargs}')
    
@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print('...............')
        print('Post_save created with new record signals')
        print('sender:',sender)
        print('Instance:',instance)
        print('Created:',created)
        print(f'kwargs:{kwargs}')
    else:
        print('...............')
        print('Post_save created with update record signals')
        print('update')
        print('sender:',sender)
        print('Instance:',instance)
        print('Created:',created)
        print(f'kwargs:{kwargs}')
        
@receiver(pre_delete,sender=User)
def at_brginning_delete(sender,instance,**kwargs):
    print('...............')
    print('Pre_delete signals')
    print('sender:',sender)
    print('Instance:',instance)
    print(f'kwargs:{kwargs}')
    
@receiver(post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print('...............')
    print('Post_delete  signals')
    print('deleted')
    print('sender:',sender)
    print('Instance:',instance)
    print(f'kwargs:{kwargs}')
    
@receiver(request_started)
def at_brginning_delete(sender,environ,**kwargs):
    print('...............')
    print('request_started signals')
    print('sender:',sender)
    print('Environ:',environ)
    print(f'kwargs:{kwargs}')
    
@receiver(request_finished)
def at_brginning_delete(sender,**kwargs):
    print('...............')
    print('request_finished signals')
    print('sender:',sender)
    print(f'kwargs:{kwargs}')
@receiver(got_request_exception)
def at_brginning_delete(sender,request,**kwargs):
    print('...............')
    print('got request exception')
    print('sender:',sender)
    print('request:',request)
    print(f'kwargs:{kwargs}')
    
@receiver(pre_migrate)
def before_insatall_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('...............')
    print('pre_migrate')
    print('sender:',sender)
    print('app_config:',app_config)
    print('verbosity:',verbosity)
    print('interactive:',interactive)
    print('Using:',using)
    print('Plan:',plan)
    print('apps:',apps)
    print(f'kwargs:{kwargs}')
@receiver(post_migrate)
def before_insatall_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print('...............')
    print('post_migrate')
    print('sender:',sender)
    print('app_config:',app_config)
    print('verbosity:',verbosity)
    print('interactive:',interactive)
    print('Using:',using)
    print('Plan:',plan)
    print('apps:',apps)
    print(f'kwargs:{kwargs}')