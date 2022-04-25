import json
import traceback
from src.utils.util import build_error_response


def test_build_error_response():

    exeption="BaseExepction"
    dict_error = {
        "message": str(exeption).replace('\'',''),
        "traceback": str(traceback.format_exc())
    }
    expected = {
        "statusCode":400,
        "body": json.dumps(dict_error),
        "headers":{
            "content-type": "application/json"
        },
        "isBase64Encoded":False
    }
    response = build_error_response(exeption)

    assert response == expected