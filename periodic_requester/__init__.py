import json
import logging
import os
from typing import List

import azure.functions as func

from periodic_requester.app import send_requests


def main(mytimer: func.TimerRequest) -> None:
    hosts: List[str] = json.loads(os.environ.get("hosts", "[]"))
    uri = os.environ.get("uri", "/")
    logging.info(
        "Azure function app got executed. Will be sending requests to %s with uri %s",
        hosts,
        uri,
    )
    send_requests(hosts, uri)
