import jwt


def create_token(data, secret):
    return jwt.encode(data, secret)


def verify_signature(token):
    try:
        data = jwt.decode(token, key="acelera")
    except jwt.exceptions.InvalidSignatureError:
        data = {"error": 2}

    print(data)
    return data
