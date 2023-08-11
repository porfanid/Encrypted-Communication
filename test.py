from send_to_server import Database


test_database=Database()
from gen import Encrypted_Communication

client=Encrypted_Communication(test_database)

client.generate_key("pavlos@orfanidis.net.gr")