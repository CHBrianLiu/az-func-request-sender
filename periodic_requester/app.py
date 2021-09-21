import logging
from typing import List

import requests


def send_requests(hosts: List[str], uri: str):
    for host in hosts:
        endpoint = "https://" + host + uri
        logging.info("send GET reqeust to %s", endpoint)
        send_request(endpoint)

def send_request(endpoint: str):
    try:
        with requests.get(endpoint) as response:
            logging.info("Status: %s", response.status_code)
    except Exception:
        logging.exception("Unexpected error.")
