import speedtest
from datetime import datetime

velocidade = speedtest.Speedtest()

data = datetime.now()
print(data.strftime('%d/%m/%Y %H:%M'))

download = velocidade.download()
print(f"Velocidade de download: {download / 10**6:.2f}")

upload = velocidade.upload()
print(f"Velocidade de upload: {upload / 10**6:.2f}")

ping = velocidade.results.ping
print(f'Ping: {ping:.2f}')
print('_________________________________________________________')