# 80. Cargar JSON de forma segura
def safe_json_load(s):
    import json
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return None
