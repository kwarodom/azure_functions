import logging
import json
import azure.functions as func
from datetime import date, datetime
import pytz

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
        req_body["datetime"] = str(datetime.now(pytz.timezone('Asia/Bangkok')))

    if name:
        doc.set(func.Document.from_json(json.dumps(req_body)))
        return func.HttpResponse(
             "push data to cosmosdb",
             status_code=200
        )
        # return func.HttpResponse(f"Hello, {name}. quemessage test")
    else:
        doc.set(func.Document.from_json(json.dumps(req_body)))
        return func.HttpResponse(
             "push data to cosmosdb",
             status_code=200
        )
