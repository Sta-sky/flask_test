import os

from flask import Blueprint
from flask import request
from tool_script.log_test import Log
import uuid
from flask_test.setting import UAER_KEY
from tool_script.token_jwt import generate_token
from tool_script.python加密 import user_pub_add_salt
from tool_script.python加密 import generate_pub_rsa_key
from tool_script.byte_change_str import change_str
logger = Log('flask.app2').print_info()


login = Blueprint(name='user_login', import_name='login',
                  static_folder='../static',)
check_login = Blueprint(name='checklogin', import_name='check')


@login.route('/login')
def user_login():
    if request.method == 'GET':
        logger.info(request)
        logger.info(request)
        logger.info(type(request))
        logger.info('=='*100)
        name = 'app2'
        token = generate_token(name)
        generate_pub_rsa_key()
        _file = os.path.realpath('../' + 'token.ini')
        logger.info(_file)

        logger.info(UAER_KEY)
        pub_filename = os.path.realpath('rsa.pub.key')
        print(pub_filename)
        with open(pub_filename, 'r') as fp:
            secrete = change_str(user_pub_add_salt(fp, UAER_KEY))
        logger.error(secrete)
        logger.info('=='*100)

        data = {
            'name': 'less',
            'age': 34,
            'sex': 'w',
            'uuid': uuid.uuid4(),
            'token': token,
            'secrete': secrete
        }
        info = f"{name}: {token}\n"
        logger.info(info)
        with open(_file, 'a+') as fp:
            fp.write(info)
        return data


@check_login.route('/checklogin')
def check_user_login():
    if request.method == 'GET':
        user_key = None
        rsp = request.get_data(as_text=True)
        print(type(rsp))
        print(rsp)
        decrypt_text = rsp.split('=')[1]
        print(decrypt_text)
        secrete_file_info = os.path.realpath('../flask_test/setting.py')
        with open(secrete_file_info, 'r') as fp:
            user_info = fp.readlines()
        for info in user_info:
            if info.find('UAER_KEY') == 0:
                user_key = eval(info.split('=')[1])
        if decrypt_text == user_key:
            return {'msg': '登录成功'}
        else:
            return {'msg': '私钥错误，登录失败'}
