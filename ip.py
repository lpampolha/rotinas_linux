import requests

file = ("/app/ip.txt", "w+")
ip_publico = requests.get('https://api.ipify.org').text
print(f'IP Público: {ip_publico}', file=file)
