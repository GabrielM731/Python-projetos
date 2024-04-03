
"""
O \r\n faz uma quebra de linha
CRLF = \r\n - Esta padrão de quebra de linha é dp Windows

o \n é um padrão unix
"""
print(12, 34, sep="-", end='\r\n')    
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')