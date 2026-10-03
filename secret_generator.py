import secrets
import math
import string

def generate_password(length=16, use_symbols=True, use_digits=True):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = lowercase + uppercase + digits + symbols

    password = [secrets.choice(lowercase),
                secrets.choice(uppercase)]

    if use_digits:
        password.append(secrets.choice(digits))
    if use_symbols:
        password.append(secrets.choice(symbols))


    remaining_len = length - len(password)
    
    for _ in range(remaining_len):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)
    
def generate_hex_token(bytes_length=32):
    return secrets.token_hex(bytes_length)

def generate_urlsafe_token(bytes_length=32):
    return secrets.token_urlsafe(bytes_length)

def calculate_entropy(password):
    if not password:
        return 0.0

    pool_size = 0

    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += 32

    if pool_size == 0:
        return 0.0

    return len(password) * math.log2(pool_size)

if __name__ == "__main__":
    pwd = generate_password(length=16)
    entropy = calculate_entropy(pwd)
    print(f"Generated Password : {pwd}")
    print(f"Calculated Entropy : {entropy:.2f} bits")
    print(f"Hex Token          : {generate_hex_token()}")
    print(f"URL-Safe Token     : {generate_urlsafe_token()}")