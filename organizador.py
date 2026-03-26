from pathlib import Path
import shutil

# Pasta Downloads do usuário atual
pasta_alvo = Path.home() / "Downloads"

# Dicionário de categorias
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv"],
    "Áudio": [".mp3", ".wav", ".aac"],
}

# Cria subpastas para cada categoria
for categoria in categorias:
    (pasta_alvo / categoria).mkdir(exist_ok=True)

# Cria a pasta "Outros"
(pasta_alvo / "Outros").mkdir(exist_ok=True)

# Percorre todos os arquivos da pasta Downloads
for arquivo in pasta_alvo.iterdir():
    if arquivo.is_file():
        ext = arquivo.suffix.lower()
        destino = None

        # Verifica em qual categoria se encaixa
        for categoria, extensoes in categorias.items():
            if ext in extensoes:
                destino = pasta_alvo / categoria / arquivo.name
                break

        # Se não encontrou categoria, vai para "Outros"
        if destino is None:
            destino = pasta_alvo / "Outros" / arquivo.name

        shutil.move(str(arquivo), str(destino))

print("✅ Organização concluída!")

#Evitar sobrescrever arquivos: se já existir um arquivo com o mesmo nome na pasta de destino, o shutil.move vai dar erro. Você pode tratar isso assim:
if destino.exists():
    destino = destino.with_name(f"{destino.stem}_copy{destino.suffix}")
shutil.move(str(arquivo), str(destino))

# Aceitar pasta como argumento: se quiser organizar qualquer pasta, não só Downloads:
import sys
pasta_alvo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Downloads"

#Log mais detalhado: imprimir cada arquivo movido para acompanhar o processo:
print(f"Movendo {arquivo.name} → {destino.parent}")

#Aqui está a forma certa de montar a lista de arquivos com iterdir():
from pathlib import Path

alvo_pasta = Path.home() / "Downloads"

# Lista apenas os arquivos (ignora diretórios)
files = [f for f in alvo_pasta.iterdir() if f.is_file()]

# Percorre cada arquivo
for f in files:
    print(f.name, f.suffix)
    if f.name == "organizar.py":
        continue
if destino.exists():
    destino = destino.with_name(f"{destino.stem}_copy{destino.suffix}")
