from flask import Flask, render_template

app=Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html') 

if __name__=='__main__':
   app.run(debug=True)

    
