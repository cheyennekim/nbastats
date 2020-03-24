from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

import models

@app.route('/')
def all_players():
     players = models.Player.query.all()
     return render_template('first.html', players=players)
<<<<<<< HEAD

@app.route('/<some_player>')
def some_player_page(some_player):
	Spec_player = models.Player.query.filter_by(name=some_player).first()
	# Spec_player_OffStat = models.OffStat.query.filter_by(name=some_player).first()
	return render_template('player.html', player = Spec_player)
=======
>>>>>>> 961d73a7d655f3c1e39d88d53fa2a0e9578b0740
