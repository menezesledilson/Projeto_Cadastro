from flask import Flask, render_template, flash, redirect, url_for, request
from repositorio import usuarios, adicionar_usuario, editar_usuario, deletar_usuario

app = Flask(__name__)
app.secret_key = "admin123"

@app.route("/")
def index():
    return render_template("index.html", users=usuarios)

@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = int(request.form["idade"])
        rua = request.form["rua"]
        cidade = request.form["cidade"]
        numero = request.form["numero"]
        estado = request.form["estado"]
        
        adicionar_usuario(nome, idade, rua, cidade, numero, estado)  # Corrigido para passar todos os argumentos necessários
        flash("Usuário adicionado com sucesso!", "success")
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<int:id>", methods=["POST","GET"])
def edit_user(id):
    user = next((user for user in usuarios if user["id"] == id), None)
    if not user:
        flash("Usuário não encontrado!", "error")
        return redirect(url_for("index"))
    if request.method == "POST":
        nome = request.form["nome"]
        idade = int(request.form["idade"])
        rua = request.form["rua"]  
        cidade = request.form["cidade"]
        numero = request.form["numero"]
        estado = request.form["estado"]
        editar_usuario(id, nome, idade, rua, cidade, numero, estado)   
        flash("Usuário atualizado com sucesso!", "success")
        return redirect(url_for("index"))
    return render_template("edit_user.html", user=user)

@app.route("/delete_user/<int:id>", methods=["GET"])
def delete_user(id):
    user = next((user for user in usuarios if user["id"] == id), None)
    if not user:
        flash("Usuário não encontrado!", "error")
    else:
        deletar_usuario(id)
        flash("Usuário deletado com sucesso!", "warning")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
