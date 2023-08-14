import gnupg
import os


class Encrypted_Communication():
    def __init__(self, database):
        self.gpg = gnupg.GPG(homedir='~/.gnupg/', options=['--pinentry-mode loopback'])
        self.database=database
        
        
    def generate_key(self, email):
        if os.path.exists("../keys/personal.asc"):
            return str(open("../keys/personal.asc", "r").read())
        input_data = self.gpg.gen_key_input(
            key_type="RSA",         # Key type (RSA, DSA, etc.)
            key_length=2048,        # Key length (bits)
            name_email=email,       # Email address associated with the key
            passphrase="<PASSWORD>",  # Passphrase for the key
        )
        key = self.gpg.gen_key(input_data)
        print("hello", key.stderr)
        public_key = self.gpg.export_keys(key, False)
        with open("../keys/personal.asc", "w") as public_key_file:
            public_key_file.write(public_key)
        try:
            private_key = self.gpg.export_keys(key, True)
            print("Private key is:")
            print(private_key)
            with open("../private.asc", "w") as public_key_file:
                public_key_file.write(private_key)
        except Exception as e:
            pass
        self.database.register_client(str(public_key), email)
        return str(public_key)

    def encrypt_message(self,message, key):
        imported_key = self.gpg.import_keys(key)
        encrypted_data = self.gpg.encrypt(message, imported_key.fingerprints[0])
        return str(encrypted_data)

    def decrypt_message(self, message):
        decrypted_data = None
        try:
            key = self.gpg.import_keys(open("../private.asc", "r").read())
            # Decrypt message
            decrypted_data = self.gpg.decrypt(message, passphrase=key)
            return str(decrypted_data)
        except Exception as e:
            # Handle other exceptions
            print("An error occurred:", e)
            return decrypted_data


