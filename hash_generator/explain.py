import hashlib

plain_text = input("Enter text to hash: ")

encoded_text = plain_text.encode('utf-8')


hash_md5 = hashlib.md5(encoded_text).hexdigest()

print(hash_md5)