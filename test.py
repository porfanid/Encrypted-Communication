from send_to_server import Database
test_database=Database("test@orfanidis.net.gr")
from gen import Encrypted_Communication
client=Encrypted_Communication(test_database)
key=client.generate_key("test@orfanidis.net.gr")
message = client.encrypt_message("hello", key)
test_database.send_message("pavlos@orfanidis.net.gr", message)