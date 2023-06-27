import ascon2

my_key = bytes.fromhex('00456c6c616e61206427416c2d466172') # Ellana d'Al-Far <333
my_nonce = bytes.fromhex('00000000000000000000000000000000')
secret_message = bytes.fromhex('ac6679386ffcc3f82d6fec9556202a1be26b8af8eecab98783d08235bfca263793b61997244e785f5cf96e419a23f9b29137d820aab766ce986092180f1f5a690dc7767ef1df76e13315a5c8b04fb782')
associated_data = bytes.fromhex('80400c0600000000')

# Decipher the ASCON message
# CODE HERE
print(type(my_key), type(my_nonce), type(secret_message), type(associated_data))
print(len(my_key), len(my_nonce), len(secret_message), len(associated_data))
text = ascon2.ascon_decrypt(my_key, my_nonce, associated_data, secret_message)
print(text)

# 404CTF{V3r5_l4_lum1\xe8r3.} -> 404CTF{V3r5_l4_lum1èr3.}