from flask import Flask, request, render_template, redirect, url_for
import weather_info

app = Flask(__name__)

@app.route('/menu', '/', methods=['GET', 'POST'])
def menu():
    #Digitar nome da cidade
    #clicar botao: chamar função get_weather_info e redireciona para a página de resultados
    return render_template("menu.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)
