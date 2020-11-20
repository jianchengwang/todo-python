def result(data=None, msg='', status=200):
    return {
        "data": data,
        "msg": msg
    }, status, {'ContentType':'application/json'}

def badRequest(msg='Bad Request'):
    return result(msg=msg, status=400)

def notAuth(msg='Not Auth'):
    return result(msg=msg, status=401)

def notPermission(msg='Not Permission'):
    return result(msg=msg, status=403)

def notFound(msg='Not Found'):
    return result(msg=msg, status=404)

def serveError(msg='Serve Error'):
    return result(msg=msg, status=500)
