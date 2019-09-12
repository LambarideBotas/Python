#Importa as biblilhotecas
import wikipedia
from googletrans import Translator
#Cria um loop para o menu
while True:
    #Coleta as Informçoes
    p = str(input('Oque deseja pesquisar? :'))
    p1 = int(input('Digite quantas cetenças vc quer :'))
    p2 = str(input('Vc desaja imagens? [S/N] :'))
    #Aqui seria se a pessoa quisesse imagens
    if p2 == 'S':
        #Biblilhoteca do google de imagens
        from google_images_download import google_images_download
        #Define a busca
        busca = p
        #Pede o limite de imagens
        limit = int(input("Qual o limite? :"))
        #Pede para o google se preparar
        response = google_images_download.googleimagesdownload()
        #Argumentos da pesquisa
        arguments = {"keywords": busca, "limit": limit, "delay": 1, "output_directory": "train",
                     "prefix": busca}
        #Mostra se a imagem baixou corretamente
        paths = response.download(arguments)
        print(paths)
    #Para o programa comprender melhor eu usei listas
    lista1 = [p]
    #O wikipedia so recebe em ingles entao aqui o programa vai traduzir oque o cliente pediu para ingles
    transletor = Translator()
    translations = transletor.translate(lista1, dest='en')
    for translation in translations:
        t1 = translation.text
    #Aqui o wikipedia vai fazer a pesquisa e tambem tirar palavras inadequadas
    w = wikipedia.summary(t1, sentences=p1)
    #Aqui ele ira traduzir o texto do ingles para o portugues
    transletor = Translator()
    lista = [w]
    translations = transletor.translate(lista, dest='pt')
    for translation in translations:
        #Aqui ele salva e cria um arquivo no word
        print("")
        print(translation.text)
        t2 = translation.text
        print("")
        print('Criando aquivo RTF')
        p3 = str(input("Digite o nome do arquivo (Adicionar .rtf) :"))
        #Aqui ele adiciona a pepsquisa no arquivo do word altomaticamente
        arquivo = open(p3, 'w')
        arquivo.write(t2)
        arquivo.close()
        print("")
        print("/----/FIM/----/")
        print('')
