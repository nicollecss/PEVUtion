from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    telefone = db.Column(db.Integer)
    senha = db.Column(db.Integer)

class jasoualuno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)

    senha = db.Column(db.Integer)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/criar_aluno", methods=["GET", "POST"])
def aluno_create():
    if request.method == "POST":
        print(request.form["email"])

        alunos= Aluno(
            email=request.form["email"],
            telefone=request.form["telefone"],
            senha=request.form["senha"]
        )

        db.session.add(alunos)
        db.session.commit()
        return redirect("aluno")
    return render_template("cadastro.html")




@app.route("/aluno")
def alunos_list():
    alunos = db.session.query(Aluno)
    return render_template('listadealunos.html', alunos=alunos)



@app.route ('/vest')
def vest ():
    return render_template ('vest.html')

@app.route ('/enem')
def enem ():
    return render_template ('enem.html')

@app.route ('/pas')
def pas ():
    return render_template ('pas.html')

@app.route ('/pas_primeira_etapa')
def PAS1 ():
    return render_template ('pas1.html')

@app.route ('/pas_segunda_etapa')
def PAS2 ():
    return render_template ('pas2.html')

@app.route ('/pas_terceira_etapa')
def PAS3 ():
    return render_template ('pas3.html')

@app.route ('/sobre')
def sobre ():
    return render_template ('sobre.html')

@app.route ('/cadastro_aluno')
def signin ():
    return render_template ('cadastro.html')

@app.route ('/login_aluno')
def entrar_conta ():
    return render_template ('aluno.html')


if __name__ == '__main__':
    app.run(debug=True)






















































































































