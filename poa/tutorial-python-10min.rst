=======================================================
Aprendendo Python em 10 Minutos
=======================================================

.. footer:: LABASE - NCE

.. |py| replace:: <pre title="py_code">

.. |npy| replace:: </pre>

.. class:: right big

   | *Carlo Emmanoel Tolla de Oliveira*
   | carlo@nce.ufrj.br
   | http://labase.nce.ufrj.br/

.. class:: small

   ©2007, licensed under a `Creative Commons
   Attribution/Share-Alike (BY-SA) license
   <http://creativecommons.org/licenses/by-sa/3.0/>`__.

Introdução
--------------------------------------------------------------------------------

* Tutorial conciso e completo
* Mistura de tutorial com folheto de ajuda
* Requer conhecimento de alguma linguagem
* Palavras chaves destacadas
* Conceitos introduzidos no código e comentados

.. class:: handout

Então, você quer aprender a linguagem de programação Python mas não pode encontrar um tutorial conciso e completo. Este tutorial tentará ensinar-lhe Python em 10 minutos. Não é provavelmente tanto um tutorial porque é um cruzamento entre um tutorial e um folheto, de modo a ensinar apenas alguns conceitos para você poder começar. Obviamente, se você quiser aprender realmente uma língua você necessita programar nela por um tempo. Eu suponho que você é já familiar com alguma linguagem de programação e, saltarei a maioria do material básico. As palavras chaves importantes serão *destacadas* de modo que você possa facilmente localizá-las. Também, fique atento, devido à simplicidade deste tutorial, algumas coisas serão introduzidas diretamente no código e somente levementes comentadas.

Propriedades
--------------------------------------------------------------------------------

* Fortemente tipado
* Linguagem dinâmica
* Sensível a maiúsculas
* Orientado a Objetos

.. class:: handout


O Python é fortemente tipado (isto é, os tipos são reforçados), dinâmicamente, tipados implicitamente (isto é, você não tem que declarar variáveis), sensível a maúsculas e minúsculas (isto é var e VAR são duas variáveis diferentes) e orientado a objetos (isto é, tudo é um objeto).

Sintaxe
--------------------------------------------------------------------------------

* Não obriga ter caracter terminador de comando
* Blocos indicados pela identação
* Comentário de uma linha: *#*
* Strings também são comentários *"comentário"*
* Strings de linhas múltiplas: *''' linhas.. '''*
* Atribuição: *=* *+=* *-=*
* Comparação: *==* *!=* *<* *>* *<=* *>=*
* Funciona para diversos tipos de dados, incluíndo string

.. class:: handout

O Python *não tem nenhum caráter imperativo da terminação de comandos* e os *blocos são especificados pela identação*. Identa-se para iniciar um bloco e deidenta-se para terminar. Indicações que esperam uma extremidade do nível do recorte em uns dois pontos (:). *Comentários* começam com o sinal de libra (#) e são textos de uma única linha, Strings são usados para *comentários multi-line*. *Valores são atribuídos* com o sinal de iguais (“=”), e *teste de igualdade* é feito usando dois sinais de iguais (“==”). Você pode incrementar/decrementar valores usando os operadores += e - = respectivamente. Isto funciona em muitos tipos de dados, inclusive em Strings. 

Atribuição de variáveis
--------------------------------------------------------------------------------

Você pode também usar variáveis múltiplas em uma linha. Por exemplo:

>>> myvar = myothervar = 3
>>> myvar += 2
>>> myvar -= 1
>>> """ isto é um comentário multilinha. 
... As seguintes linhas concatenam as duas strings."""
>>> mystring = "Olá"
>>> mystring += " Mundo"
>>> print mystring
Olá Mundo
>>> # este intercambia duas variáveis em uma única linha. 
>>> myvar, mystring = mystring, myvar

Tipos de dados
--------------------------------------------------------------------------------

* Listas - [1,2,3]
* Tuplas - (1,2,3)
* Tupla unitária - (1,)
* Dicionários - {1:2, 2:4, 4:8}
* Funções - objetos de primeira classe
* Criando dicionários - dict()

.. class:: handout

Os tipos de dados disponíveis no python são *listas, tuplas e dicionários*. Os conjuntos estão disponíveis na biblioteca de *sets*. As listas são como disposições uni-dimensionais (mas você pode também ter listas de outras listas), dicionários são disposições associativas (memórias associativas) e as tuplas são disposições uni-dimensionis immutáveis (as “disposições” Python pode ser de qualquer tipo, assim você pode misturar por exemplo inteiros, strings, etc. nas listas/dicionários/tuplas). O primeiro item em todos os tipos da disposição é 0. Os números negativos contam da extremidade para o começo, -1 é o último ítem. Funções são objetos de primeira classe e você pode usra referências para apontar para funções.

Listas, tuplas e dicionários
--------------------------------------------------------------------------------

O uso é como segue:

.. sourcecode:: python
  
>>> sample = [1, ["another", "list"], ("a", "tuple")]
>>> mylist = ["List item 1", 2, 3.14]
>>> mylist[0] = "List item 1 again"
>>> mylist[-1] = 3.14
>>> mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
>>> mydict["pi"] = 3.15
>>> mytuple = (1, 2, 3)
>>> myfunction = len
>>> print myfunction(mylist)
3

Sub-listas 
--------------------------------------------------------------------------------

* Delimitando intervalos
* Recortando o fim da lista
* Recortando o início da lista
* Duplicando a lista
* Invertendo a ordem da lista

.. class:: handout

Você pode obter sub-listas usando dois pontos (:). Omitindo o índice do começo supõe o primeiro item, omitindo o índice do fim supõe o último ítem. Os índices negativos contam do último ítem para trás (assim -1 é o último ítem) como abaixo:

Exemplos de Sub-listas 
--------------------------------------------------------------------------------
>>> mylist = ["List item 1", 2, 3.14]
>>> print mylist[:]
['List item 1', 2, 3.1400000000000001]
>>> print mylist[0:2]
['List item 1', 2]
>>> print mylist[-3:-1]
['List item 1', 2]
>>> print mylist[1:]
[2, 3.14]
>>> print mylist[1::-1]
[3.14, 2]

Strings de texto
--------------------------------------------------------------------------------

* Strings de texto são denotadas por **"texto"** ou **'texto'**
* Strings muti-linhas: **'''muitas linhas'''** ou **"""muitas linhas"""** 
* Strings de formatação
* Strings de formatação com dicionários

.. class:: handout

Strings podem ser marcadas por aspas simples ou duplas. As strings multilinhas são circundadas por tres caracteres de aspas simples ou duplas ("""ou '''). O Python suporta Unicode diretamente, usando a sintaxe u"Esta é uma string de texto unicode ". Voce pode usar strings par formatação de valores, você usa o perador % (modulo) e uma tupla. Cada %s é substituído com um item da tupla, começando da esquerda para a direita, e você pode também usar substituições com chaves de dicionário.

Exemplos de strings de texto
--------------------------------------------------------------------------------

>>> print "Nome: %s\nNumero: %d\nAltura: %2.1fm" % (
... 'Poromeno', 3, 1.835)
Nome: Poromeno
Numero: 3
Altura: 1.8m
>>> "Somos os %d %s que falam %s %s %s"%(
... (3,"cavaleiros")+3*('ni',))
'Somos os 3 cavaleiros que falam ni ni ni'
>>> strString = """This is
... a multiline string.""" 
>>> # ATENTAR para o s depois da chave "%(chave)s".
>>> print "Isto %(verbo)s um %(substantivo)s." % {
... "substantivo": "teste", "verbo": "era"}
Isto era um teste.

Comandos de controle do fluxo
--------------------------------------------------------------------------------

* For - for vogal in 'aeiou'
* If - if 4%2 : print 'eepa!'
* Else - else: print 'ufa!'
* While - while False: pass

.. class:: handout

Os comandos de controle do fluxo são *while*, *if* e *for*. Não há comandos para seleção de casos; Use o if para isso. Use *if* para iterar através dos membros de uma lista. Para obter uma lista de números, use a função embutida *range(<número>)*. A sintaxe destas indicações é assim:

Comandos For e If
--------------------------------------------------------------------------------

>>> rangelist = range(10)
>>> print rangelist
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for number in rangelist:
...   # verifica se o número pertence à tupla
...   if number in (3, 4, 7, 9):
...     # "Break" termina sem executar o else
...     break
...   else:
...     # "Continue" inicia uma nova iteração, inócuo aqui
...     continue
... else:
...   # O else do for é opcional, executa não tendo break.
...   pass # O pass é usado para marcar um bloco vazio
...

Elif e While
--------------------------------------------------------------------------------

>>> if rangelist[1] == 2:
...     print "O segundo item (inicia em 0) é 2"
... elif rangelist[1] == 3:
...     print "O terceiro item (inicia em 0) é 3"
... else:
...     print "Seilá"
...  
... while rangelist[1] == 1:
...     pass
...

Funções
--------------------------------------------------------------------------------

* Declaradas com o palavra chave **def**
* Argumentos opcionais - **def func(p, s):**
* Parâmetros por omissão - **def func(p, s=2):**
* Os por omissão são os últimos - **def erro(p=1, s):**
* Na chamada pode-se nomear os parametros
* Chamadas que são equivalentes:
* **func(1,2)**, **func(1)** e **func(seg=2,pri=1)**

.. class:: handout

As funções são declaradas com palavra chave **def**. Argumentos opcionais são colocados na declaração da função após os argumentos imperativos sendo atribuído um valor por omissão. Para argumentos nomeados na chamada, o nome do argumento é atribuído um valor. As funções podem retornar uma tupla (e ao desempacotar a tupla, pode-se eficazmente retornar valores múltiplos). As funções Lambda são  funções ad hoc que são declaradas em um único comando. Os parâmetros são passados por referência, mas os tipos imutáveis (tuples, ints, strings, etc.) não podem ser mudados.

Funções, Exemplo
--------------------------------------------------------------------------------

>>> # arg2 and arg3 são opcionais, têm valores default
>>> # se não for passado (100 and "test", respectivamente).
>>> def myfunction(arg1, arg2 = 100, arg3 = "test"):
...     return arg3, arg2, arg1
... 
>>> ret1, ret2, ret3 = myfunction(
...   "Argument 1", arg3 = "Named argument"
... ) # um comando pode ser quebrado no parêntesis
>>> # Usando "print" com valores múltiplos, lista cada um.
>>> print ret1, ret2, ret3
Named argument 100 Argument 1
>>> # clausura equivalente a def f(x): return x + 1
>>> functionvar = lambda x: x + 1
>>> print functionvar(1)
2

Classes
--------------------------------------------------------------------------------

* Python é orientado a objetos
* Suporta a criação de classes e instâncias
* Suporta herança simples ou múltipla
* Atributos e métodos privados são por convenção
* O compilador reforça fracamente algumas formas privadas
* Uma instância é criada invocando a classe como uma função

.. class:: handout

O Python suporta uma forma de herança múltipla nas classes. As variáveis e os métodos privados podem ser declarados (normalmente é apenas uma convenção, esta não é reforçada pela linguagem) adicionando pelo menos dois underscores à frente e no máximo um como sufixo (por exemplo “__spam”). Atributos de classe e de instância podem ser adicionados dinâmicamente após a criação da classe ou instância

Classes, Atributos e Métodos
--------------------------------------------------------------------------------

* Todos os métodos tem que ter o primeiro parâmetro **self**
* Self não é uma palavra reservada, é uma convenção
* O método **__init__** é invocado quando uma instância é criada
* Normalmente é usado para adicionar atributos de instância
* Todos os membros do objetos devem ser referenciados via self
* Atributos de classe e instância podem ser adicionados a posteriori

.. class:: handout

O construtor de uma instância é invocado pela chamada da classe acrescida dos parâmetros definidos no método **__init__**. O init é invocado loga após a instância ser construída. O método init pode adicionar um conjunto de atributos de instância. Todos estes atributos são prefixados pelo parâmetro **self.** para pertencerem à instância. Todas as invocações de atributos e métodos do objeto tem que ser referenciados via **self**, usando algo como self.xxx, onde xxx é o membro do ojeto que se quer referenciar. Como Python é uma linguagem dinâmica, novos atributos podem ser acrescentados à classe ou a instância, bastando atribuir um valor a ele.

Declaração de Classes
--------------------------------------------------------------------------------
>>> class MyClass:
...   common = 10 # atributo de classe
...   def __init__(self):
...     self.myvariable = 3 # atributo de intância
...   def myfunction(self, arg1, arg2):
...     return self.myvariable
... 
>>> # This is the class instantiation
>>> classinstance = MyClass()
>>> classinstance.myfunction(1, 2)
3

Atributos de Classe e Instância
--------------------------------------------------------------------------------

>>> # This variable is shared by all classes.
... classinstance2 = MyClass()
>>> classinstance.common
10
>>> classinstance2.common
10
>>> # Note how we use the class name
... # instead of the instance.
... MyClass.common = 30
>>> classinstance.common
30
>>> classinstance2.common
30

Atributos Dinâmicos
--------------------------------------------------------------------------------
>>> # This will not update the variable on the class,
... # instead it will create a new one on the class
... # instance and assign the value to that.
... classinstance.common = 10
>>> classinstance.common
10
>>> classinstance2.common
30
>>> MyClass.common = 50
>>> # This has not changed, because "common" is
... # now an instance variable.
... classinstance.common
10
>>> classinstance2.common
50


Exceções
--------------------------------------------------------------------------------

As exceções no Python são capturadas com blocos try-except

>>> def somefunction():
...     try:
...         # Division by zero raises an exception
...         10 / 0
...     except ZeroDivisionError:
...         print "Oops, invalid."
...  
>>> fnExcept()
Oops, invalid.

Importação de módulos
--------------------------------------------------------------------------------

As bibliotecas externas são usadas com a palavra chave **import [libname]**.
Você pode também usar **from [libname] import [funcname]** para funções individuais. Está aqui um exemplo:

>>> import random
>>> from time import clock
>>> 
>>> randomint = random.randint(1, 100)
>>> print randomint
64

Seriação de estruturas de dados
--------------------------------------------------------------------------------

O Python tem uma grande coleção funções embutidas e módulos pré-instalados. Como um exemplo, mostramos o módulo de seriação de estruturas **pickle** (estruturas de dados se convertendo em strings usando a biblioteca do pickle) com entrada e saída em arquivo:

>>> import pickle
>>> mylist = ["This", "is", 4, 13327]
>>> # Abre o arquivo binary.dat para escrita.
>>> myfile = file("binary.dat", "w")
>>> pickle.dump(mylist, myfile)
>>> myfile.close()

Entrada e saída de arquivos
--------------------------------------------------------------------------------

>>> myfile = file(r"text.txt", "w")
>>> myfile.write("This is a sample string")
>>> myfile.close()
>>>  
>>> myfile = file(r"text.txt")
>>> print myfile.read()
This is a sample string
>>> myfile.close()
>>>  
>>> # Abre o arquivo para leitura.
>>> myfile = file(r"binary.dat")
>>> loadedlist = pickle.load(myfile)
>>> myfile.close()
>>> print loadedlist
['This', 'is', 4, 13327]
>>> 

Comparações e Compressão de Listas
--------------------------------------------------------------------------------

* As comparações podem ser encadeadas. 1 < a < 3 certifica-se de que a seja simultaneamente menor que 3 e maior que 1.
* Você pode usar o del suprimir variáveis ou itens nas coleções.
* As compreensões da lista fornecem uma maneira poderosa criar e manipular listas. 
* Consistem em uma expressão seguida por uma clúsula **for** seguida por zero ou mais cláusulas **if** ou **for**

Compressão de Listas - Exemplo
--------------------------------------------------------------------------------

>>> lst1 = [1, 2, 3]
>>> lst2 = [3, 4, 5]
>>> print [x * y for x in lst1 for y in lst2]
[3, 4, 5, 6, 8, 10, 9, 12, 15]
>>> print [x for x in lst1 if 4 > x > 1]
[2, 3]
>>> # Verifica se um item tem uma determinada propriedade
... any(i % 3 for i in [3, 3, 4, 4, 3])
True
>>> # Verifica quantos itens tem uma determinada propriedade
... sum(1 for i in [3, 3, 4, 4, 3] if i == 3)
3
>>> del lst1[0]
>>> print lst1
[2, 3]
>>> del lst1

Referências Globais
--------------------------------------------------------------------------------

* As variáveis globais são declaradas fora das funções e podem ser lidas sem nenhumas declarações especiais, mas se você quiser alterar seu conteúdo, você deve declará-las no começo da função com o palavra chave **global**, se não o Python criará um variável local e tentará usá-la nas atribuições (cuidado com isso, ele é um prendedor pequeno que possa o começar se você não o souber). Por exemplo:

Exemplo de Referências Globais
--------------------------------------------------------------------------------
>>> number = 5
>>>  
>>> def myfunc(): # imprime 5
...   print number
... 
>>> def anotherfunc(): 
...   # gera excessão, number é tratado como local
...   print number
...   number = 3
... 
>>> def yetanotherfunc(): 
...   # este troca corretamente o valor de number global
...   global number
...   number = 3


Epílogo
--------------------------------------------------------------------------------

Este tutorial não pretende ser uma lista exaustiva de todo o (ou mesmo de um subconjunto) Python. O Python tem uma coleção vasta de bibliotecas e de muito mais funcionalidade que você terá que descobrir com outros meios, tais como o excelente livro Mergulhando no Python. Eu espero ter ajudado a compreender melhor o  Python.
