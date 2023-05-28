
import ssl
import threading as th
import socket
from queue import Queue
import db
certfile=r"localhost.pem"
cafile = r"cacert.pem"
purpose = ssl.Purpose.CLIENT_AUTH
context = ssl.create_default_context(purpose, cafile=cafile)
context.load_cert_chain(certfile)
def insert_db(conn_q):
    db.build_DB()
    if conn_q.empty() is False:
        data = conn_q.get()
        print(data[0],data[1])
        bret = db.insert_to_DB(data[0],data[1],data[2], data[3])
        return bret
    #time.sleep(0.05)

def handle_pic(spllited_data, client_socket):
    photo_name = spllited_data[0]
    # while True:
    #     data = client_socket.recv(1024)
    #     f.write(data)
    #     if len(data) < 1024:
    #         f.write(data)
    #         break
    # photo_path = os.path.join(r"D:\Projects\finale", "pneumonia_3.jpeg")
    img_bytes = b''
    while True:
        data = client_socket.recv(1024)
        img_bytes += data
        if len(data) < 1024:
            img_bytes += data
            break

    # with client_socket:
    #     img_bytes = b''
    #     while True:
    #         data = client_socket.recv(4096)
    #         if not data:
    #             break
    #         img_bytes += data
    doctor_id = spllited_data[1]
    return photo_name, doctor_id, img_bytes


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
    gender = msg[3]
    birth_date = msg[4]
    case_description = msg[5]
    visit_date = msg[6]
    doctor_id = msg[7]
    if len(msg) < 9:
        return full_name, ID, email, gender, birth_date, case_description, visit_date, doctor_id, None
    else:
        pneu_chance = msg[8]
        return full_name, ID, email, gender, birth_date, case_description, visit_date, doctor_id, pneu_chance

def handle_client(client_socket, client_address, conn_q):
    while True:
        try:
            data = client_socket.recv(1024)
            data = data.decode()
            print(f'[*] Received message from {client_address}: {data}')
            split_data = data.splitlines()
            bret = 0
            #handle with login requests
            if split_data[0] == 'login':
                username, password = handle_login_msg(split_data[1:])
                bret, unique_id = db.find_username_and_password(username, password)
                if bret:
                    res = str(bret) + "\r\n" + unique_id
                else:
                    res = str(bret)

            #handle with sign up requests
            if split_data[0] == 'sign_up':
                name, email, username, password = handle_sign_up_msg(split_data[1:])
                bret, unique_id = db.add_user(name, email, username, password)
                if bret:
                    res = str(bret) + "\r\n" + unique_id
                else:
                    res = str(bret)

            if split_data[0] == 'pic':
                photo_name, doctor_id, img_bytes =handle_pic(split_data[1:], client_socket)
                db.add_image(doctor_id, img_bytes)

            if split_data[0] == 'add_patient':
                full_name, ID, email, gender, birth_date, case_description, visit_date, doctor_id, pneu_chance = handle_add_patient_msg(split_data[1:])
                if pneu_chance is None:
                    bret = db.add_patient(full_name, ID, email, gender, birth_date, case_description, visit_date, doctor_id)
                else:
                    bret = db.add_patient_with_photo(full_name, ID, email, gender, birth_date, case_description, visit_date, doctor_id, pneu_chance)
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
            response = response.encode()
            total_sent = 0
            # while total_sent < len(response):
            #     sent = client_socket.send(response)
            #     response = response[1024:]
            #     if sent == 0:
            #         raise RuntimeError("socket connection broken")
            #     total_sent += sent
            client_socket.sendall(response)
            # client_socket.close()
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
    ServerSideSocket = context.wrap_socket(ServerSideSocket, server_side=True)
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