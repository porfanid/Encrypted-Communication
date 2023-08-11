import gnupg
import os


class Encrypted_Communication():
    def __init__(self, database):
        self.gpg = gnupg.GPG()
        self.database=database
    
    def generate_key(self, email):
        if os.path.exists("keys/personal.asc"):
            return str(open("keys/personal.asc", "r").read())
        input_data = self.gpg.gen_key_input(
            name_email=email)
        key = self.gpg.gen_key(input_data).fingerprint
        public_key = self.gpg.export_keys(key)
        with open("keys/personal.asc", "w") as public_key_file:
            public_key_file.write(public_key)
        try:
            private_key = self.gpg.export_keys(key, True)
            with open("private.asc", "w") as public_key_file:
                public_key_file.write(private_key)
        except Exception as e:
            pass
        self.database.register_client(str(public_key), email)
        return str(public_key)

    def encrypt_message(self,message, email):
        encrypted_data = self.gpg.encrypt(message, [email])
        return str(encrypted_data)

    def decrypt_message(self, message):
        decrypted_data = self.gpg.decrypt(
            message)
        return str(decrypted_data)