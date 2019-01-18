import socket
import json

## we store products in memory. trying to keep it lightweight
products = {"book":{"title":"book", "price":1, "inventory_count":5},
            "shoe":{"title":"shoe", "price":2, "inventory_count":6},
            "food":{"title":"food", "price":3, "inventory_count":7},
            "bark":{"title":"bark", "price":4, "inventory_count":8},
            "bazz":{"title":"bazz", "price":5, "inventory_count":9},
            "booo":{"title":"booo", "price":100, "inventory_count":0}}

## quick reference for what codes correspond to
codes = {200: "OK", 404: "Not Found", 400: "Bad Request"}

## given a code and a body, generates the appropriate http reply
def http_format(code, message):
    return f"HTTP/1.1 {code} {codes[code]}\r\n\r\n{message}".encode()

## given an endpoint :: String and a params :: Dict 
## will return the appropriate http response to handle a get
def getter(endpoint, params):
    print("GET", endpoint, params)

    # default to 404
    code, message = 404, "Not in spec"

    # landing page
    if endpoint == "" or endpoint == "index.html":
        code, message = 200, "Super simple API home!"

    # code path for dealing with fetching price/stock
    elif endpoint == "fetch":
        output = {}
        for key in params.keys():
            if key in products.keys():
                output[key] = products[key]
            else:
                output[key] = None
        code, message = 200, json.dumps(output)

    # code path for listing store catalogue, plus option to see only in stock
    elif endpoint == "catalogue":
        if params and "available" in params.keys() and params["available"] != "0":
            output = {}
            for key, value in products.items():
                if value["inventory_count"] > 0: output[key] = value
            code, message = 200, json.dumps(output)
        else:
            code, message = 200, json.dumps(products)

    return http_format(code, message)

## same as getter but for posts
def poster(endpoint, params):
    print("POST", endpoint, params)
    code, message = 404, "Not in spec"

    # the only posts are buy and unbuy here, so we deal exclusively with those
    # and 404 the rest
    if endpoint == "buy":
        multiplier = 1
    elif endpoint == "unbuy":
        multiplier = -1
    else:
        return http_format(code, message)

    output = {}
    for key, value in params.items():
        if key in products.keys():
            if value:
                decrease = int(value)
            else:
                decrease = 0
            products[key]["inventory_count"] = \
                max(0, products[key]["inventory_count"] - multiplier*decrease)
            output[key] = products[key]
        else:
            output[key] = None
    code, message = 200, json.dumps(output)

    return http_format(code, message)

def param_parse(raw_params):
    # transforms "a=b&c=d&... into a dict {a:b, c:d, etc.}"
    pairs = [tuple(x.split("=")) for x in raw_params.split("&")]
    params = {}
    for key, value in pairs:
        params[key] = value
    return params

host = ''
port = 8000

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
main_socket.bind((host, port))
main_socket.listen(1)

print(f"serving http on port {port}")

while True:
    # default response in case of shenanigans
    response = http_format(404, "Not in spec")
    connection, address = main_socket.accept()
    raw_request = connection.recv(4096)
    try:
        request_type, request, version = \
          tuple(x.decode() for x in raw_request.split(b"\r\n")[0].split())

        # print(raw_request)

        if "?" in request:
            endpoint, raw_params = tuple(request[1:].lower().split("?"))
            params = param_parse(raw_params)
        else:
            endpoint, raw_params = request[1:], {}
            params = {}

        if request_type   == "GET":
            response       = getter(endpoint, params)
        elif request_type == "POST":
            response       = poster(endpoint, params)
    except ValueError:
        response = http_format(400, "Bad formatting")

    print(response)

    connection.sendall(response)
    connection.close()


