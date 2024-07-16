from flask import Flask, request, render_template, redirect, url_for, session
from weather_info import get_weather_info

app = Flask(__name__)
app.secret_key = "teste"

@app.route('/', methods=['GET', 'POST'])
def menu():
    #Digitar nome da cidade
    if request.method == "POST":
        city = request.form["city"]
        session["city"] = city
        return redirect(url_for("result"))
    #clicar botao: chamar função get_weather_info e redireciona para a página de resultados
    return render_template("menu.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    try:
        city, weather_cond, temp, humidity, date, icon = get_weather_info(session["city"])
        return render_template("result.html", icon=icon, city=city, weather_cond=weather_cond, temp=temp, humidity=humidity, date=date)
    except:
        return get_weather_info(session["city"])
    
if __name__ == '__main__':
    app.run(debug=True)
