import json
from aiohttp import web


async def hello(body):
    print(f"body: {json.dumps(body)}")
    if body is None:
        return web.json_response(data={"result": "empty"}, status=400)

    # print(json.dumps(body))
    return web.json_response(data={"result": "ok"}, status=200)
