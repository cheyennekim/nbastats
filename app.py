from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

import models

@app.route('/')
def all_players():
     players = models.Player.query.all()
     return render_template('first.html', players=players)

@app.route('/<some_player>')
def some_player_page(some_player):
	Spec_player = models.Player.query.filter_by(name=some_player).first()
	# Spec_player_OffStat = models.OffStat.query.filter_by(name=some_player).first()
	return render_template('player.html', player = Spec_player)

