import os
import signal
import time
from _thread import *

from tabulate import tabulate
import subprocess, sys, socket

FILE_NAME = "init.config"
DATA_TRANSFER_FILE_NAME = "data_transfer.config"
RESULT_FILE_NAME = "manager_result.log"


# UDP_PORT_START = 5005


# FILE_NAME = sys.argv[1]
class Manager:
    socket_tcp = None
    TCP_PORT = 5000
    TCP_IP = "127.0.0.1"
    TCP_IP_INIT = 2

    def read_init_file(self):
        f = open(FILE_NAME, "r")
        f.seek(0)
        return f.read()

    def make_table(self):
        inner_lines = [["From", "To", "Cost"]]
        with open(FILE_NAME, "r") as f:
            lines = [line.rstrip() for line in f]
            for num in lines:
                org, dest, cost = num.split()
                if org != dest:
                    line = [org, dest, cost]
                    inner_lines.append(line)
                    # print(line)
                    line = [dest, org, cost]
                    inner_lines.append(line)
                    # print(line)

                else:
                    line = [org, dest, cost]
                    # print(line)

        print(inner_lines)
        print(tabulate(inner_lines))
        return tabulate(inner_lines)

    def make_router(self):
        # inner_lines = [["From", "To", "Cost"]]
        router_names = list()
        router_udps = dict()
        router_tcp_addresses = dict()
        router_processes = list()

        with open(FILE_NAME, "r") as f:
            lines = [line.rstrip() for line in f]
            for num in lines:
                org, dest, _ = num.split()
                if org not in router_names:
                    router_names.append(org)
                    router_udps[org] = None
                    router_tcp_addresses[org] = "127.0.0." + str(self.TCP_IP_INIT)
                    self.TCP_IP_INIT += 1
                elif dest not in router_names:
                    router_names.append(dest)
                    router_udps[dest] = None
                    router_tcp_addresses[dest] = "127.0.0." + str(self.TCP_IP_INIT)
                    self.TCP_IP_INIT += 1

        router_names.sort()
        print(router_names)

        print("HI", router_tcp_addresses)

        for router_name in router_names:
            router_process = subprocess.Popen('start python router_new.py' + ' ' + router_name, shell=True)
            print(router_process.stdout)
            with open(RESULT_FILE_NAME, 'a') as f:
                f.write("Created " + router_name + '\n')
            router_processes.append(router_process)

            self.socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_tcp.bind((self.TCP_IP, self.TCP_PORT))
            self.socket_tcp.listen()
            conn, addr = self.socket_tcp.accept()
            with conn:
                print('Connected by', addr)

                while True:
                    data = conn.recv(1024)
                    router_udps[router_name] = str(data)[2:-1]
                    print(data)
                    conn.sendall((bytes(str(data), 'utf-8')))
                    conn.sendall((bytes(str(router_tcp_addresses[router_name]), 'utf-8')))

                    break

        print(router_udps)
        # self.socket_tcp.close()

        for router_name in router_names:

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((router_tcp_addresses[router_name], 5000))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    data = self.make_adjacent_connectivity_table(router_name, router_udps, router_tcp_addresses)
                    conn.sendall((bytes(str(data), 'utf-8')))
                    data_ack = conn.recv(2048)
                    print(str(data_ack)[2:-1].startswith("Ready"))
                    if str(data_ack)[2:-1].startswith("Ready"):
                        print("READY!")
                    else:
                        continue

                    with open(RESULT_FILE_NAME, 'a') as f:
                        f.write(str(data_ack)[2:-1] + '\n')

        for router_name in router_names:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((router_tcp_addresses[router_name], 5000))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    conn.sendall(b'safe')

        return router_processes, router_names, router_tcp_addresses, router_udps

    def make_adjacent_connectivity_table(self, name, udps, tcp_ips):
        connectivity_table = list()
        with open(FILE_NAME, "r") as f:
            lines = [line.rstrip() for line in f]
            for num in lines:
                org, dest, cost = num.split()
                if org == name:
                    connectivity_table.append([org, dest, cost, udps[dest], tcp_ips[dest]])
                elif dest == name:
                    connectivity_table.append([dest, org, cost, udps[org], tcp_ips[org]])
        # print(connectivity_table)
        return connectivity_table

    def make_tcp_connection(self, name):
        pass

    def tcp_send(self):
        pass

    def tcp_receive(self):
        pass


manager = Manager()
router, router_names, router_tcp_addresses, router_udps = manager.make_router()
open(RESULT_FILE_NAME, 'w').close()

for router_name in router_names:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((router_tcp_addresses[router_name], 5000))
        s.listen()
        conn, addr = s.accept()
        with conn:
            # conn.settimeout(20)
            print('Connected by', addr)
            data_ack = conn.recv(2048)
            print(data_ack)
            # if not data_ack.decode('utf-8').startswith("SecondReady"):
            #     all_ready = False
            message = bytes("OK \n" + str(router_tcp_addresses) + "\n" + str(router_udps), 'utf-8')
            conn.sendall(message)
            # conn.sendall(b'OK')

with open(DATA_TRANSFER_FILE_NAME, "r") as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        router_name, dest_router_name = line.split(" ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((router_tcp_addresses[router_name], 7000))
            s.listen()
            conn, addr = s.accept()
            with conn:
                # conn.settimeout(20)
                print('Connected by', addr)
                # data_ack = conn.recv(2048)
                # print(data_ack)
                # if not data_ack.decode('utf-8').startswith("SecondReady"):
                #     all_ready = False
                message = bytes("Send Data \n" + str(router_tcp_addresses[dest_router_name]), 'utf-8')
                conn.sendall(message)
                # conn.sendall(b'OK')
        time.sleep(10)

    print(lines)

# def threaded_client(connection):
#     connection.send(str.encode('Welcome to the Servern'))
#     while True:
#         data = connection.recv(2048)
#         reply = 'Server Says: ' + data.decode('utf-8')
#         if not data:
#             break
#         connection.sendall(str.encode(reply))
#     connection.close()
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(("127.0.0.1", 4000))
#     s.listen(10)
#     while True:
#         Client, address = s.accept()
#         print('Connected to: ' + address[0] + ':' + str(address[1]))
#         start_new_thread(threaded_client, (Client, ))
#         # ThreadCount += 1
#         # print('Thread Number: ' + str(ThreadCount))
#     ServerSocket.close()


# all_ready = False
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(("127.0.0.1", 4000))
#
#     s.listen(10)
#     conn, addr = s.accept()
#     with conn:
#         # conn.settimeout(20)
#         print('Connected by', addr)
#         while True:
#             try:
#                 data_ack = conn.recv(2048)
#                 print(data_ack)
#                 if not data_ack.decode('utf-8').startswith("SecondReady"):
#                     all_ready = False
#             except socket.timeout:
#                 if all_ready:
#                     conn.sendall(b'OK')


# for p in router:
#     # p.terminate()
#     os.killpg(os.getpgid(p.pid), signal.SIGTERM)


print("THE END")
while True:
    pass