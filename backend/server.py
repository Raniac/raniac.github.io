from sanic import Sanic
from sanic.log import logger
from sanic.response import json

from api import portfolio, blog, toolkit

app = Sanic("raniac-api-service")
app.blueprint([portfolio, blog, toolkit])

@app.route('/healthcheck')
async def healthcheck(request):
    logger.info(request.body)
    return json({'msg': 'success'})

@app.route('/')
async def test(request):
    logger.info(request.body)
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1470, auto_reload=True)
