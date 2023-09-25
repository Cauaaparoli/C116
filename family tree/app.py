# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Caua" # escreva seu nome
    idade = "14" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
    return render_template('pai.html')

# defina a rota para a página da mãe
    return render_template('mae.html')

# defina a rota para a página do amigo
    return render_template('amigo.html')

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
