from media import media

from moda import moda

from desvio_padrao import desvio

from mediana import mediana

from variancia import variancia

from matplotlib import pyplot as plt

ensino_fundamental1= [1,8,9,10,3,5,8,8,9]
ensino_fundamental1.sort()
ensino_medio = list(range(1,151))
ensino_medio.sort()

aluno = ['Liz' , 'Davi' , 'Andrew' , ' Otávio' , 'Aline']


def hadle(lista):

    print('Aluno')
    print('----------------------------')
    media(lista)
    mediana(lista)
    moda(lista)
    varianca(lista)
    desvio(lista)



def hadle(lista1):

    print('nota')
    print('----------------------------')
    media(lista1)
    mediana(lista1)
    moda(lista1)
    varianca(lista1)
    desvio(lista1)
    

hadle(ensino_fundamental1)  

plt.plot(aluno, ensino_fundamental1, linestyle = '--', marker = "o")
plt.plot(aluno, ensino_medio, linestyle = '--', marker = "o")



plt.title('Alunos e notas')
plt.xlabel('nota')
plt.ylabel('aluno')


plt.show()

