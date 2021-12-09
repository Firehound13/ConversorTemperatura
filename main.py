"""Programa no Python 3 para converter de Celsius para Kelvin + Fahrenheit."""
from helpers import celsius_para_kelvin, celsius_para_fahrenheit
if __name__ == '__main__':
        while True:
            mensagem = ('Qual a temperatura em Celsius?')
            mensagem += ("Pressione 'q' para sair!")

            try:
                celsius = input(mensagem)
                if celsius.lower() != 'q':
                    print(f"Celsius para Kelvin(K) {celsius_para_kelvin(float(celsius))}")
                    print(f"Celsius para Fahrenheit(F) {celsius_para_fahrenheit(float(celsius))}")
                else:
                    print("Até a próxima!")
                    break
            except ValueError:
                    print("Você digitou um caractere inválido!Por favor digite um número ou a letra 'q'")