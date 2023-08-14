import hashlib
from hmac import compare_digest
import json
import datetime
import base64
#TODO: use randum salt per user or login if needed

#TODO move to setting or db
AUTH_SECRET = 'TODO replace with a random secure string 123'
AUTH_TTL = 12000

def create_sing(message_bytes, secret, salt=''):
    h=hashlib.blake2b((secret+salt).encode())
    h.update(message_bytes)
    sign = h.hexdigest()

    return sign

def create_token(user_id):
    create_date_string = datetime.datetime.now().isoformat()
    td = dict(user_id=user_id, timestamp=create_date_string, sign='')

    data_string = json.dumps(td)
    data_string_bytes = data_string.encode("ascii")
    sign = create_sing(data_string_bytes, AUTH_SECRET)
    td['sign'] = sign

    token_string = json.dumps(td)
    token_string_bytes = token_string.encode("ascii")
    base64_bytes = base64.b64encode(token_string_bytes)

    return base64_bytes

def verify_token(token_base64_bytes):
    try:
        token_string_bytes = base64.b64decode(token_base64_bytes)
        token_string = token_string_bytes.decode("ascii")
        td = json.loads(token_string)
        check_sign = td['sign']
        timestamp =  datetime.datetime.fromisoformat(td['timestamp'])

        if(datetime.timedelta(minutes=AUTH_TTL) < datetime.datetime.now() - timestamp):
            return False, 'timeout'

        td['sign'] = ''
        data_string = json.dumps(td)
        data_string_bytes = data_string.encode("ascii")
        sign = create_sing(data_string_bytes, AUTH_SECRET)

    except Exception:
        return False, 'parsing failed'

    if compare_digest(check_sign, sign):
        return True, td['user_id']
    return False, 'sign verify failed'

if __name__ == "__main__":
    # small test cases
    token = create_token('tst')
    assert True == verify_token(token)[0]
    assert False == verify_token(token+b'1')[0]
