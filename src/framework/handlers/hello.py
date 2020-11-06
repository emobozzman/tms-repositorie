from urllib.parse import parse_qs

from framework.classes import ResponseT


def handle_hello(request):
    query_string = parse_qs(request.query or "")
    name = query_string.get("name", ["Anon"])[0]

    payload = f"Hello {name}"
    status = "200 OK"
    headers = {
        "Content-type": "text/plain",
    }
    return ResponseT(status, headers, payload.encode())
