from vibora import Vibora, Request
from vibora.responses import JsonResponse


app = Vibora()


@app.route('/hello-world', methods=['GET', 'POST'])
async def hello_world(request: Request):
    response = {
        'ok': True, 'method': request.method, 'hello': 'world'
    }
    if request.method == b'POST':
        response.update(
            {'hello': (await request.json()).get('who', 'whoareyou?')}
        )
    return JsonResponse(response)


app.run(host='0.0.0.0', port=8000, workers=4)
