=======================================================
Testando Programas Python
=======================================================

.. footer:: LABASE - NCE

.. class:: right big

   | *Lívia Monnerat*
   | liviamc@posgrad.nce.ufrj.br
   | http://labase.nce.ufrj.br/

.. class:: small

   ©2007, licensed under a `Creative Commons
   Attribution/Share-Alike (BY-SA) license
   <http://creativecommons.org/licenses/by-sa/3.0/>`__.

Agenda
--------------------------------------------------------------------------------

* Desenvolvimento Guiado a Testes
* Teste Unitário com Doctest, Unittest, Py.test
* Teste mimético com Pmock, Monkey Patch
* Teste funcional com Metatest
* Teste de aceitação com PyFIT
* Teste de aceitação com Selênio (opcional)

Desenvolvimento Guiado a Testes
--------------------------------------------------------------------------------

O desenvolvimento guiado a testes é a repetição deste ciclo:

* Escreva um teste
* Verifique que ele falhe
* Faça compilar
* Faça passar
* Refatore o código
* Refatore e elabore o teste
* Limpe o código e repita

.. class:: handout

* http://us.pycon.org/TX2007/TestingToolsPanel
* http://www.onlamp.com/pub/a/python/2004/12/02/tdd_pyunit.html
* http://dirtsimple.org/2005/02/making-it-from-scratch-with-tdd-and.html
* http://powertwenty.com/kpd/downloads/TestDrivenDevelopmentInPython.pdf
* http://www.python.org/pycon/2005/papers/10/

Desenvolvendo Centrado em Testes
--------------------------------------------------------------------------------

* Testes unitários - Limitando o êrro dentro da unidade
* Testes funcionais - integrando todo o software
* Enemy Testing - validando as API's para se proteger
* Teste de aceitação - atendendo ao cliente

.. note:: O teste de inimigo evita que se perca horas por conta dos erros dos outros.

.. note:: O teste deve ser feito para todas as situações e chamadas feitas.

.. class:: handout

* http://groboutils.sourceforge.net/testing-junit/art_eut.html
* http://caseysoftware.com/files/presentations/20050809/Open_Source_Integrations.pdf

Teste Unitário com Doctest
--------------------------------------------------------------------------------

Os testes são criados como documentação das classes e métodos

* Uma versão compilável de programação literária
* Não tem api, o teste é uma simulação de uma sessão interativa no console
* invoca-se um conjunto de operações no console simulado
* descreve-se o resultado esperado como seria a saída do console

.. class:: handout

* http://dirtsimple.org/2004/11/stream-of-consciousness-testing.html
* http://www.python.org/pycon/dc2004/papers/4/PyCon2004DocTestUnit.pdf
* http://agiletesting.blogspot.com/2005/01/python-unit-testing-part-2-doctest.html
* http://en.wikipedia.org/wiki/Doctest

Exemplo de Docutil
--------------------------------------------------------------------------------

código exemplo::

  # coding=UTF-8
  ''' 
  Esta função decodifica zenit polar intercambiando
  as letras de zenit com polar
  >>> decodezp('zenitpolar')
  'polarzenit'
  '''    
  zp=" "*97+"ibcdofghajknmlezqtsruvwxyp"+" "*133
  def decodezp(cifra):
    return cifra.translate(zp)
  
  if __name__ == "__main__":
      import doctest; doctest.testmod()

Teste Unitário com Unittest
--------------------------------------------------------------------------------

O Unittest usa o modelo de teste clássico criado por Kent Beck

* Criação de classes de teste
* Cada método é um teste
* A classe de teste herda do cado de teste
* O caso de teste provê métodos utilitários (assertivas)

.. class:: handout

* http://pyunit.sourceforge.net/pyunit.html
* http://agiletesting.blogspot.com/2005/01/python-unit-testing-part-1-unittest.html



Teste Unitário com Py.test
--------------------------------------------------------------------------------

Engenho aperfeiçoado de testes

* Não tem api, todos os testes são marcados com prefixo test\_
* Classes de teste são prefixadas com Test\_
* testes são guardados em arquivos que começam com test\_
* A preparação do do teste é feita pela prefixação setup\_
 
.. class:: handout

* http://agiletesting.blogspot.com/2005/01/python-unit-testing-part-3-pytest-tool.html

Teste mimético com Pmock
--------------------------------------------------------------------------------

Para se isolar um teste unitário é preciso que outras unidades não operem

* Todas as dependências devem ser substituídas por miméticos
* Os miméticos imitam a interface das unidades substituídas
* Observam as invocações que são feitas às unidades auxiliares
* são treinados para reconhecer as sequências corretas

.. class:: handout

* http://pmock.sourceforge.net/
* http://www.jmock.org/

Teste mimético com Monkey Patch
--------------------------------------------------------------------------------

Evitando que módulos do importados interfiram no teste unitário

* Monkey Patch: redefinindo módulos a tempo de execução
* O Python permite sobrescrever as definições dos módulos (patch)
* O módulo pode ser substituido por um mock ou stub
* Mock : as chamadas são registradas para efeito de teste
* Stub: as chamadas são descartadas (pass)

.. class:: handout


* http://psychicorigami.com/2007/09/20/monkey-patching-pythons-smtp-lib-for-unit-testing/

Teste funcional com Metatest
--------------------------------------------------------------------------------

Facilita a construção de testes com variações de valores

* Cada comando registra como um teste
* Não é ncecessario criar classes funções ou métodos
* cada teste é uma comparação
* Um novo parâmetro é acrescentado em todas as funções e métodos
* Este parâmetro discrimina o valor esperado resultante

.. class:: handout

* http://metatest.sourceforge.net/

Teste de aceitação com PyFIT
--------------------------------------------------------------------------------

Os testes são construídos com uma planilha

* A planilha descreve os valores de entrada e os respectivos esperados
* Quando a planilha é executada os corretos ficam verdes
* Os incorretos ficam vermelhos e descrevem a discrepância acontecida
* Os teste são descritos dentro de um site wiki
* As planilhas são definidas por uma notação especial nas tabelas

.. class:: handout

* http://agile.unisonis.com/PyFitTutorial.html
* http://agiletesting.blogspot.com/2004/11/writing-fitnesse-tests-in-python.html

Teste de aceitação com Selênio (op)
--------------------------------------------------------------------------------

O teste é feito diretamente contra o website

* Semelhante ao Fit, os testes são descritos como uma tabela

.. class:: handout

* http://agiletesting.blogspot.com/2005/03/web-app-testing-with-python-part-2.html
* http://openqa.org/selenium-rc/
* http://joker.linuxstuff.pl/documentation/make_selenium
* http://wiki.javascud.org/display/SEL/Selenium+Remote+Control+-+Python
* http://johnmudd.infogami.com/blog/5be6
* http://www.bluetwanger.de/blog/2006/09/14/functional-unit-testing-for-web-applications-selenium-remote-control/

Conclusão
--------------------------------------------------------------------------------

* O teste como processo de desenvolvimento
* O teste como uma documentação confiável, garantida pela execução correta
* O modelo de documentação através de exemplos de uso
* A primazia da qualidade do software


