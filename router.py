from controllers import hello, exchange_rate

ROUTES = dict({
    "/" : {
        "controller": hello.helloWorld
    },
    "/convert": {
        "controller": exchange_rate.convert
    }
})

STATUS_OK = 200
STATUS_ROUTE_NOT_FOUND = 404

def route(path, input=b''):
    """Routes a request to the appropriate controller using the path"""
    if path in ROUTES:
        if len(input) > 0:
            return (STATUS_OK, ROUTES[path]['controller'] (input))
        return (STATUS_OK, ROUTES[path]['controller'] ())
    else:
        return (STATUS_ROUTE_NOT_FOUND, "{{\"message\": \"{} path not found\"}}".format(path))