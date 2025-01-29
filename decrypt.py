from Crypto.Cipher import AES
import os

# Nome do arquivo criptografado
file_name = 'clientes.txt.ransomwaretroll'

# Ler o arquivo criptografado
with open(file_name, 'rb') as file:
    file_data = file.read()

# Extrair o nonce (primeiros 8 bytes) e os dados criptografados
nonce = file_data[:8]
ciphertext = file_data[8:]

# Verificar o tamanho do nonce
print(f"Tamanho do nonce extraído: {len(nonce)} bytes")

# Chave usada para criptografia (deve ser a mesma usada na criptografia)
key = b"testeransomwares"  # 16 bytes fixos

# Inicializar o AES no modo CTR com o nonce correto
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

# Descriptografar os dados
decrypted_data = cipher.decrypt(ciphertext)

# Excluir o arquivo criptografado
os.remove(file_name)

# Criar o arquivo original descriptografado
new_file_name = 'clientes.txt'
with open(new_file_name, 'wb') as new_file:
    new_file.write(decrypted_data)

print(f"Arquivo '{file_name}' foi descriptografado como '{new_file_name}'.")


