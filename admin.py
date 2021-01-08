import bcrypt

password = b"super secret password"

# Hash password
hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))

# Check to see if user has got the correct password
if bcrypt.checkpw(password, hashed):
    print("right password")
else:
    print("wrong password")
