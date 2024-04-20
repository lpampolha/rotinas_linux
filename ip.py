import requests

ip_publico = requests.get('https://api.ipify.org').text
print(f'IP Público: {ip_publico}')
