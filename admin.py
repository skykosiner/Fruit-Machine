from sqlalchemy import create_engine
import bcrypt

# # Connect to db
# engine = create_engine("")

# print(engine)

password = b"secret password"

# Hash passwordxxc
hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
print(hashed)

# Check to see if user has got the correct password
if bcrypt.checkpw(password, hashed):
    print("right password")
else:
    print("wrong password")
