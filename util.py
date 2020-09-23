import time
import jwt
from tool_script.byte_change_str import change_str

SALT_KEY = 'PXU9@ctuNov20!'


def generate_token(username, exp=3600 * 24):
    """
    过期时间为一天
    :param salt: 加盐值
    :param exp: 过期时间
    :return:
    """
    key = SALT_KEY
    now = time.time()
    payload = {'username': username, 'exp': exp + now}
    return change_str(jwt.encode(payload=payload, key=key, algorithm='HS256'))

result = generate_token('dyy')
print(type(result))
print(change_str(result))

