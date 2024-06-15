import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Load passwords
    with open('top-10000-passwords.txt', 'r') as file:
        passwords = [line.strip() for line in file]

    # If salts are to be used
    if use_salts:
        with open('known-salts.txt', 'r') as file:
            salts = [line.strip() for line in file]
    else:
        salts = []

    # Helper function to compute SHA-1 hash
    def sha1_hash(string):
        return hashlib.sha1(string.encode()).hexdigest()

    # Check passwords without salts
    for password in passwords:
        if sha1_hash(password) == hash:
            return password

    # If salts are used, check passwords with each salt
    if use_salts:
        for salt in salts:
            for password in passwords:
                if sha1_hash(salt + password) == hash or sha1_hash(password + salt) == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"