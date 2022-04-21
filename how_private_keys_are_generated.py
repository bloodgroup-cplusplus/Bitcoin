import hashlib
import sys
import base58
# get the message
message = "AofidowXhk&)):@:@9727929Hcks&&&(nkhgiowiwj919283$’@bnwkiHhVjKihUNnkllswiwi9@/93938’bbndkk!?,(ikjqlwlw188020$n€¥¥Hbnk"

#encode the message
message = message.encode()
# generate a sha256 hash 
sha_256_hash = hashlib.sha256(message).hexdigest()

#see how big of a number it is in decimal 

number_in_decimal = int(sha_256_hash, 16)

print(number_in_decimal)


# verify if number lies in range 1 and 2**256 (2 to the power 256)


print("YES the number is in the required range" if number_in_decimal >=1 and number_in_decimal <= 2**256 else "NO it is not in the range")


# add version number 
# In bitcoin every private key on the mainnet begins with "5". This makes it easy to identify a private key 

#Lets add 80 to the beginning of our hexadecimal so that private key starts with 5

sha_256_hash_plus_eighty = hex(int("80",16) + int(sha_256_hash,16))

#this is the final added number 
print("this is our 80 + hexadecimal")
print(sha_256_hash_plus_eighty)
sha_256_hash_plus_eighty = "80"+sha_256_hash_plus_eighty[2:]
print(sha_256_hash_plus_eighty)
#sys.exit()

# Add 32 bit checksum . Typing our private key is too large. Adding a checksum allows us to 
#detect any typing errors when using private key. To add a checksum get the double SHA256 hash of
# our new hexadecimal number 

# Lets encode our string before generating the first hash 
sha_256_hash_plus_eighty = sha_256_hash_plus_eighty.encode()
#the first hash 
first_hash_of_the_new_hexadecimal = hashlib.sha256(sha_256_hash_plus_eighty).hexdigest()
print("First hash is given by")
print(first_hash_of_the_new_hexadecimal)
#Lets encode the first hash as well
first_hash_of_the_new_hexadecimal= first_hash_of_the_new_hexadecimal.encode()
#the second hash of first hash 

double_hash = hashlib.sha256(first_hash_of_the_new_hexadecimal).hexdigest()

#Here's the hash of the first hash we generated above 
print(double_hash)

#Now we take the first 8 characters, 32 bits, of the double hash and add it to end our new hexadecimal above .
first_eight_characters_of_double_hash =  double_hash[:8]

#print(first_eight_characters_of_double_hash)

#Encode the first eight characters of the double hash before generating it's double hash 

#first_eight_characters_of_double_hash = first_eight_characters_of_double_hash.encode()

#first_hash_of_the_first_eight_characters_of_double_hash = hashlib.sha256(first_eight_characters_of_double_hash).hexdigest()

# Encode the first_hash_of_the_first_eight_characters_of_double_hash 

#first_hash_of_the_first_eight_characters_of_double_hash = first_hash_of_the_first_eight_characters_of_double_hash.encode()

# Generate the second_hash_of_the_first_eight_characters_of_double_hash 
#final_hash = hashlib.sha256(first_hash_of_the_first_eight_characters_of_double_hash).hexdigest()

#Let's print the final decimal 
#print(final_hash)

# Let's add the final_hash to our double hash 
final_hash = hex(int(double_hash,16) + int(first_eight_characters_of_double_hash,16))

print(final_hash)
#Let's convert the new hexadecimal to base 58 to further prevent typing errors 

#convert final_hash to base 58 

if final_hash[:2] in ["0X","0x"]:
    final_hash = "41"+final_hash[2:]
bytes_str = bytes.fromhex(final_hash)
base58_private_key = base58.b58encode_check(bytes_str)
print(base58_private_key.decode("UTF-8"))


