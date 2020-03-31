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

@app.route('/<some_player>')
def some_player_page(some_player):
	PlayerAdv = models.PlayerAdvOff.query.filter_by(name=some_player).first()
	Player = models.PlayerOff.query.filter_by(name=some_player).first()
	pD = models.PlayerDef.query.filter_by(name=some_player).first()

	string = Player.tester()

	if Player.THptAr > 60.0:
		type1 = "yes"
	else:
		type1 = "Two Point Specialist"


	return render_template('player.html', player = Player, player1 = PlayerAdv, pDef = pD, str = string, type = type1)
	# return render_template('player.html')
