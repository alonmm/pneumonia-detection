import os.path
import threading as th
import socket

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from queue import Queue
import db
import hashlib
def insert_db(conn_q):
    db.build_DB()
    if conn_q.empty() is False:
        data = conn_q.get()
        print(data[0],data[1])
        bret = db.insert_to_DB(data[0],data[1],data[2], data[3])
        return bret
    #time.sleep(0.05)

def handle_pic(data, client_socket):
    photo_name =  data[0]
    f = open(photo_name, 'wb')
    while True:
        data = client_socket.recv(1024)
        f.write(data)
        if len(data) < 1024:
            f.write(data)
            break
    photo_path = os.path.join(r"D:\Projects\finale", "pneumonia_3.jpeg")
    # chance = sendCurl.send_curl(photo_path)
    # print(chance)


def handle_login_msg(msg):
    username = msg[0]
    password = msg[1]
    return username, password

def handle_sign_up_msg(msg):
    name = msg[0]
    email = msg[1]
    username = msg[2]
    password = msg[3]
    return name, email, username, password

def handle_add_patient_msg(msg):
    full_name = msg[0]
    ID = msg[1]
    email = msg[2]
    date = msg[3]
    case_description = msg[4]
    doctor_id = msg[5]
    if len(msg) < 7:
        return full_name, ID, email, date, case_description, doctor_id, None
    else:
        pneu_chance = msg[6]
        return full_name, ID, email, date, case_description, doctor_id, pneu_chance

def handle_client(client_socket, client_address, conn_q):
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Serialize public key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Send public key to client
    client_socket.send(public_pem)
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            # Decrypt message using private key
            plaintext = private_key.decrypt(
                encrypted_message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            data = plaintext.decode()
            print(f'[*] Received message from {client_address}: {data}')
            split_data = data.splitlines()
            bret = 0
            #handle with login requests
            if split_data[0] == 'login':
                username, password = handle_login_msg(split_data[1:])
                password = hashlib.md5(password.encode()).hexdigest()
                #conn_q.put((username, password))
                bret, unique_id = db.find_username_and_password(username, password)
                if bret:
                    res = str(bret) + "\r\n" + unique_id
                else:
                    res = str(bret)

            #handle with sign up requests
            if split_data[0] == 'sign_up':
                name, email, username, password = handle_sign_up_msg(split_data[1:])
                password = hashlib.md5(password.encode()).hexdigest()
                #conn_q.put((name, email, username, password))
                bret, unique_id = db.add_user(name, email, username, password)
                if bret:
                    res = str(bret) + "\r\n" + unique_id
                else:
                    res = str(bret)

            if split_data[0] == 'pic':
                handle_pic(split_data[1:], client_socket)

            if split_data[0] == 'add_patient':
                full_name, ID, email, date, case_description, doctor_id, pneu_chance = handle_add_patient_msg(split_data[1:])
                if pneu_chance is None:
                    bret = db.add_patient(full_name, ID, email, date, case_description, doctor_id)
                else:
                    bret = db.add_patient_with_photo(full_name, ID, email, date, case_description, doctor_id, pneu_chance)
                if bret:
                    res = str(bret) + "\r\n" + username
                else:
                    res = str(bret)

            if split_data[0] == 'get_patients_list':
                patient_list = db.get_patients_list(split_data[1])
                res = patient_list

            if split_data[0] == 'get_specific_patient':
                patient = db.get_specific_patient(split_data[1])
                res = patient

            print(bret)
            # Send encrypted message to client
            response = split_data[0] +"_ans\r\n" + res
            if not encrypted_message:
                break
            client_socket.sendall(str.encode(response))
        except Exception as e:
            None
    client_socket.close()

def run():
    host = '127.0.0.1'
    port = 8080
    ThreadCount = 0
    conn_q = Queue()

    ServerSideSocket = socket.socket()

    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print('Socket is listening..')
    ServerSideSocket.listen(1)
    b = th.Thread(target=db.build_DB())
    b.start()
    while True:
        client_socket, client_address = ServerSideSocket.accept()
        print(f'[*] Accepted connection from {client_address}')
        a = th.Thread(target=handle_client, args=(client_socket, client_address, conn_q, ))
        a.start()
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()

if __name__ == '__main__':
    run()