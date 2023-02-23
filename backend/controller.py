from sanic import Sanic
from sanic.response import json

app = Sanic("raniac-api-service")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run()
