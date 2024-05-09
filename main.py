from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html',resultado="")

@app.route('/verificaidade', methods = ['POST'])
def verificaidade():
    verificar = " "
    idade = int(request.form["idade"])
    if (idade >= 0) and (idade <= 5):  # condição de idade
        verificar = "Bebê"
    elif (idade >= 6) and (idade <= 15):  # condição de idade
        verificar = "Criança"  # impressão
    elif (idade >= 16) and (idade <= 18):  # condição de idade
        verificar = "Marmanjos hora de trabalhar"  # impressão
    elif (idade >= 19) and (idade <= 60):  # condição de idade
        verificar = "Acorda pra vida, que você tem boleto pra pagar" # impressão
    if (idade > 60):  # condição de idade
        verificar = "Daqui pra frente e só pra traz"  # impressão
    return render_template('index.html', resultado=verificar)

if __name__ == "__main__":
    app.run(debug=True)
