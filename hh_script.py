from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define the FTP server settings
FTP_HOST = '127.0.0.1'  # FTP server host address
FTP_PORT = 2121  # FTP server port
FTP_USER = 'username'  # FTP username
FTP_PASSWORD = 'password'  # FTP password

# Define the FTP server handler
class MyHandler(FTPHandler):
    def on_file_received(self, file):
        # Process the received file
        print(f"Received file: {file}")

# Configure the FTP server
def configure_ftp_server():
    # Create a dummy authorizer for managing users
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, '.', perm='elradfmwMT')

    # Instantiate FTP handler class
    handler = MyHandler
    handler.authorizer = authorizer

    # Configure the FTP server
    server = FTPServer((FTP_HOST, FTP_PORT), handler)
    server.serve_forever()

if __name__ == '__main__':
    configure_ftp_server()