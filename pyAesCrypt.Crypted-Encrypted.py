import pyAesCrypt

password = input("Enter your password: ")

# encrypt file with password
pyAesCrypt.encryptFile('data.txt', 'data_encrypted.txt.aes', password)
print(f'File data.txt encrypted.')

# decrypt file with password
pyAesCrypt.decryptFile('data_encrypted.txt.aes', 'data_decrypted.txt', password)
print(f'File data_encrypted.txt.aes decrypted.')