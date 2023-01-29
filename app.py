from flask import Flask, render_template
import random as r
import time as t

app = Flask(__name__)


def rand():
	list = ["Salmos 23, Versiculo 1: 'O Senhor é meu pastor e nada me faltará'","Salmos 91, Versiculo 9: 'Porque Tu, ó Senhor, és o meu refúgio! O Atissimo é a tua habitação.'","Josué 1 Versiculo 9: 'Não to mandei Eu? Esforça-te e tem bom ânimo; não pasmes, nem te espantes; porque o Senhor teu Deus é contigo, por onde quer que andares.'","Salmos 32 Versiculo 1 & 2: 'BEM-AVENTURADO aquele cuja transgreção é perdoada, e cujo pecado é coberto. Bem-aventurado o homem a quem o Senhor não imputa maldade, e em cujo o espírito não há engano.'","Salmos 32 Versiculo 7: 'Tu és o lugar em que me escondo; Tu me preservas da angústia; Tu me singes de alegres cantos  de livramento (Selá).'"]
	result = r.choice(list)
	return result
@app.route("/")
def index():
	txt = rand()
	return render_template("index.html", text=txt)

if __name__ == "__main__":
	app.run(debug=True)
