import json


def lambda_handler(event, context):
	event = event or {}
	params = event.get("queryStringParameters") or {}
	nombre = params.get("nombre") or event.get("nombre")

	if isinstance(nombre, str) and nombre.strip():
		mensaje = f"hola {nombre.strip()}"
	else:
		mensaje = "hola mundo"

	return {
		"statusCode": 200,
		"body": json.dumps({"mensaje": mensaje}),
	}
