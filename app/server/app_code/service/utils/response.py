import traceback
import json
from app_code.exception.basic_exception import NotFoundException, NotChangeException, RepeatException, RequiredException, LoginException, DeleteYourSelfException, DeleteRootException

from flask import request, jsonify, make_response, send_file

def try_catch(action):
    status_code = 200
    try:
         response, msg = action()

         res = get_response(data = response, status_code = status_code, msg = msg)

    except NotFoundException as error:

        status_code = 404
        res = error_response(error, status_code)      

    except NotChangeException as error:

        status_code=406
        res = error_response(error, status_code)      
    
    except RepeatException as error:

        status_code=406
        res = error_response(error, status_code)      
    
    except RequiredException as error:

        status_code=406
        res = error_response(error, status_code)      

    except LoginException as error:

        status_code=404
        res = error_response(error, status_code)      

    except DeleteYourSelfException as error:

        status_code=406
        res = error_response(error, status_code)      

    except DeleteRootException as error:

        status_code=406
        res = error_response(error, status_code)      

    except Exception as error:

        status_code = 500
        res = error_response(error, status_code)      

    finally:

        response = make_response(json.dumps(res), status_code)
        response.headers['mimetype'] = 'application/json'
        return response


def error_response(error, status_code):

    traceback.print_exc()

    return get_response(status_code = status_code, msg = str(error))

def get_response(status_code, msg, data = None,):

    return {
            "data": data,
            "status": status_code,
            "msg": msg
        }