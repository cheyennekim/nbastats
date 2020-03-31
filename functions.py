import models

def threeShooter(x):
	advOff = models.advOff.query.filter_by(name=player).first()
	off = models.offStat.query.filter_by(name=player).first()
	if off.THptper > 35.0:
		return 5.0
	else:
		return 2.0