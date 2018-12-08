import socket

port = 60000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print 'Server listening....'

while True:
    conn, addr = s.accept()
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = '/home/jackiechang/Downloads/software/CPLEX/cplex_studio128.win-x86-64.exe'
    f = open(filename, 'rb')
    l = f.read(1024)
    while(l):
        conn.send(l)
      #  print('Sent ', repr(l),'\n')
        l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()

