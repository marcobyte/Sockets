import time
from socket import *

server_address = 'localhost' 
server_port = 50000

# socket UDP
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)  # timeout de 1 segundo

rtts = []
pacotes_enviados = 10
pacotes_recebidos  = 0

# envio dos 10 pings
for n in range(1, pacotes_enviados+1):
    envio = time.time()
    messagem = f"Ping {n}"

    try:
        #Envia a mensagem para o servidor
        client_socket.sendto(messagem.encode(), (server_address, server_port))

        resposta, _ = client_socket.recvfrom(1024)
        
        #RTT
        recebimento = time.time()
        rtt = recebimento - envio
        rtts.append(rtt)
        pacotes_recebidos += 1
        
        #print(f"Resposta do servidor: {resposta.decode()} \nRTT: {rtt:.6f} segundos\n")
    except timeout:
        print("Request timed out\n")

min_rtt = min(rtts)
max_rtt = max(rtts)
avg_rtt = sum(rtts) / len(rtts)

taxa_perda = ((pacotes_enviados-pacotes_recebidos)/pacotes_enviados)*100
print("----------------->")
print(f"Pacotes enviados: {pacotes_enviados}")
print(f"Pacotes recebidos: {pacotes_recebidos}")
print(f"Perda de pacotes: {taxa_perda:.2f}%")

print(f"RTT minimo: {min_rtt:.6f} segundos")
print(f"RTT maximo: {max_rtt:.6f} segundos")
print(f"RTT medio: {avg_rtt:.6f} segundos")


client_socket.close()
