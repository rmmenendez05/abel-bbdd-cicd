import json

from handler import lambda_handler


def mensaje(resp):
	return json.loads(resp["body"])["mensaje"]


def test_con_nombre():
	assert mensaje(lambda_handler({"nombre": "David"}, None)) == "hola David"


def test_con_query_string():
	ev = {"queryStringParameters": {"nombre": "David"}}
	assert mensaje(lambda_handler(ev, None)) == "hola David"


def test_sin_nombre():
	assert mensaje(lambda_handler({}, None)) == "hola mundo"


def test_nombre_vacio():
	assert mensaje(lambda_handler({"nombre": "  "}, None)) == "hola mundo"
