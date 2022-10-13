import json
import sys
from general.variables import MAX_PACKAGE_LENGTH, ENCODING
from general.errors import IncorrectDataReceivedError, NonDictInputError
from general.decos import log
sys.path.append('../')


@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    json_response = encoded_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    else:
        raise TypeError


@log
def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
