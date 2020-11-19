def trueReturn(data, msg):
    return {
        "code": 0,
        "data": data,
        "msg": msg
    }

def falseReturn(data=None, msg=''):
    return {
        "code": -1,
        "data": data,
        "msg": msg
    }