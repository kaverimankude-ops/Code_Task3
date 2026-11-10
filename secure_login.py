import hashlib
import hmac

# Secure password hash and salt
SALT = bytes.fromhex("a1b2c3d4e5f60718293a4b5c6d7e8f90")

PASSWORD_HASH = bytes.fromhex(
    "28f13e32486c93011aeaef0959fcc8ffab26ce1cfb41a5f2e4065263807038ee"
)

# Maximum login attempts
MAX_ATTEMPTS = 3

for attempt in range(MAX_ATTEMPTS):

    username = input("Enter username: ")
    password = input("Enter password: ")

    entered_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        SALT,
        200000
    )

    if username == "admin" and hmac.compare_digest(
        entered_hash, PASSWORD_HASH
    ):
        print("Login Successful!")
        break

    else:
        print("Invalid username or password!")

else:
    print("Account locked. Too many attempts.")