import hashlib

# create s string to hash and print it out

myString = "JOSHUA IS A BITCOIN DEVELOPER!"
print("Your string is: ", myString)

#hash it

myhash = hashlib.sha256(myString.encode())

#print the hashed messaged

print("Your SHA256 hash is: ", myhash.hexdigest())

#make your output deterministic

print("The lenght of your hash is: ", len(myhash.hexdigest()))
