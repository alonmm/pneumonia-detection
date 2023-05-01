import socket
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import appDate1



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
        ui = appDate1.Ui_MainWindow()
        ui.setupUi(Window, self)
        Window.show()
        sys.exit(app.exec_())

    def login(self, username, password):
        message = 'login\r\n' + username + '\r\n' + password
        encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(encrypted_message)
        res = self.client_socket.recv(1024)
        return res.decode()

    def get_specific_patient(self, patient_id):
        message = 'get_specific_patient\r\n' + patient_id
        encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(encrypted_message)
        res = self.client_socket.recv(1024)
        res = res.decode()
        spllited_res = res.splitlines()
        return spllited_res[1]
    def get_patients_list(self, doctor_id):
        message = 'get_patients_list\r\n' + doctor_id
        encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(encrypted_message)
        res = self.client_socket.recv(1024)
        res = res.decode()
        spllited_res = res.splitlines()
        return spllited_res[1:]

    def encrypt_msg(self, msg, is_photo):
        if not is_photo:
            msg = bytes(msg, 'utf-8')
        encrypted_message = self.public_key.encrypt(
            msg,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def run(self):
        self.client_socket = socket.socket()
        host = '127.0.0.1'
        port = 8080
        print('Waiting for connection response')
        try:
            self.client_socket.connect((host, port))
        except socket.error as e:
            print(str(e))

        # Receive public key from server
        public_pem = self.client_socket.recv(1024)
        # Deserialize public key
        self.public_key = serialization.load_pem_public_key(
            public_pem,
            backend=default_backend()
        )

        self.run_app()


    def sign_up(self, name, email, username, password):
        message = 'sign_up\r\n' + name + '\r\n' + email + '\r\n' + username + '\r\n' + password
        encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(encrypted_message)
        res = self.client_socket.recv(1024)

        return res.decode()

    def send_photo(self, photo_path):
        #at first send the name of command and the name of the photo
        splitted_path = photo_path.split("/")
        photo_name = splitted_path[-1]
        message = 'pic\r\n' + photo_name
        encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(encrypted_message)


        f = open(photo_path, "rb")
        data = f.read(1024)
        while data:
            #encrypted_message = self.encrypt_msg(data,True)
            if self.client_socket.send(data):
                # print "sending ..."
                data = f.read(1024)
            else:
                break
        res = self.client_socket.recv(1024)

    def send_patient(self, full_name, ID, email, date, case_description, chance, doctor_id):
        message = 'add_patient\r\n' + full_name + '\r\n' + ID + '\r\n' + email + '\r\n' + date + '\r\n' + case_description + '\r\n' + doctor_id
        if chance != '':
            message = message + '\r\n' + chance

        encrypted_message = self.encrypt_msg(message, False)
        self.client_socket.send(encrypted_message)
        res = self.client_socket.recv(1024)
        return res
if __name__ == '__main__':
    theClinet = myClient()
    #theClinet.setMessage("noo")
    theClinet.run()
