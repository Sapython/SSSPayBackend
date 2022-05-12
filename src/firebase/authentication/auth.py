from src.helpers.requestData import getRequestData

class Authentication:
    def __init__(self, auth):
        self.auth = auth

    def verifyToken(self,func):
        def wrapper(*args, **kwargs):
            print(args,kwargs)
            dataType = {
                'token':{
                    'type':'string',
                },
                'uid':{
                    'type':'string',
                }
            }
            data = getRequestData(args[0],dataType)['FORMED_DATA']
            print('---- Data ---- ',data)
            if data['token'] is None:
                return {'error': 'Token is required'}, 400
            try: 
                decoded_token = self.auth.verify_id_token(data['token'])
            except ValueError:
                return {'error': 'Invalid token'}, 400
            kwargs['verified']=data['uid'] == decoded_token['uid']
            return func(*args, **kwargs)
        return wrapper
        