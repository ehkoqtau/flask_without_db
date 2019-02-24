"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for, session, flash
from web_flask import app

from .include.rumus_mtk import Lingkaran


#config
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.after_request
def apply_config(response):
    response.headers['server'] = "Python @ehkoqtau"
    return response

@app.route('/')
@app.route('/home')
@app.route('/home/<int:number>')
def index(number = 1):
    m_rumus_mtk = Lingkaran()
    m_rumus_mtk.setRadius(number)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        m_rumus_mtk = m_rumus_mtk
    )

@app.route('/dashboard')
def dashboard():
    if session:
        data = {
                'username' : session['username']
            }
        return render_template(
            'dashboard.html',
            title='Dashboard',
            year=datetime.now().year,
            data = data
        )
    else:
        flash('Anda belum masuk')
        return render_template(
                'login.html',
                title='Login',
                year=datetime.now().year
            )

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.values.get('username') == 'ehkoqtau' and request.values.get('password') == '234':
		#if request.values.get('username') and request.values.get('password'):
			session['username'] = request.form['username']
			return redirect(url_for('dashboard'))
		else:
			flash('User atau password salah')
			return render_template(
                'login.html',
                title='Login',
                year=datetime.now().year
            )
	else:
		flash('Masuk')
		return render_template(
            'login.html',
            title='Login',
            year=datetime.now().year,
            message='Halaman Login'
        )

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))