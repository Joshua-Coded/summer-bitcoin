from ecdsa import SigningKey, SECP256k1
'''
 we can't generate or verify a message without some keys!
let's generate our private key '''

sk = SigningKey.generate(curve=SECP256k1)
print(sk)

'''
and our public, or verifying key '''

vk = sk.verifying_key
print(vk)

''' WE WILL NEED A MESSAGE TO SIGN '''

signature = sk.sign(b"Not your keys, not your coins!")
print(signature)

''' since we have all the component we need to validate the signature! we have:

1. the signature
2. the message
3. the public or verifying key

'''

''' let's put these components together and see if we have produced a valid signature'''

assert vk.verify(signature, b"Not your keys, not your coins!")

print("if your script runs to this point without error, congrats, you successfully validated the signature!")
