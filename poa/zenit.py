# coding=UTF-8
'''
Esta função decodifica zenit polar intercambiando as letras de zenit com polar
>>> decodezp('zenitpolar')
'polarzenit'
'''
def decodezp(cifra):
  zp="""                                 !"#$%&\'()*+,-./0123456789:;<=>?@IBCDOFGHAJKNMLEZQTSRUVWXYP[\\]^_`ibcdofghajknmlezqtsruvwxyp{|}~                                                                                                                                 """
  return cifra.translate(zp)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

