def dobro_preco(precos):
    return [preco * 2 for preco in precos]

print("Exercício 1:", dobro_preco([5.00, 8.00, 12.00]))


def boas_vindas(nomes):
    return [f"Bem-vindo(a), {nome}!" for nome in nomes]

print("Exercício 2:", boas_vindas(["João", "Maria", "Carlos"]))


def verificar_par_ou_impar(numeros):
    return [(num, "Par" if num % 2 == 0 else "Ímpar") for num in numeros]

print("Exercício 4:", verificar_par_ou_impar([4, 7, 10]))


def gerar_tabuada(numero):
    return [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]

print("Exercício 5 – Tabuada do 2:")
print("\n".join(gerar_tabuada(2)))
print("Tabuada do 3:")
print("\n".join(gerar_tabuada(3)))
print("Tabuada do 4:")
print("\n".join(gerar_tabuada(4)))


def pode_assistir_filme(idades):
    return [(idade, idade >= 18) for idade in idades]

print("Exercício 6:", pode_assistir_filme([15, 20, 8]))


def aplicar_desconto(precos, percentual):
    return [round(preco * (1 - percentual / 100), 2) for preco in precos]

print("Exercício 7:", aplicar_desconto([50, 120, 200], 10))


def contar_letras(palavras):
    return [(palavra, len(palavra)) for palavra in palavras]

print("Exercício 8:", contar_letras(["casa", "paralelepípedo", "python"]))


def celsius_para_fahrenheit(temperaturas_c):
    return [round(c * 1.8 + 32, 2) for c in temperaturas_c]

print("Exercício 9:", celsius_para_fahrenheit([30, 100, 0]))


def classificar_numeros(numeros):
    resultado = []
    for num in numeros:
        if num < 5:
            resultado.append((num, "Pequeno"))
        elif num < 10:
            resultado.append((num, "Médio"))
        else:
            resultado.append((num, "Grande"))
    return resultado

print("Exercício 10:", classificar_numeros([3, 9, 12]))


def eh_palindromo(frases):
    resultado = []
    for frase in frases:
        limpa = ''.join(frase.lower().split())
        resultado.append((frase, limpa == limpa[::-1]))
    return resultado

print("Exercício 11:", eh_palindromo(["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]))


from math import factorial

def calcular_fatoriais(numeros):
    return [(num, factorial(num)) for num in numeros]

print("Exercício 12:", calcular_fatoriais([3, 7, 9, 25, 26]))
