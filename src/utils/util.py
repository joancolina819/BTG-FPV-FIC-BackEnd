import json
import logging
import traceback

logger=logging.getLogger()
logger.setLevel(logging.INFO)

def build_error_response(e):
    logger.info("## start build_error_response")

    logger.info(f"error recibido {e}")

    dict_error = {
        "message": str(e).replace('\'',''),
        "traceback": str(traceback.format_exc())
    }

    return {
        "statusCode":400,
        "body": json.dumps(dict_error),
        "headers":{
            "content-type": "application/json"
        },
        "isBase64Encoded":False
    }

