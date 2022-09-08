from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,post_delete,pre_delete,post_init,pre_init
from django.core.signals import request_finished,request_started,got_request_exception 

##Work in sequence
##Receive signal and then post or pre display signal
#@receiver(user_logged_in,sender=User)
# def login_success(sender,request,user,**kwargs):
#     print("Sender",sender)
#     print("User",user)
#     print(kwargs)

# #user_logged_in.connect(login_success,sender=User)

# @receiver(user_logged_out,sender=User)
# def login_out(sender,request,user,**kwargs):
#     print("Sender",sender)
#     print("User",user)
#     print(kwargs)


# @receiver(user_login_failed)
# def login_out(sender,credentials,request,**kwargs):
#     print("Sender",sender)
#     print("User_Cred",credentials)
#     print(kwargs)

# #Before saving pre_save will be activated and after that post_save
# @receiver(pre_save,sender=User)
# def begin_pre_save(sender,instance,**kwargs):
#     print("Sender",sender)
#     print("Instance",instance)
#     print(kwargs)

# @receiver(post_save,sender=User)
# def post_save(sender,instance,created,**kwargs):
#     if created:
#         print("New Record")
#         print("Sender",sender)
#         print("Instance",instance)
#         print(created)
#         print(kwargs)
#     else:
#         print("Update Record")
#         print("Sender",sender)
#         print("Instance",instance)
#         print(created)
#         print(kwargs)

# #predelete and postdelete is similar to save only

# @receiver(request_started)
# def begin_request(sender,environ,**kwargs):
#     print("Request Send")
#     print("Sender",sender)
#     print(kwargs)

# @receiver(request_finished)
# def end_request(sender,**kwargs):
#     print("Sender",sender)
#     print(kwargs)

# @receiver(got_request_exception)
# def exception_request(sender,request,**kwargs):
#     print("Exception")
#     print("Sender",sender)
#     print(kwargs)