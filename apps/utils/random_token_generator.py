# ALL METHODS TO GENERATE TOKENS FOR 
# 1 - Epins
# 2 - Username
# 3 - Others ...

import os
import base64
from apps.network_settings.models import TokenCreationHelper as TCH



def subadmin_username (country, usertype):
    user_id = 1
    #pad the string
    number_generate = str(user_id).rjust(5,"0")
    base64.b32encode(bytes(number_generate, 'utf-8')).decode('utf-8').replace('=','')


def random_admin_password_gen ():
    user_id = 1
    #pad the string
    number_generate = str(user_id).rjust(5,"0")
    base64.b32encode(bytes(number_generate, 'utf-8')).decode('utf-8').replace('=','')
