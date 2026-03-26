<<<<<<< HEAD
# Organizador de Arquivos em Python

Este projeto demonstra como automatizar uma tarefa repetitiva clássica: organizar arquivos em uma pasta, distribuindo-os em subpastas de acordo com seu tipo.  
O exemplo usa apenas bibliotecas padrão do Python e pode ser executado manualmente ou agendado para rodar periodicamente.

---

## 📌 Funcionalidades
- Organiza arquivos da pasta **Downloads** (ou outra especificada).
- Cria subpastas como **Imagens**, **Documentos**, **Vídeos**, **Áudio** e **Outros**.
- Move cada arquivo para a subpasta correspondente com base em sua extensão.
- Evita erros caso as pastas já existam (`mkdir(exist_ok=True)`).
- Pode ser expandido com opções de linha de comando (`argparse`).

---

## 🚀 Como funciona
1. Define um **dicionário de categorias**, onde as chaves são nomes de pastas e os valores são listas de extensões.
2. Lista todos os arquivos da pasta alvo usando `Path.iterdir()`.
3. Para cada arquivo:
   - Obtém a extensão com `Path.suffix`.
   - Determina a categoria correspondente.
   - Cria a pasta de destino se não existir.
   - Move o arquivo com `Path.rename`.
   - Imprime no console o movimento realizado.
4. Arquivos sem categoria definida vão para a pasta **Outros**.

---

## 📂 Exemplo de uso
Na pasta `Downloads`, crie os arquivos:
- `foto1.jpg`
- `documento.txt`
- `video.mkv`
- `audio.mp3`
- `script.py`

Execute:
```bash
python organizar.py
=======
# Organizador-de-Arquivos
>>>>>>> c774294517ea9046fce888615a4719f4bebf0a73
