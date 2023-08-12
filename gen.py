import gnupg
import os


class Encrypted_Communication():
    def __init__(self, database):
        self.gpg = gnupg.GPG(homedir='~/.gnupg/')
        self.database=database
        self.gpg.import_keys(open("private.asc", "r").read())
    
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
        self.database.register_client(str(public_key))
        return str(public_key)

    def encrypt_message(self,message, key):
        imported_key = self.gpg.import_keys(key)
        encrypted_data = self.gpg.encrypt(message, imported_key.fingerprints[0])
        return str(encrypted_data)

    def decrypt_message(self, message):
        # Decrypt message
        decrypted_data = self.gpg.decrypt(message)
        
        # Print the complete status message from GnuPG
        print("GnuPG Status Message:", decrypted_data.status)
        
        if decrypted_data.ok:
            return str(decrypted_data)
        else:
            print("Decryption failed:", decrypted_data)
            raise ValueError("Decryption failed")
