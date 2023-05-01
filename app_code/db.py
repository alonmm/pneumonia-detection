import hashlib
import threading
import sqlite3
from uuid import uuid4
connection = sqlite3.connect("user_details.db", check_same_thread=False)
cur = connection.cursor()


def build_DB():
    command = """CREATE TABLE IF NOT EXISTS user_details_db(full_name TEXT NOT NULL, email TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, unique_id TEXT NOT NULL) """
    print("111", threading.get_native_id())
    command_2 = """CREATE TABLE IF NOT EXISTS patient_details_db(full_name TEXT NOT NULL, ID INTEGER NOT NULL, email TEXT NOT NULL, date TEXT NOT NULL, description TEXT NOT NULL, doctor_id TEXT NOT NULL, pneu_chance TEXT) """
    cur.execute(command)
    connection.commit()
    cur.execute(command_2)
    connection.commit()


#def insert_to_DB(username, password):
    #connection.execute("INSERT INTO user_details_db (username, password) VALUES (?,?)", (username, password))
   # connection.commit()
   # connection.ro

def add_user(name, email, username, password):

    # check if a row is already exist
    cur.execute("SELECT rowid FROM user_details_db WHERE username = ?", (username,))
    db_result = cur.fetchall()
    if len(db_result) == 0:
        unique_id = str(uuid4())
        connection.execute("INSERT INTO user_details_db (full_name, email, username, password, unique_id) VALUES (?,?,?,?,?)", (name, email, username, password, unique_id))
        connection.commit()
        return True, unique_id
    else:
        return False, None

def add_patient(full_name, ID, email, date, description, doctor_id):
    try:
        # check if the patient is already exists
        cur.execute("SELECT rowid FROM patient_details_db WHERE full_name = ?", (full_name,))
        db_result = cur.fetchall()
        if len(db_result) != 0:
            connection.execute("DELETE FROM patient_details_db WHERE  full_name = '" + full_name + "'")
            connection.commit()
            # command = "UPDATE patient_details_db SET pneu_chance = '"+ pneu_chance + "' WHERE ID = '"+ID+"'"
        connection.execute("INSERT INTO patient_details_db (full_name, ID, email, date, description, doctor_id) VALUES (?,?,?,?,?,?)", (full_name, ID, email, date, description, doctor_id))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def add_patient_with_photo(full_name, ID, email, date, description, doctor_id, pneu_chance):
    try:
        # check if the patient is already exists
        cur.execute("SELECT rowid FROM patient_details_db WHERE full_name = ?", (full_name,))
        db_result = cur.fetchall()
        if len(db_result) != 0:
            connection.execute("DELETE FROM patient_details_db WHERE  full_name = '" + full_name + "'")
            connection.commit()
        connection.execute("INSERT INTO patient_details_db (full_name, ID, email, date, description, doctor_id, pneu_chance) VALUES (?,?,?,?,?,?,?)", (full_name, ID, email, date, description, doctor_id, pneu_chance))
        connection.commit()
        return True

    except Exception as e:
        print(e)
        return False

def find_username(username):
    cur.execute("SELECT rowid FROM user_details_db WHERE username = ? ", (username,))
    db_result = cur.fetchall()
    if len(db_result) == 0:
        return False
    else:
        return True

def find_username_and_password(username, password):
    cur.execute("SELECT rowid FROM user_details_db WHERE username = ? AND password = ?", (username, password,))
    db_result = cur.fetchall()
    print(type(db_result))
    if len(db_result) == 0:
        return False, None
    else:
        cur.execute('SELECT unique_id FROM user_details_db')
        data = cur.fetchall()
        db_result = db_result[0]
        row_number = db_result[0]-1
        unique_id_tuple = data[row_number]
        return True, str(unique_id_tuple[0])

def get_patients_list(doctor_id):
    cur.execute('SELECT * FROM patient_details_db')
    data = cur.fetchall()
    patient_list = ''
    for row in data:
        if row[5] == doctor_id:
            row = row[:-1]
            patient_list += '#'.join(str(s) for s in row) +'\r\n'
    return patient_list

def get_specific_patient(patient_id):
    cur.execute('SELECT * FROM patient_details_db')
    data = cur.fetchall()
    patient = ''
    for row in data:
        id = str(row[1])
        if id == patient_id:
            if row[-1] == None:
                row = row[:-1]
            patient += '#'.join(str(s) for s in row) + '\r\n'

            break
    return patient

#if __name__ == '__main__':
