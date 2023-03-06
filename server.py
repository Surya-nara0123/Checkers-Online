import socket, threading, sys, datetime
clientList = []

def clientHandler(c, addr):
    while True:
        clientList.append((c, addr))
        while True:
            try:
                board = c.recv(2048).decode("utf-8")
            except Exception as m:
                board = ''
            if board != '':
                for socket, us, m  in clientList:
                    try:
                        socket.send(f"{board[::-1]}".encode("utf-8"))
                    except BrokenPipeError:
                        pass
def function():

    while True:
        c, addr = s.accept()
        threading.Thread(target=clientHandler, args=(c, addr)).start()
    
if __name__ == "__main__":
    try:
        s = socket.socket()
        port = 12345
        s.bind(('', port))
        s.listen(1)
        function()
    except:
        pass
    