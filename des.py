from Crypto.Cipher import DES
from Crypto import Random
import sys

key = b'8bytekey'
cipher = DES.new(key, DES.MODE_ECB) 

while(True):

 print '~~~~~DES File Encryption~~~~~'
 print '1. Encrypt a plaintext file'
 print '2. Decrypt a ciphertext file'
 print '0. Exit program'

 selection = raw_input("Please select an option: ")
 if selection == '0':
  print 'Exiting program. Bye!'
  sys.exit()

 elif selection == '1':
  filein = raw_input("Please enter name of plaintext file to encrypt (eg. plain.txt): ")
  fileout = raw_input("Please enter name of file to create to store ciphertext (eg. cipher.txt): ")
  print "Encrypting file: " + filein + ". Please make sure it exists. Press any key to continue..."
  raw_input()

  f = open(filein, 'r')
  text = f.read()
  print "Text in file " + filein + ": " + text 
  f.close()

  mod = len(text) % 8
  pad = 8 - mod
  text = text + pad*' '

  enc = cipher.encrypt(text)
  print "Encrypted text in file " + fileout + ": " + enc

  f = open(fileout, 'w')
  f.write(enc)
  f.close()

  raw_input("Press any key to continue...")

 elif selection == '2':
  filein = raw_input("Please enter name of file containing cyphertext (eg. cypher.txt): ")
  raw_input("Decrypting file " + filein + ". Press any key to continue...")
  f = open(filein, 'r')
  ctext = f.read()
  f.close()
  print "Ciphertext in file " + filein + ": " + ctext 
  dec = cipher.decrypt(ctext)
  print "Decrypted text: " + dec  
  raw_input("Press any key to continue...") 
