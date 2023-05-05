import hashlib

dictionary = open("dictionary.txt", "rb").readlines()
hashes = open("hashes.txt", "rb").readlines()

start = input("Press enter to start")

for password in dictionary:
    password = password.replace(b"\r", b"")
    password = password.replace(b"\n", b"")
    for algorithm in hashlib.algorithms_guaranteed:
        hashingAlgorithm = getattr(hashlib, algorithm)
        if algorithm != "shake_128" and algorithm != "shake_256":
            hashedPassword = hashingAlgorithm(password).hexdigest().encode() 
            for hash in hashes:
                hash = hash.replace(b"\n", b"")
                hash = hash.replace(b"\r", b"")
                if hash == hashedPassword:
                    print(password.decode() + " = " + hash.decode() + " using " + algorithm)