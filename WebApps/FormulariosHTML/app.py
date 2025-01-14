from flask import Flask, request,url_for,render_template
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html",titulo="Ejemplo aplicación Flask")

@app.route("/suma",methods=["GET","POST"])
def sumar():
	if request.method=="POST":
		num1=request.form.get("num1")
		num2=request.form.get("num2")
		suma = int(num1)+int(num2)
		try:
			resultado=f"Resultado de la suma: {str(suma)}"
		except:
			resultado="No se puede realizar la suma"
		return render_template("resultado.html",titulo="Resultado de la suma",resultado=resultado)
	else:
		return render_template("suma.html",titulo="Sumar")

if __name__ == '__main__':
	app.run(debug=False)
