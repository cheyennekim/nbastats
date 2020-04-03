from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app, session_options={'autocommit': False})

import models


@app.route('/')
def all_players():
     players = models.Player.query.all()
     return render_template('first.html', players=players)


@app.route('/allplayers')
def allplayer_page():
    players = models.IsOn.query.join(models.Player, models.IsOn.player == models.Player.name)\
    	.add_columns(models.IsOn.player, models.IsOn.team, models.Player.age)
    return render_template('allplayers.html', players=players)

@app.route('/allteams')
def allteams_page():
	teams = models.Teams.query.join(models.CoachedBy, models.Teams.teamabv == models.CoachedBy.team)\
		.add_columns(models.Teams.teamname, models.Teams.teamabv, models.CoachedBy.coach)
	return render_template('allteams.html', teams=teams)

@app.route('/<some_player>')
def some_player_page(some_player):
	PlayerAdv = models.PlayerAdvOff.query.filter_by(name=some_player).first()
	Player = models.PlayerOff.query.filter_by(name=some_player).first()
	pD = models.PlayerDef.query.filter_by(name=some_player).first()


	# index = {0: "ppg", 1: "apg", 2: "tov", 3: "orpg", 4: "fgper", 5: "minutes", 6: "THptAr", 7: "TWptmr", 8: "THptr", 9: "fbpsr", 10: "ftr", 11: "pipr", 12: "fgmUass", 13: "THptAtt", 14: "THptper", 15: "ftAtt", 16: "ftper", 17: "THptperD", 18: "drPts", 19: "drPer", 20: "casPts", 21: "casPer", 22: "pullPts", 23: "pullPer", 24: "postPts", 25: "postPer", 26: "elbPts", 27: "elbPer", 28: "drpg", 29: "drebPer", 30: "spg", 31: "bpg", 32: "oppPoT", 33: "oppPsec", 34: "oppPIP", 35: "eightPer", 36: "sixTwentyPer", 37: "twenFourPer", 38: "gp", 39: "fgDiffPer", 40: "touches", 41: "fcTouch", 42: "timeOfpos", 43: "avgSecTouch", 44: "ppTouch", 45: "elbowTouch", 46: "postUps", 47: "paintTouch", 48: "ppElb", 49: "ppPost", 50: "ppPaint", 51: "drives", 52: "dFGA", 53: "dFGper", 54: "dpts", 55: "dPassPer", 56: "dAstPer", 57: "dTovPer", 58: "dFoulPer"}
	
	# sevFiveCheck = models.check(some_player, 75.0, 20.0)
	# sevFive = []
	# twenty = []

	# for x in range(len(sevFiveCheck)):
	# 	if sevFiveCheck[x] == 1:
	# 		sevFive.append(x)
	# 	if sevFiveCheck[x] == -1:
	# 		twenty.append(x)


	# ninetyCheck = models.check(some_player, 90.0, 10.0)
	# ninety = []
	# ten = []

	# for x in range(len(ninetyCheck)):
	# 		if ninetyCheck[x] == 1:
	# 			ninety.append(x)
	# 		if ninetyCheck[x] == -1:
	# 			ten.append(x)

	tot = "test"
	type1="test"
	percentFG = "test"
	boo="test"




	return render_template('player.html', player = Player, player1 = PlayerAdv, pDef = pD, str = tot, type = type1, last = percentFG, verdict = boo)
	# return render_template('player.html')

@app.route('/allteams/<some_team>')
def teams_page(some_team):
	Teams= db.session.execute('WITH temp1 as (select * from Teams, CoachedBy where Teams.teamabv = :val and Teams.teamabv = CoachedBy.team), temp2 as (select * from coaches) select * from temp1, temp2 where temp2.name = temp1.coach', {'val': some_team}).first()
	players = db.session.execute('select * from isOn where team= :val', {'val': some_team})
	return render_template('team.html', team=Teams, players=players)

@app.route('/search/<searched_player>')
def search_page(searched_player):
    player = models.PlayerOff.query.filter_by(name=searched_player).first()
    return render_template('search.html', player = player)
