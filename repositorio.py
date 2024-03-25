# repositorio.py

# Lista de usuários
usuarios = []

def adicionar_usuario(nome, idade, cidade):
    novo_id = len(usuarios) + 1
    usuarios.append({"id": novo_id, "nome": nome, "idade": idade, "cidade": cidade})

def editar_usuario(id, nome, idade, cidade):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = nome
            usuario["idade"] = idade
            usuario["cidade"] = cidade
            break

def deletar_usuario(id):
    usuarios[:] = [usuario for usuario in usuarios if usuario["id"] != id]
