import bcrypt # type: ignore

def encrypt_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

user_password = input("Enter the password to encrypt: ")
encrypted_password = encrypt_password(user_password)
print("Encrypted Password: ", encrypted_password)

check_password = input("Re-enter the password to verify: ")
is_valid = verify_password(check_password, encrypted_password)

if is_valid:
    print("Password is valid.")
else:
    print("Invalid Password!!")