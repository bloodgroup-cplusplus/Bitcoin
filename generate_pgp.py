# https://medium.com/@almirx101/pgp-key-pair-generation-and-encryption-and-decryption-examples-in-python-3-a72f56477c22
# Let's go through an example of PGP key pair generation and using the
# keys for encryption and decryption 
# the PGP key generation is different on MACOs compared to Windows. 
# Inorder to generate the PGP key pair on MACOs, you need to have the 
# following installed. 

# GNUPG
# GPA
# python-gnupg module if you plan to generate the keys using Python3

# Install this on MACOs:

# brew install GnuPG
# brew install gpa

# Install Python3 modules for GnuPG:
# pip3 install python-gnupg
# export GPG_TTY = $(tty)

import gnupg
import os


gpg = gnupg.GPG('/usr/local/bin/gpg')
gpg.encoding = 'utf-8'

key_input_data = gpg.gen_key_input(
        name_email = "yourmail",
        passphrase = "your password",
        key_type = "RSA",
        key_length = 4096)


key = gpg.gen_key(key_input_data)


print(key)

