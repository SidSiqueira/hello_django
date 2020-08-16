from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def soma(request, valor1, valor2):
    resultado = valor1 + valor2
    return HttpResponse('<h1>A soma de {} - {} = {}<h1>'.format(valor1, valor2, resultado))

def subtracao(request, valor1, valor2):
    resultado = valor1 - valor2
    return HttpResponse('<h1>A subtrção de {} - {} = {}<h1>'.format(valor1, valor2, resultado))

def multiplicacao(request, valor1, valor2):
    resultado = valor1 * valor2
    return HttpResponse('<h1>A multiplicação de {} * {} = {}<h1>'.format(valor1, valor2, resultado))

def divisao(request, valor1, valor2):
    resultado = valor1 / valor2
    if valor1 % valor2 == 0:
        return HttpResponse('<h1>A divisão de {} / {} = {}<h1>'.format(valor1, valor2, int(resultado)))
    else:
        return HttpResponse('<h1>A divisão de {} / {} = {}<h1>'.format(valor1, valor2, round(resultado, 2)))