from framework.classes import RequestT
from framework.handlers.generate_404 import generate_404
from framework.handlers.hello import handle_hello
from framework.handlers.index import handle_index
from framework.handlers.logo import handle_logo
from framework.handlers.styles import handle_styles
from framework.handlers.system_handlers.error import handler_error


def make_error(_request):
    1 / 0


handlers = {
    "/": handle_index,
    "/styles/": handle_styles,
    "/logo.png/": handle_logo,
    "/e": make_error,
    "/hello": handle_hello,
}


def application(environ, start_response):
    try:
        path = environ["PATH_INFO"]

        handler_info = handlers.get(path, generate_404)

        request_headers = {
            key[5:]: environ[key]
            for key in filter(lambda key: key.startswith("HTTP_"), environ)
        }
        request = RequestT(
            method=environ["REQUEST_METHOD"],
            headers=request_headers,
            path=path,
            query=environ.get("QUERY_STRING"),
        )

        response = handler_info(request)

    except Exception:
        response = handler_error()

    start_response(response.status, list(response.headers.items()))
    yield response.payload
