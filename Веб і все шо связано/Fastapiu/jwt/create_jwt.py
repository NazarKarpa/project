import jwt as jv

headers = {
    'alg': 'HS256',
    'type': 'JWT',
}
payload = {
    'username': 'tester_user',
    'email': 'tester@gmail.com',
    'is_activate': False,
}

secret = 'secret_1234'

encoded_token = jv.encode(headers=headers, payload=payload, key=secret)

try:
    decoded_token = jv.decode(encoded_token, secret, algorithms=('HS256'))
    print(decoded_token)
except jv.InvalidTokenError:
    print('Invalid token')
except jv.DecodeError:
    print('decoded eror')