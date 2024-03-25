# repositorio.py

# Lista de usuários
usuarios = []

def adicionar_usuario(nome, idade, rua, cidade, numero, estado):
    novo_id = len(usuarios) + 1
    usuarios.append({"id": novo_id, "nome": nome, "idade": idade, "rua":rua, "cidade": cidade, "numero": numero, "estado":estado})

def editar_usuario(id,nome, idade, rua, cidade, numero, estado):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = nome
            usuario["idade"] = idade
            usuario["rua"] = rua
            usuario["cidade"] = cidade
            usuario["numero"] = numero
            usuario["estado"] = estado
            break

def deletar_usuario(id):
    usuarios[:] = [usuario for usuario in usuarios if usuario["id"] != id]
