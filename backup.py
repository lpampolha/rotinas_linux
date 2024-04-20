import os
import shutil

origem = ("/app/")
destino = ("/root/")

arquivos = os.listdir(origem)
arquivos
print(arquivos)

for arquivo in arquivos:
    shutil.copy2(arquivo, destino)