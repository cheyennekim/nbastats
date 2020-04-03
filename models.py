from sqlalchemy import sql, orm
from app import db
import numpy as np
from statistics import mean, median
from scipy import stats
import difflib




class Player(db.Model):
    __tablename__ = 'players'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name', db.String(20), primary_key=True)
    age = db.Column('age', db.Integer)

class IsOn(db.Model):
    __tablename__ = 'ison'
    __table_args__ = {'extend_existing': True}
    player = db.Column('player', db.String(20), primary_key=True)
    team = db.Column('team', db.String(20),primary_key=True)

class Teams(db.Model):
    __tablename__ = 'teams'
    __table_args__ = {'extend_existing': True}
    teamname = db.Column('teamname', db.String(50), primary_key=True) 
    teamabv = db.Column('teamabv', db.String(50))

class CoachedBy(db.Model):
    __tablename__ = "coachedby"
    __table_args__ = {'extend_existing': True}
    coach = db.Column('coach', db.String(40), primary_key=True)
    team = db.Column('team', db.String(20), primary_key=True)



class PlayerOff(db.Model):
    __tablename__ = 'offStat'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    ppg = db.Column('ppg', db.Float)
    apg = db.Column('apg', db.Float)
    tov = db.Column('tov', db.Float)
    orpg = db.Column('orpg', db.Float)
    fgper = db.Column('fgper', db.Float)

    minutes = db.Column('min', db.Float)
    THptAr = db.Column('3ptAr', db.Float)
    TWptmr = db.Column('2ptmr', db.Float)
    THptr = db.Column('3ptr', db.Float)
    fbpsr = db.Column('fbpsr', db.Float)

    ftr = db.Column('ftr', db.Float)
    pipr = db.Column('pipr', db.Float)
    fgmUass = db.Column('fgmUass', db.Float)
    THptAtt = db.Column('3ptAtt', db.Float)
    THptper = db.Column('3ptper', db.Float)

    ftAtt = db.Column('ftAtt', db.Float)
    ftper = db.Column('ftper', db.Float)
    THptperD = db.Column('3ptperD', db.Float)

    def tester(self):
    	if self.minutes > 10:
    		print("ten")
    		return 10
    	else:
    		print("less")
    		return "less"
class DriveTouch(db.Model):
    __tablename__ = 'touchDrives'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name', db.String(20), db.ForeignKey('player'), primary_key=True)
    touches = db.Column('touches', db.Float)
    fcTouch = db.Column('fcTouch', db.Float)
    timeOfpos = db.Column('timeOfpos', db.Float)
    avgSecTouch = db.Column('avgSecTouch', db.Float)
    ppTouch = db.Column('ppTouch', db.Float)

    elbowTouch = db.Column('elbowTouch', db.Float)
    postUps = db.Column('postUps', db.Float)
    paintTouch = db.Column('paintTouch', db.Float)
    ppElb = db.Column('ppElb', db.Float)
    ppPost = db.Column('ppPost', db.Float)

    ppPaint = db.Column('ppPaint', db.Float)
    drives = db.Column('drives', db.Float)
    dFGA = db.Column('dFGA', db.Float)
    dFGper = db.Column('dFGper', db.Float)
    dpts = db.Column('dpts', db.Float)

    dPassPer = db.Column('dPassPer', db.Float)
    dAstPer = db.Column('dAstPer', db.Float)
    dTovPer = db.Column('dTovPer', db.Float)
    dFoulPer = db.Column('dFoulPer', db.Float)


class PlayerAdvOff(db.Model):
    __tablename__ = 'advOff'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    drPts = db.Column('drPts', db.Float)
    drPer = db.Column('drPer', db.Float)
    casPts = db.Column('casPts', db.Float)
    casPer = db.Column('casPer', db.Float)
    pullPts = db.Column('pullPts', db.Float)
    pullPer = db.Column('pullPer', db.Float)
    postPts = db.Column('postPts', db.Float)
    postPer = db.Column('postPer', db.Float)
    elbPts = db.Column('elbPts', db.Float)
    elbPer = db.Column('elbPer', db.Float)

class PlayerDef(db.Model):
    __tablename__ = 'defStat'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    drpg = db.Column('drpg', db.Float)
    drebPer = db.Column('drebPer', db.Float)
    spg = db.Column('spg', db.Float)
    bpg = db.Column('bpg', db.Float)
    oppPoT = db.Column('oppPoT', db.Float)
    oppPsec = db.Column('oppPsec', db.Float)
    oppPIP = db.Column('oppPIP', db.Float)
    eightPer = db.Column('eightPer', db.Float)
    sixtTwentyPer = db.Column('sixtTwentyPer', db.Float)
    twenFourPer = db.Column('TwenFourPer', db.Float)
    gp = db.Column('gp', db.Float)
    fgDiffPer = db.Column('fgDiffPer', db.Float)
    def __repr__(self):
        return self.name

def setDict():
    defGP = []
    #list of players in defStat with minimum games played: 5
    playDict = {}
    defDict = {}
    off2Dict = {}
    lstPts = []
    lstApg = []
    lstTov = []
    lstOrpg = []
    lstfgper = []
    lstMinutes = []
    lstTHptAr = []
    lstTWptmr = []
    lstTHptr = []
    lstFbpsr = []
    lst = []

    Ans = []

    off = PlayerOff.query.all()
    #all playerOff instances in offStat table
    def1 = PlayerDef.query.all()
    #all playerDef instances in defStat table
    minGP = PlayerDef.query.filter(PlayerDef.gp>8).all()
    #all playerDef instances in defStat table and > 4 gp
    off2 = PlayerAdvOff.query.all()
    #all playerAdvOff instances in advOff table
    off3 = DriveTouch.query.all()


    for r in off:
        playDict[r.name] = [r.ppg, r.apg, r.tov, r.orpg, r.fgper, r.minutes, r.THptAr, r.TWptmr, r.THptr, r.fbpsr, r.ftr, r.pipr, r.fgmUass, r.THptAtt, r.THptper, r.ftAtt, r.ftper, r.THptperD]
    
   
    for p in off2:
        if p.name in playDict:
            playDict[p.name].append(p.drPts) 
            playDict[p.name].append(p.drPer)
            playDict[p.name].append(p.casPts)  
            playDict[p.name].append(p.casPer) 
            playDict[p.name].append(p.pullPts) 
            playDict[p.name].append(p.pullPer) 
            playDict[p.name].append(p.postPts)
            playDict[p.name].append(p.postPer)
            playDict[p.name].append(p.elbPts)  
            playDict[p.name].append(p.elbPer)  
        else:
            playDict[p.name] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            playDict[p.name].append(p.drPts) 
            playDict[p.name].append(p.drPer)
            playDict[p.name].append(p.casPts)  
            playDict[p.name].append(p.casPer) 
            playDict[p.name].append(p.pullPts) 
            playDict[p.name].append(p.pullPer) 
            playDict[p.name].append(p.postPts)
            playDict[p.name].append(p.postPer)
            playDict[p.name].append(p.elbPts)  
            playDict[p.name].append(p.elbPer)  

    for k in def1:
        if k.name in playDict:
            playDict[k.name].append(k.drpg) 
            playDict[k.name].append(k.drebPer)
            playDict[k.name].append(k.spg)  
            playDict[k.name].append(k.bpg) 
            playDict[k.name].append(k.oppPoT) 
            playDict[k.name].append(k.oppPsec) 
            playDict[k.name].append(k.oppPIP)
            playDict[k.name].append(k.eightPer)
            playDict[k.name].append(k.sixtTwentyPer)  
            playDict[k.name].append(k.twenFourPer)  
            playDict[k.name].append(k.gp) 
            playDict[k.name].append(k.fgDiffPer) 
        else:
            playDict[k.name] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            playDict[k.name].append(k.drpg) 
            playDict[k.name].append(k.drebPer)
            playDict[k.name].append(k.spg)  
            playDict[k.name].append(k.bpg) 
            playDict[k.name].append(k.oppPoT) 
            playDict[k.name].append(k.oppPsec) 
            playDict[k.name].append(k.oppPIP)
            playDict[k.name].append(k.eightPer)
            playDict[k.name].append(k.sixtTwentyPer)  
            playDict[k.name].append(k.twenFourPer)  
            playDict[k.name].append(k.gp) 
            playDict[k.name].append(k.fgDiffPer) 
    for p in off3:
        if p.name in playDict:
            playDict[p.name].append(p.touches) 
            playDict[p.name].append(p.fcTouch) 
            playDict[p.name].append(p.timeOfpos)
            playDict[p.name].append(p.avgSecTouch)  
            playDict[p.name].append(p.ppTouch) 
            playDict[p.name].append(p.elbowTouch) 
            playDict[p.name].append(p.postUps) 
            playDict[p.name].append(p.paintTouch)
            playDict[p.name].append(p.ppElb)
            playDict[p.name].append(p.ppPost)  
            playDict[p.name].append(p.ppPaint)
            playDict[p.name].append(p.drives) 
            playDict[p.name].append(p.dFGA) 
            playDict[p.name].append(p.dFGper)
            playDict[p.name].append(p.dpts)
            playDict[p.name].append(p.dPassPer)  
            playDict[p.name].append(p.dAstPer)
            playDict[p.name].append(p.dTovPer)  
            playDict[p.name].append(p.dFoulPer)

    return playDict
dic = setDict()

def games(playername):
    defPlayer = PlayerDef.query.filter_by(name=playername).first()
    return defPlayer.gp

def ppg(percentile):
    lst = []
    lstPts = []
    lstNms = []
    dict2 = {}
    pts=0
    denom=0
    off1 = PlayerOff.query.all()
    def1 = PlayerDef.query.all()
    def2 = PlayerDef.query.filter(PlayerDef.gp>5).all()
    off2 = PlayerAdvOff.query
    for y in def2:
        lst.append(y.name)

    # joiner = db.Model.query(PlayerOff, PlayerDef).outerjoin(PlayerDef, PlayerOff.name==PlayerDef.name).all()
    q1 = PlayerOff.query.filter(PlayerOff.name.in_(lst)).all()
    for x in q1:
        lstPts.append(x.ppg)
        lstNms.append(x.name)
    # for player in q1: 
    #     pts+=player.ppg
    #     denom+=1
    return np.percentile(lstPts, percentile)

def avg(att):
    lst = []
    lstAtt = []
    lstNms = []
    dict2 = {}
    pts=0
    denom=0
    off1 = PlayerOff.query.all()
    def1 = PlayerDef.query.all()
    def2 = PlayerDef.query.filter(PlayerDef.gp>5).all()
    off2 = PlayerAdvOff.query
    for y in def2:
        lst.append(y.name)

    # joiner = db.Model.query(PlayerOff, PlayerDef).outerjoin(PlayerDef, PlayerOff.name==PlayerDef.name).all()
    q1 = PlayerOff.query.filter(PlayerOff.name.in_(lst)).all()
    for x in q1:
        lstAtt.append(x.att)
        lstNms.append(x.name)
    # for player in q1: 
    #     pts+=player.ppg
    #     denom+=1
    return mean(lstAtt)


    

def percentile(playerName, statDex):
    defGP = []
    #list of players in defStat with minimum games played: 5
    defDict = {}
    off2Dict = {}
    lstPts = []
    lstApg = []
    lstTov = []
    lstOrpg = []
    lstfgper = []
    lstMinutes = []
    lstTHptAr = []
    lstTWptmr = []
    lstTHptr = []
    lstFbpsr = []
    lst = []

    Ans = []


    minGP = PlayerDef.query.filter(PlayerDef.gp>8).all()
    #all playerDef instances in defStat table and > 4 gp


    

    for y in minGP:
        defGP.append(y.name)
    
    
    for x, v in dic.items():
        #to create a list of all ppgs
        if x in defGP:
            lst.append(v[statDex])

    correct = dic[playerName]


    return round((stats.percentileofscore(lst, correct[statDex])), 2)

def check(playerName):
    ans = []
    for x in range(59):
        ans.append(percentile(playerName, x))
        # if percentile(playerName, x) > perGood:
        #     ans.append(1)
        # elif percentile(playerName, x) < perBad:
        #     ans.append(-1)
        # else:
        #     ans.append(0)
    return ans

def printer(playerName):
    index = {0: "ppg", 1: "apg", 2: "tov", 3: "orpg", 4: "fgper", 5: "minutes", 6: "THptAr", 7: "TWptmr", 8: "THptr", 9: "fbpsr", 10: "ftr", 11: "pipr", 12: "fgmUass", 13: "THptAtt", 14: "THptper", 15: "ftAtt", 16: "ftper", 17: "THptperD", 18: "drPts", 19: "drPer", 20: "casPts", 21: "casPer", 22: "pullPts", 23: "pullPer", 24: "postPts", 25: "postPer", 26: "elbPts", 27: "elbPer", 28: "drpg", 29: "drebPer", 30: "spg", 31: "bpg", 32: "oppPoT", 33: "oppPsec", 34: "oppPIP", 35: "eightPer", 36: "sixTwentyPer", 37: "twenFourPer", 38: "gp", 39: "fgDiffPer", 40: "touches", 41: "fcTouch", 42: "timeOfpos", 43: "avgSecTouch", 44: "ppTouch", 45: "elbowTouch", 46: "postUps", 47: "paintTouch", 48: "ppElb", 49: "ppPost", 50: "ppPaint", 51: "drives", 52: "dFGA", 53: "dFGper", 54: "dpts", 55: "dPassPer", 56: "dAstPer", 57: "dTovPer", 58: "dFoulPer"}
    check1 = check(playerName)
    for x in range(len(check1)):
        if check1[x] > 90.0:
            print(index[x], check1[x])
        if check1[x] < 20.0:
            print(index[x], check1[x])
    
print(printer("Patrick Beverley"))





       
    






        