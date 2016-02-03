from Crypto.Cipher import DES
from Crypto import Random

key = 'this key'
cipher = DES.new(key, DES.MODE_ECB)
plaintext = raw_input('Enter your message (must be multiple of 8 bytes): ') 
msg = cipher.encrypt(plaintext) 
print 'Encrypted message: ', msg 
dec = cipher.decrypt(msg)
print 'Decrypted message: ', dec
