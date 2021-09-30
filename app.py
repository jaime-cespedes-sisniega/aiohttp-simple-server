from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    response_txt = {'text': 'Hello'}
    return web.json_response(response_txt, status=200)


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == "__main__":
    main()
