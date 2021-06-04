import socket, cv2, os
import numpy as np
import threading as thread

# tcp and ipv4 address family
tcp = socket.SOCK_STREAM
afm = socket.AF_INET

# user b
userb_ip = "192.168.0.103"
userb_port = 2001

# creating socket
sb = socket.socket(afm,tcp)
sa = socket.socket(afm,tcp)

# bindiing ports 
sb.bind((userb_ip,userb_port))

# connecting to usera
sa.connect((userb_ip,2000))

# listening port and creating session
sb.listen()
session, addr = sb.accept()

print(addr)

def receive():
    while True:
        en_photo = session.recv(921600)
        image_arr = np.frombuffer(en_photo,np.uint8)
        image = cv2.imdecode(image_arr, cv2.IMREAD_COLOR)
        if type(image) is type(None):
            pass
        else:
            cv2.imshow("Video stream", image)
            if cv2.waitKey(10) == 13: 
                break

    cv2.destroyAllWindows()
    os._exit(1)


def send():
    capture = cv2.VideoCapture(3)

    while True:
        ret, photo = capture.read()
        if ret == True:
            en_photo = cv2.imencode('.jpg',photo)[1].tobytes()
            sa.sendall(en_photo)
        else: 
            pass

    os.exit_(1)


# send and receive threads
send_thread = thread.Thread(target=send)
recv_thread = thread.Thread(target=receive)

# starting threads
send_thread.start()
recv_thread.start()