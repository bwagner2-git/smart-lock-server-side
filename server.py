#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import threading
from Crypto.Cipher import AES
import face_recognition as fr
from Crypto.Util.Padding import pad,unpad
import datetime
import numpy as np
import pathlib


HOST="104.194.110.170"
PORT = 6000
KEY= b'3874460957140850'
iv = b'9331626268227018'
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
HEADER = 135 #size of the first message specifying how big the entire message will be
FORMAT='utf-8' #format for encoding and decoding
DISCONNECT_MESSAGE="!DISCONNECT" #message that will tell the server the client is disconnecting

def handle_client(conn, addr):
    print("Connection by " + str(addr))
    connected=True
    while connected:
        msg_len=conn.recv(HEADER).decode(FORMAT) #length of message
        if msg_len: ###ignore the initial null message
            msg_len=int(msg_len)  ###decrypt and decode the message
            print("Message Length: " + str(msg_len))
            msg=conn.recv(msg_len)
            print("Real Message Lenght: " + str(len(msg)))
            dec_cipher = AES.new(KEY, AES.MODE_CBC, IV=iv)
            plaintext=dec_cipher.decrypt(msg)
            plaintext=unpad(plaintext,16)
            plaintext=plaintext.decode(FORMAT)
            print(str(addr)+str(plaintext))
            if plaintext == DISCONNECT_MESSAGE: ##if the disconnect message is sent
                print(str(addr)+" Disconnected")
                break #initiate disconnect
                
            access=False #do not grant access yet
            ### handle the which comes in the format username,code,encoding info message ###
            lst=plaintext.split(',')
            lst[2]=lst[2][1:-1]
            lst[2].replace('\n','')
            f=lst[2].split()
            target=np.array(f, dtype=float) ### turn encoding back into numpy array so it can be compared using fr module
            
            ### compare faces with everyone in the users account ###
            people_with_access=[]
            
            allowed=[] ## allowed user encoding
            with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\people\\one.txt', 'r') as file:
                for line in file:
                    # remove linebreak which is the last character of the string
                    position = line[:-1]
                    # add item to the list
                    allowed.append(position)  
            allowed=np.array(allowed, dtype=float)  #turn into numpy array to be compared
            if len(allowed) !=0: ###if the owner of the box has a person for this spot add them to the list of people
                people_with_access.append(allowed)
            
            
            allowed=[] ## allowed user encoding
            with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\people\\two.txt', 'r') as file:
                for line in file:
                    # remove linebreak which is the last character of the string
                    position = line[:-1]
                    # add item to the list
                    allowed.append(position)
            allowed=np.array(allowed, dtype=float)  #turn into numpy array to be compared
            if len(allowed) !=0: ###if the owner of the box has a person for this spot add them to the list of people
                people_with_access.append(allowed)
            
            allowed=[] ## allowed user encoding
            with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\people\\three.txt', 'r') as file:
                for line in file:
                    # remove linebreak which is the last character of the string
                    position = line[:-1]
                    # add item to the list
                    allowed.append(position)  
            allowed=np.array(allowed, dtype=float)  #turn into numpy array to be compared
            if len(allowed) !=0: ###if the owner of the box has a person for this spot add them to the list of people
                people_with_access.append(allowed)
            
            allowed=[] ## allowed user encoding
            with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\people\\four.txt', 'r') as file:
                for line in file:
                    # remove linebreak which is the last character of the string
                    position = line[:-1]
                    # add item to the list
                    allowed.append(position)  
            allowed=np.array(allowed, dtype=float)  #turn into numpy array to be compared
            if len(allowed) !=0: ###if the owner of the box has a person for this spot add them to the list of people
                people_with_access.append(allowed)
            
            allowed=[] ## allowed user encoding
            with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\people\\five.txt', 'r') as file:
                for line in file:
                    # remove linebreak which is the last character of the string
                    position = line[:-1]
                    # add item to the list
                    allowed.append(position)  
            allowed=np.array(allowed, dtype=float)  #turn into numpy array to be compared
            if len(allowed) !=0: ###if the owner of the box has a person for this spot add them to the list of people
                people_with_access.append(allowed)
            
            allowed=[] ## allowed user encoding
            with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\people\\six.txt', 'r') as file:
                for line in file:
                    # remove linebreak which is the last character of the string
                    position = line[:-1]
                    # add item to the list
                    allowed.append(position)  
            allowed=np.array(allowed, dtype=float)  #turn into numpy array to be compared
            if len(allowed) !=0: ###if the owner of the box has a person for this spot add them to the list of people
                people_with_access.append(allowed)
            
            allowed=[] ## allowed user encoding
            with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\people\\seven.txt', 'r') as file:
                for line in file:
                    # remove linebreak which is the last character of the string
                    position = line[:-1]
                    # add item to the list
                    allowed.append(position)  
            allowed=np.array(allowed, dtype=float)  #turn into numpy array to be compared
            if len(allowed) !=0: ###if the owner of the box has a person for this spot add them to the list of people
                people_with_access.append(allowed)
            
            allowed=[] ## allowed user encoding
            with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\people\\eight.txt', 'r') as file:
                for line in file:
                    # remove linebreak which is the last character of the string
                    position = line[:-1]
                    # add item to the list
                    allowed.append(position)  
            allowed=np.array(allowed, dtype=float)  #turn into numpy array to be compared
            if len(allowed) !=0: ###if the owner of the box has a person for this spot add them to the list of people
                people_with_access.append(allowed)
            
            ##### make decisions######
            decision_array=fr.compare_faces(people_with_access,target)
            print(decision_array)
            if True in decision_array:
                access=True
                code =lst[1]
                with open(str(pathlib.Path().absolute())+'\\users'+'\\boxes\\'+lst[0]+'\\log.txt', 'a') as file:
                    file.write(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+'\n') #add the access time to that specific boxes time log to be displayed by the web app
                
            else:
                code='Access Denied'
            en_cipher=AES.new(KEY, AES.MODE_CBC, IV=iv)
            message_back=en_cipher.encrypt(pad(code.encode(FORMAT),16))
            conn.send(message_back)
            
            
            
    conn.close() #close the connection, this is important to tell the server in case the client ever wants to reconnect again after closing the intial connection


def start():
    print("Server is starting: ")
    s.listen()
    while True:
        conn, addr = s.accept()
        thread=threading.Thread(target=handle_client, args=(conn,addr))    ### threading allows us to handle mutliple clients connecting to the server at once
        thread.start()
        print(str(threading.activeCount()-1)+" Active Connections")

start()
s.close() #if we get here for whatever reason close the socket

        

    
#alot of credit to Tech with Tim for providing a socket programming tutorial that helped me tremendously with this code https://www.youtube.com/watch?v=3QiPPX-KeSc

