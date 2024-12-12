from fastapi import FastAPI
from typing import List
import sqlite3

app = FastAPI()

# Função para criar um usuário
@app.post("/create_user")
def criar_usuario(nome: str, palavra: str, preco: str):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()  # Corrigido: adicionar os parênteses
    cursor.execute('''
    INSERT INTO data (nome, palavra, preco) VALUES (?, ?, ?)
    ''', (nome, palavra, preco))
    conn.commit()
    conn.close()  # Boa prática fechar a conexão
    return {"status": "usuário criado com sucesso", "nome": nome, "palavra": palavra, "preco": preco}

# Função para listar os usuários
@app.get("/users", response_model=List[dict])
def listar_usuarios():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()  
    cursor.execute("""
    SELECT * FROM data 
    """)
    usuarios = cursor.fetchall()
    conn.close()

    return [dict(usuario) for usuario in usuarios]
