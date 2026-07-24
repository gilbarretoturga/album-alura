from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância da aplicação FastAPI
app = FastAPI()

# 1. Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Define caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# 3. Lista de 30 figurinhas, deixando ativas apenas as que existem na pasta de imagens
figurinhas_estaticas = [
    {
        "id": 1,
        "nome": "Joaquim",
        "categoria": "Pai",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": 2,
        "nome": "Neli",
        "categoria": "Mãe",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
        "id": 3,
        "nome": "Erdinilza",
        "categoria": "Filha",
        "imagem_url": "/figurinhas/3/imagem"
    },
    {
        "id": 4,
        "nome": "Arnaldo",
        "categoria": "Filho",
        "imagem_url": "/figurinhas/4/imagem"
    },
    {
        "id": 5,
        "nome": "Gernilson",
        "categoria": "Filho",
        "imagem_url": "/figurinhas/5/imagem"
    },
    {
        "id": 6,
        "nome": "Sirlene",
        "categoria": "Filha",
        "imagem_url": "/figurinhas/6/imagem"
    },
    {
        "id": 7,
        "nome": "Gildeon",
        "categoria": "Filho",
        "imagem_url": "/figurinhas/7/imagem"
    },
    {
        "id": 8,
        "nome": "Gildei",
        "categoria": "Filho",
        "imagem_url": "/figurinhas/8/imagem"
    },
    {
        "id": 9,
        "nome": "Carlos",
        "categoria": "Genro",
        "imagem_url": "/figurinhas/9/imagem"
    },
    {
        "id": 10,
        "nome": "Danilia",
        "categoria": "Nora",
        "imagem_url": "/figurinhas/10/imagem"
    },
    {
        "id": 11,
        "nome": "Poliana",
        "categoria": "Nora",
        "imagem_url": "/figurinhas/11/imagem"
    },
    {
        "id": 12,
        "nome": "Daniella",
        "categoria": "Neta",
        "imagem_url": "/figurinhas/12/imagem"
    },
    
     {
         "id": 13,
         "nome": "Lucas",
         "categoria": "Neto",
         "imagem_url": "/figurinhas/13/imagem"
     },
     {
         "id": 14,
         "nome": "Livia",
         "categoria": "Neta",
         "imagem_url": "/figurinhas/14/imagem"
     },
     {
         "id": 15,
         "nome": "Momento",
         "categoria": "momento",
         "imagem_url": "/figurinhas/15/imagem"
     },    

     {
         "id": 16,
         "nome": "Momentos 2",
         "categoria": "momento",
         "imagem_url": "/figurinhas/16/imagem"
     }, 
     # As figurinhas abaixo ainda não possuem imagens correspondentes na pasta e estão comentadas:
     # {
    #     "id": 21,
    #     "nome": "Figurinha 21",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/21/imagem"
    # },
    # {
    #     "id": 22,
    #     "nome": "Figurinha 22",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/22/imagem"
    # },
    # {
    #     "id": 23,
    #     "nome": "Figurinha 23",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/23/imagem"
    # },
    # {
    #     "id": 24,
    #     "nome": "Figurinha 24",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/24/imagem"
    # },
    # {
    #     "id": 25,
    #     "nome": "Figurinha 25",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/25/imagem"
    # },
    # {
    #     "id": 26,
    #     "nome": "Figurinha 26",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/26/imagem"
    # },
    # {
    #     "id": 27,
    #     "nome": "Figurinha 27",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/27/imagem"
    # },
    # {
    #     "id": 28,
    #     "nome": "Figurinha 28",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/28/imagem"
    # },
    # {
    #     "id": 29,
    #     "nome": "Figurinha 29",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/29/imagem"
    # },
    # {
    #     "id": 30,
    #     "nome": "Figurinha 30",
    #     "categoria": "Parente",
    #     "imagem_url": "/figurinhas/30/imagem"
    # }
]

# Extensões de imagem suportadas
EXTENSOES_IMAGEM = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff"}

def obter_novos_arquivos():
    caminhos_estaticos = set()
    for f in figurinhas_estaticas:
        padrao = os.path.join(PASTA_IMAGENS, f"{f['id']:02d}[!0-9]*")
        caminhos_estaticos.update(glob.glob(padrao))
    
    todos = glob.glob(os.path.join(PASTA_IMAGENS, "*"))
    todos_arquivos = []
    for f in todos:
        if os.path.isfile(f):
            _, ext = os.path.splitext(f)
            if ext.lower() in EXTENSOES_IMAGEM:
                todos_arquivos.append(f)
                
    novos = [f for f in todos_arquivos if os.path.abspath(f) not in {os.path.abspath(p) for p in caminhos_estaticos}]
    # Ordena os novos alfabeticamente para consistência
    novos.sort(key=lambda x: os.path.basename(x).lower())
    return novos

# 4. Endpoint GET "/figurinhas" que retorna a lista das figurinhas (estáticas + dinâmicas)
@app.get("/figurinhas")
def listar_figurinhas():
    lista = list(figurinhas_estaticas)
    novos = obter_novos_arquivos()
    
    max_id = max([f["id"] for f in figurinhas_estaticas]) if figurinhas_estaticas else 0
    for idx, caminho in enumerate(novos):
        novo_id = max_id + 1 + idx
        lista.append({
            "id": novo_id,
            "nome": "", # sem nome
            "categoria": "Extra",
            "imagem_url": f"/figurinhas/{novo_id}/imagem"
        })
    return lista

# 5. Endpoint GET "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    # Verifica se o ID corresponde a uma das figurinhas estáticas
    id_estatico = any(f["id"] == id for f in figurinhas_estaticas)
    if id_estatico:
        # Padrão glob original para buscar arquivos na pasta com prefixo formatado "{id:02d}[!0-9]*"
        padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
        arquivos = glob.glob(padrao)
        if not arquivos:
            raise HTTPException(status_code=404, detail="Imagem não encontrada")
        return FileResponse(arquivos[0])
    else:
        # Se for um ID dinâmico, recupera a imagem da lista ordenada de novos arquivos
        novos = obter_novos_arquivos()
        max_id = max([f["id"] for f in figurinhas_estaticas]) if figurinhas_estaticas else 0
        idx = id - (max_id + 1)
        if 0 <= idx < len(novos):
            return FileResponse(novos[idx])
        else:
            raise HTTPException(status_code=404, detail="Imagem não encontrada")
