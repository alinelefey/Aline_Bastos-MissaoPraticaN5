from faker import Faker
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from num2words import num2words
        

### GERAÇÃO DADOS ###
class randomica:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

fake = Faker('pt_BR')
lista_random = []

for a in range (10):
    nota = fake.random_int(1,10)
    nome = fake.name ()
    dados = randomica (nome, nota)
    lista_random.append (dados)


### GRAVACAO DE DADOS ###
def gravacao (lista_random):
    arquivo = open ('DadosLista.txt','w+')
    for dados in lista_random:
       arquivo.write (dados.nome + "," + str (dados.nota) + "\n")

    arquivo.close()

gravacao (lista_random)


### IMPORTAÇÃO DE DADOS ###
def importacao ():
    arquivo = open ('DadosLista.txt','r')
    lista = arquivo.read () .splitlines()
    lista_random2 = []
    for NomesNotas in lista:
        lista2 = NomesNotas.split(',')  
        dados = randomica (lista2 [0],lista2 [1])
        lista_random2.append (dados)
    arquivo.close ()
    
    return lista_random2


### HISTOGRAMA ###
lista2 = importacao() 
lista_notas = []
lista_ordinal = []
for i in lista2:
    numero = int(i.nota)
    lista_notas.append (numero)
    num_ptbr = num2words(numero, lang='pt-br')
    lista_ordinal.append (num_ptbr)   
    

plt.hist(lista_notas,density=True,facecolor='blue', alpha=0.75)

plt.xlabel('Pontuações')
plt.ylabel('Probabilidade')
plt.title('Histograma das Pontuações')
plt.grid(True)
plt.show()


### NUVEM DE PALAVRAS ###
texto = (" ").join(lista_ordinal)
nuvem_palavras = WordCloud(background_color='black',
                           width=800,height=400).generate(texto)
plt.imshow(nuvem_palavras, interpolation='bilinear')
plt.axis("off")
plt.show()
nuvem_palavras.to_file("Nuvem de palavras.png")








