import os
import pyaes

nome_arquivo = "teste.txt.ransomwaretroll"
arquivo = open(nome_arquivo, "rb")
dados_arquivo = arquivo.read()
arquivo.close()

chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)
dado_descriptografado = aes.decrypt(dados_arquivo)

os.remove(nome_arquivo)

novo_arquivo = "teste.txt"
novo_arquivo = open(f'{novo_arquivo}', "wb")
novo_arquivo.write(dado_descriptografado)
novo_arquivo.close()
