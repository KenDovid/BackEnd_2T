# 92. Conversor de monedas usando función retornada
def currency_converter(rates_dict):
    def convertir(moneda_origen, moneda_destino, cantidad):
        if moneda_origen not in rates_dict or moneda_destino not in rates_dict:
            return "Moneda no encontrada"
        valor_usd = cantidad / rates_dict[moneda_origen]
        return valor_usd * rates_dict[moneda_destino]
    return convertir

