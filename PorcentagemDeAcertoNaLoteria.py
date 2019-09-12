#Funçao da fatorial
def fatorial(n):
    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    print(fat)
    return fat
#Mini exenplo da Mega Sena
print("Gerador de possibilidades de ganhar na mega sena")
print("A Mega-Sena consiste num jogo de 60 números"
" (1 a 60) no qual é permitido apostar de 6 a 15 "
"números (valor das apostas tende a aumentar conforme"
" a quantidade de números assinalados por jogo)")
#Pede as informaçoes
NumerosNaCartela = int(input("Digite a quantidade de numeros na sua cartela :"))
NumerosMarcados = int(input("Digite a quantidade de numeros que vc marcou na tabela :"))
#Faz a fatorial dos numeros marcados usando a funçao criada no inicio
fatorial(NumerosMarcados)
#Nao preciso fatoral 60 inteiro so vou usar os 5 numeros pra tras
n1 = NumerosNaCartela - 1
n2 = NumerosNaCartela - 2
n3 = NumerosNaCartela - 3
n4 = NumerosNaCartela - 4
n5 = NumerosNaCartela - 5
#Faz a fatorial dos 6 numeros
Fatorial1 = NumerosNaCartela *n1 *n2 *n3 *n4 *n5
print(Fatorial1)
#Divide a Fatorial do Numeros da tabela e divide pela fatorial dos numeros marcados
resultado = Fatorial1 / fatorial(NumerosMarcados)
print(resultado)