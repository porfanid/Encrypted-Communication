from send_to_server import Database
test_database=Database()
from gen import Encrypted_Communication
client=Encrypted_Communication(test_database)
key=client.generate_key("test@orfanidis.net.gr")
print(client.encrypt_message("hello", key))