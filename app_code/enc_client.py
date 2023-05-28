import hashlib
import socket
import ssl
import re
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import main_win

context = ssl.create_default_context()

# Set the context to not verify the server's SSL/TLS certificate
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

class myClient():
    client_socket = None
    public_key = None

    def handle_res(self, res, command):
        splitted_res = res.split()
        if splitted_res[0] == command + "_ans" and splitted_res[1] == "True":
            return splitted_res[2]
        else:
            return None

    def run_app(self):
        app = QtWidgets.QApplication(sys.argv)
        Window = QtWidgets.QMainWindow()
        ui = main_win.Ui_MainWindow()
        ui.setupUi(Window, self)
        Window.show()
        sys.exit(app.exec_())

    def login(self, username, password):
        password = hashlib.md5(password.encode()).hexdigest()
        message = 'login\r\n' + username + '\r\n' + password
       # encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(message.encode())
        res = self.client_socket.recv(1024)
        return res.decode()

    def get_specific_patient(self, patient_id):
        message = 'get_specific_patient\r\n' + patient_id
        #encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(message.encode())
        res = self.client_socket.recv(1024)
        res = res.decode()
        spllited_res = res.splitlines()
        if len( spllited_res) > 0:
            return spllited_res[1]
        else:
            return ''
    def get_patients_list(self, doctor_id):
        message = 'get_patients_list\r\n' + doctor_id
        #encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(message.encode())
        res = ''
        while True:
            data = self.client_socket.recv(1024)
            data = data.decode()
            res += data
            if len(data) < 1024:
                break
        #res = self.client_socket.recv(1024)
        spllited_res = res.splitlines()
        return spllited_res[1:]

    def run(self):
        self.client_socket = socket.socket()
        host = '127.0.0.1'
        port = 8080
        print('Waiting for connection response')
        try:
            self.client_socket.connect((host, port))
            self.client_socket = context.wrap_socket(self.client_socket, server_hostname=host)
        except socket.error as e:
            print(str(e))

        self.run_app()



    def sign_up(self, name, email, username, password):
        password = hashlib.md5(password.encode()).hexdigest()
        message = 'sign_up\r\n' + name + '\r\n' + email + '\r\n' + username + '\r\n' + password
        #encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(message.encode())
        res = self.client_socket.recv(1024)

        return res.decode()

    def send_photo(self, photo_name, img_bytes, ID):
        #at first send the name of command and the name of the photo
        message = 'pic\r\n' + photo_name + "\r\n" + ID
        #encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(message.encode())


        # f = open(photo_path, "rb")
        # data = image.read(1024)
        # while data:
        #     #encrypted_message = self.encrypt_msg(data,True)
        #     if self.client_socket.send(data):
        #         # print "sending ..."
        #         data = image.read(1024)
        #     else:
        #         break

        # Send the image bytes in a loop to ensure that all the data is sent
        total_sent = 0
        while total_sent < len(img_bytes):
            sent = self.client_socket.send(img_bytes[total_sent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_sent += sent
        res = self.client_socket.recv(1024)

    def send_patient(self, full_name, ID, email, gender, birth_date, case_description, visit_date,  chance, doctor_id):
        message = 'add_patient\r\n' + full_name + '\r\n' + ID + '\r\n' + email + '\r\n' + gender + '\r\n' + birth_date + '\r\n'+ case_description + '\r\n' + visit_date +'\r\n' +doctor_id
        if chance != '':
            message = message + '\r\n' + chance

        #encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(message.encode())
        res = self.client_socket.recv(1024)
        return res
    def check_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # pass the regular expression
        # and the string into the fullmatch() method
        if (re.fullmatch(regex, email)):
            return True
        else:
            return False
if __name__ == '__main__':

    theClinet = myClient()
    #theClinet.setMessage("noo")
    theClinet.run()
