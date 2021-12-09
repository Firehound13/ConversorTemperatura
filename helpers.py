def celsius_para_kelvin(temperatura_celsius):
    """"Converte a temperatura de Celsius para Kelvin
    Formula: Celsius = Kelvin  + 273.15
    """
    temperatura_kelvin = temperatura_celsius + 273.15
    return temperatura_kelvin

def celsius_para_fahrenheit(temperatura_celsius):
    """
    Converte a temperatura de celsius para fahrenheit
    Formula: Fahrenheit = Celsius * 9 / 5 + 32
    """
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    return temperatura_fahrenheit