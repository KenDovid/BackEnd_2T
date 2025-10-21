# 97. Cliente API simulado
def simple_api_client(base_url):
    def get(endpoint):
        print(f"GET → {base_url}/{endpoint}")
    def post(endpoint, data):
        print(f"POST → {base_url}/{endpoint} con datos {data}")
    return {"get": get, "post": post}

