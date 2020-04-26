from sqlalchemy import sql, orm
from app import db
import math
import os
import numpy as np
from statistics import mean, median
from scipy import stats
import difflib
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go


# def makePlt(name):
#     plt.compOff(name)


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

class touchDrives(db.Model):
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

class mesA(db.Model):
    __tablename__ = 'mesA'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    yearStart = db.Column('yearStart', db.Float)
    position = db.Column('position', db.String(80))
    wingspan = db.Column('wingspan', db.Float)
    standReach = db.Column('standReach', db.Float)
    handLen = db.Column('handLen', db.Float)
    handWid = db.Column('handWid', db.Float)
    bodyFat = db.Column('bodyFat', db.Float)
    college = db.Column('college', db.String(80))

class mesB(db.Model):
    __tablename__ = 'mesB'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    pick = db.Column('pick', db.Float)
    vert = db.Column('vert', db.String(80))
    vertNostep = db.Column('vertNostep', db.Float)
    bodyFat = db.Column('bodyFat', db.Float)
    bench = db.Column('bench', db.Float)
    agility = db.Column('agility', db.Float)
    sprint = db.Column('sprint', db.Float)

class mesC(db.Model):
    __tablename__ = 'mesC'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name', db.String(20), db.ForeignKey('player'), primary_key=True)
    age = db.Column('age', db.Float)
    height = db.Column('height', db.String(80))
    weight = db.Column('weight', db.Float)

class salary(db.Model):
    __tablename__ = 'salaries'
    __table_args__ = {'extend_existing': True}
    name = db.Column('Player', db.String(20), db.ForeignKey('player'), primary_key=True)
    rank = db.Column('Rank', db.Float)
    nineteen = db.Column('Nineteen', db.Float)
    twenty = db.Column('Twenty', db.Float)
    twentyOne = db.Column('TwentyOne', db.Float)
    twentyTwo = db.Column('TwentyTwo')

    
def games(playername):
    __table_args__ = {'extend_existing': True}
    defPlayer = PlayerDef.query.filter_by(name=playername).first()
    return defPlayer.gp

def avg(att):
    lst = []
    lstAtt = []
    lstNms = []

    def2 = PlayerDef.query.filter(PlayerDef.gp>5).all()
    for y in def2:
        lst.append(y.name)
    q1 = PlayerOff.query.filter(PlayerOff.name.in_(lst)).all()
    for x in q1:
        lstAtt.append(x.att)
        lstNms.append(x.name)
    return mean(lstAtt)


def setDic():
    playDict = {}
    off = PlayerOff.query.all()
    #all playerOff instances in offStat table
    def1 = PlayerDef.query.all()
    #all playerDef instances in defStat table
    off2 = PlayerAdvOff.query.all()
    #all playerAdvOff instances in advOff table
    off3 = touchDrives.query.all()

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
            if k.gp < 7:
                playDict[k.name].append(0)
            else:
                playDict[k.name].append(1)
            playDict[k.name].append(k.fgDiffPer) 
        else:
            playDict[k.name] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
    for x,y in playDict.items():
        if (len(y) != 41):
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
    for k in off3:
        if k.name in playDict:
            playDict[k.name].append(k.touches) 
            playDict[k.name].append(k.fcTouch)
            playDict[k.name].append(k.timeOfpos)  
            playDict[k.name].append(k.avgSecTouch) 
            playDict[k.name].append(k.ppTouch) 
            playDict[k.name].append(k.elbowTouch) 
            playDict[k.name].append(k.postUps)
            playDict[k.name].append(k.paintTouch)
            playDict[k.name].append(k.ppElb)  
            playDict[k.name].append(k.ppPost)  
            playDict[k.name].append(k.ppPaint) 
            playDict[k.name].append(k.drives) 

            playDict[k.name].append(k.dFGA) 
            playDict[k.name].append(k.dFGper)
            playDict[k.name].append(k.dpts)
            playDict[k.name].append(k.dPassPer)  
            playDict[k.name].append(k.dAstPer)  
            playDict[k.name].append(k.dTovPer) 
            playDict[k.name].append(k.dFoulPer) 
        else:
            playDict[k.name] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x,y in playDict.items():
        if (len(y) != 60):
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
  
    return playDict
dic = setDic()
testlist=[]
stat_list = []
#stat_list in form of: [ (1, (3.0, 4.5, 5.0)), (2, (6.0, 2.0, 4.9))] with first num representing what statistic and list representing all values from all players
df = pd.DataFrame(data=dic)

for i in range((df.shape[0])): 
    #this is to input NBA wholistic data to calculate individual percentiles
    stat_list.append((i,[]))
    for x in range(df.shape[1]):
        if (df.iloc[39, x] == 1) and (df.iloc[5, x] > 5):
            stat_list[i][1].append(df.iloc[i,x])

def setPhysdic():
    dict = {}
    MA = mesA.query.all()
    MB = mesB.query.all()
    MC = mesC.query.all()

    for p in MC:
        dict[p.name] = [p.age, p.height, p.weight]
    for x in MA:
        if x.name in dict:
            dict[x.name].append(x.yearStart)
            if x.position == 'G':
                dict[x.name].append(0)
            elif x.position == 'F-G' or x.position == 'G-F':
                dict[x.name].append(1)
            elif x.position == 'F':
                dict[x.name].append(2)
            elif x.position == 'F-C' or x.position == 'C-F':
                dict[x.name].append(3)
            elif x.position == 'C':
                dict[x.name].append(4)
            else:
                dict[x.name].append(5)
            dict[x.name].append(x.wingspan)
            dict[x.name].append(x.standReach)
            dict[x.name].append(x.handLen)
            dict[x.name].append(x.handWid)
            dict[x.name].append(x.bodyFat)
        else:
            dict[x.name] = [0,0,0]
            dict[x.name].append(x.yearStart)
            if x.position == 'G':
                dict[x.name].append(0)
            elif x.position == 'F-G' or x.position == 'G-F':
                dict[x.name].append(1)
            elif x.position == 'F':
                dict[x.name].append(2)
            elif x.position == 'F-C' or x.position == 'C-F':
                dict[x.name].append(3)
            elif x.position == 'C':
                dict[x.name].append(4)
            else:
                dict[x.name].append(5)
            dict[x.name].append(x.wingspan)
            dict[x.name].append(x.standReach)
            dict[x.name].append(x.handLen)
            dict[x.name].append(x.handWid)
            dict[x.name].append(x.bodyFat)
    for k in MB:
        if k.name in dict:
            if len(dict[k.name]) == 3:
                dict[k.name].append(0)
                dict[k.name].append(0)
                dict[k.name].append(0)
                dict[k.name].append(0)
                dict[k.name].append(0)
                dict[k.name].append(0)
                dict[k.name].append(0)
            dict[k.name].append(k.pick) 
            dict[k.name].append(k.vert)
            dict[k.name].append(k.vertNostep) 
            dict[k.name].append(k.bodyFat) 
            dict[k.name].append(k.bench) 
            dict[k.name].append(k.agility) 
            dict[k.name].append(k.sprint) 
        else:
            dict[k.name] = [0,0,0,0,0,0,0,0,0,0]
            dict[k.name].append(k.pick) 
            dict[k.name].append(k.vert)
            dict[k.name].append(k.vertNostep) 
            dict[k.name].append(k.bodyFat) 
            dict[k.name].append(k.bench) 
            dict[k.name].append(k.agility) 
            dict[k.name].append(k.sprint)

    for x,y in dict.items():
        if len(y) == 3:
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
        if len(y) == 10:
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)
            dict[x].append(0)

    return dict
dict2 = setPhysdic()
dfPhys = pd.DataFrame(data=dict2)
l = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def setSalDic():
    dict = {}
    sal = salary.query.all()
    for p in sal:
        dict[p.name] = [p.rank, p.nineteen, p.twenty, p.twentyOne, p.twentyTwo]
    return dict

dict3 = setSalDic()
dfSal = pd.DataFrame(data=dict3)
#player names are columns, years salaries are rows

# print("what we got", stats.percentileofscore(stat_list[28][1], 9))
# print("what old got", stats.percentileofscore(testlist, 9))
def percentile(playerName):
    ans = []
    for i in range(df.shape[0]):
        # print("stat: ", df.loc[i,playerName])
        num = round(stats.percentileofscore((stat_list[i][1]), df.loc[i,playerName]), 2)
        # print("perc: ", num)
        ans.append(num)
    return ans
# print(percentile("James Harden"))

def checkerG(name, good):
    index = {0: "ppg", 1: "apg", 2: "tov", 3: "orpg", 4: "fgper", 5: "minutes", 6: "THptAr", 7: "TWptmr", 8: "THptr", 9: "fbpsr", 10: "ftr", 11: "pipr", 12: "fgmUass", 13: "THptAtt", 14: "THptper", 15: "ftAtt", 16: "ftper", 17: "THptperD", 18: "drPts", 19: "drPer", 20: "casPts", 21: "casPer", 22: "pullPts", 23: "pullPer", 24: "postPts", 25: "postPer", 26: "elbPts", 27: "elbPer", 28: "drpg", 29: "drebPer", 30: "spg", 31: "bpg", 32: "oppPoT", 33: "oppPsec", 34: "oppPIP", 35: "eightPer", 36: "sixTwentyPer", 37: "twenFourPer", 38: "gp", 40: "fgDiffPer", 41: "touches", 42: "fcTouch", 43: "timeOfpos", 44: "avgSecTouch", 45: "ppTouch", 46: "elbowTouch", 47: "postUps", 48: "paintTouch", 49: "ppElb", 50: "ppPost", 51: "ppPaint", 52: "drives", 53: "dFGA", 54: "dFGper", 55: "dpts", 56: "dPassPer", 57: "dAstPer", 58: "dTovPer", 59: "dFoulPer"}
    check1 = percentile(name)
    lstG = []
    for x in range(len(check1)):
        if x != 39:
            if check1[x] > good:
                lstG.append((check1[x], index[x], x))
    return lstG

# print(checkerG("James Harden", 90))

def checkerB(name, bad):
    index = {0: "ppg", 1: "apg", 2: "tov", 3: "orpg", 4: "fgper", 5: "minutes", 6: "THptAr", 7: "TWptmr", 8: "THptr", 9: "fbpsr", 10: "ftr", 11: "pipr", 12: "fgmUass", 13: "THptAtt", 14: "THptper", 15: "ftAtt", 16: "ftper", 17: "THptperD", 18: "drPts", 19: "drPer", 20: "casPts", 21: "casPer", 22: "pullPts", 23: "pullPer", 24: "postPts", 25: "postPer", 26: "elbPts", 27: "elbPer", 28: "drpg", 29: "drebPer", 30: "spg", 31: "bpg", 32: "oppPoT", 33: "oppPsec", 34: "oppPIP", 35: "eightPer", 36: "sixTwentyPer", 37: "twenFourPer", 38: "gp", 40: "fgDiffPer", 41: "touches", 42: "fcTouch", 43: "timeOfpos", 44: "avgSecTouch", 45: "ppTouch", 46: "elbowTouch", 47: "postUps", 48: "paintTouch", 49: "ppElb", 50: "ppPost", 51: "ppPaint", 52: "drives", 53: "dFGA", 54: "dFGper", 55: "dpts", 56: "dPassPer", 57: "dAstPer", 58: "dTovPer", 59: "dFoulPer"}
    check1 = check(name)
    lstB = []
    for x in range(len(check1)):
        if check1[x] < bad:
            lstB.append((check1[x], index[x]))
    return lstB

def leagueLead(perc):
    index = {0: "ppg", 1: "apg", 2: "tov", 3: "orpg", 4: "fgper", 5: "minutes", 6: "THptAr", 7: "TWptmr", 8: "THptr", 9: "fbpsr", 10: "ftr", 11: "pipr", 12: "fgmUass", 13: "THptAtt", 14: "THptper", 15: "ftAtt", 16: "ftper", 17: "THptperD", 18: "drPts", 19: "drPer", 20: "casPts", 21: "casPer", 22: "pullPts", 23: "pullPer", 24: "postPts", 25: "postPer", 26: "elbPts", 27: "elbPer", 28: "drpg", 29: "drebPer", 30: "spg", 31: "bpg", 32: "oppPoT", 33: "oppPsec", 34: "oppPIP", 35: "eightPer", 36: "sixTwentyPer", 37: "twenFourPer", 38: "gp", 40: "fgDiffPer", 41: "touches", 42: "fcTouch", 43: "timeOfpos", 44: "avgSecTouch", 45: "ppTouch", 46: "elbowTouch", 47: "postUps", 48: "paintTouch", 49: "ppElb", 50: "ppPost", 51: "ppPaint", 52: "drives", 53: "dFGA", 54: "dFGper", 55: "dpts", 56: "dPassPer", 57: "dAstPer", 58: "dTovPer", 59: "dFoulPer"}
    ans = []
    for x in range(len(perc)):
        if perc[x] == 100.0:
            ans.append((x,index[x]))
    return ans

def iconSet(checkerG, player):
    ftSpecial = "whistle.svg"
    threeBall = "target.svg"
    quickWball = "clockFast.svg"
    driver = "driver.svg"
    pos = "possession.svg"
    time = "time.svg"
    workhorse = "shield.png"
    TO = "warning.svg"
    stateFarm = "assist.svg"
    pt = "paingbrush.png"
    post = "post.png"
    

    linkitylist=[]
    if checkerG[10] > 80:
        linkitylist.append((ftSpecial, "Free Throw Specialist", "Percentage of Points from Free Throws: " + str(df.loc[10,player])))
    if checkerG[14] > 80:
        linkitylist.append((threeBall, "Long Range Specialist", "Three Point Percentage: " + str(df.loc[14,player])))
    if checkerG[18] > 80 and (checkerG[53] > 80 or checkerG[52] > 80):
        linkitylist.append((driver, "Driver", "Driving PPG: " + str(df.loc[18,player])))
    if checkerG[43] > 85:
        linkitylist.append((pos, "Ball Dominant", "Time of Possession per game: " + str(df.loc[43,player])))
    if checkerG[44] > 80:
        linkitylist.append((time, "Ball Holder", "Average Time per possession: " + str(df.loc[44,player])))
    if checkerG[44] < 20:
        linkitylist.append((quickWball, "Hot Potato", "Average Time per possession: " + str(df.loc[44,player])))
    if checkerG[5] > 85:
        linkitylist.append((workhorse, "Work Horse", "Minutes per game: " + str(df.loc[5,player])))
    if checkerG[2] > 85:
        linkitylist.append((TO, "Turnover Hazard", "Turnovers per game: " + str(df.loc[2,player])))
    if checkerG[1] > 85:
        linkitylist.append((stateFarm, "Distributor", "Assists per game: " + str(df.loc[1,player])))
    if checkerG[51] or checkerG[11] > 85:
        linkitylist.append((pt, "Paint Scorer", "Points per paint touch: " + str(df.loc[51,player])))
    if checkerG[24] > 85 or checkerG[47] > 85:
        linkitylist.append((post, "Post Scorer", "Post points per game: " + str(df.loc[24,player])))
    return linkitylist

def iconSetD(perc, player):
    rebound = "rebound.png"
    steal = "stolen.png"
    block = "block.png"
    layup = "layup.png"
    defense = "defense.png"

    lst = []
    if perc[28] > 80:
        lst.append((rebound, "Crashes the Boards", "Defensive Rebounds per game: " + str(df.loc[28,player])))
    if perc[30] > 80:
        lst.append((steal, "Pesky Defender", "Steals per game: " + str(df.loc[30,player])))
    if perc[31] > 80:
        lst.append((block, "Shot Blocker", "Blocks per game: " + str(df.loc[31,player])))
    if perc[34] > 80:
        lst.append((layup, "Paint Liability", "Opponent Points in Paint per game: " + str(df.loc[34,player])))
    if perc[40] > 80:
        lst.append((defense, "Shot Contestor", "Opponent Difference in FG%: " + str(df.loc[40,player]) + "%"))
    return lst
# p = percentile("James Harden")
# print(p)

# print(iconSet(p, "James Harden"))

def pieCharter(some_player):
    plt.close('all')
    labels = 'Free Throws', 'Mid Range', 'Three Pointers', 'Paint', 'Fast Break'
    Player = PlayerOff.query.filter_by(name=some_player).first()
    sizes = [Player.ftr, Player.TWptmr, Player.THptr, Player.pipr, Player.fbpsr]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'magenta']

    # Plot
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    # plt.savefig('/Users/daniellanda/Desktop/NBA_316/nbastats/templates/' + some_player + 'scoreDist.svg')
    strFile = "static/iscoreDist_" + Player.name + ".svg"
    plt.savefig(strFile)
    plt.close()
    return None

def offtopThree(player):
    percentiles = percentile("James Harden")
    offDex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
    first=0
    firstdex=0
    second=0
    seconddex=0
    third=0
    thirddex=0
    lst=[]
    for x in range(len(percentiles)):
        if x in offDex:
            perc = percentiles[x]
            if perc>first:
                first=perc
                firstdex=x
            elif perc>second:
                second=perc
                seconddex=x
            elif perc>third:
                third=perc
                thirddex=x
            else:
                None
    lst.append((firstdex, first))
    lst.append((seconddex, second))
    lst.append((thirddex, third))
    return lst

def offPS(some_player):
    perc = percentile(some_player)
    lst = []
    if perc[8] > 85.0 and perc[16] > 85.0:
        lst.append("Efficient Perimeter Threat")
    elif perc[8] > 90.0:
        lst.append("Does most of his damage beyond the arc")


    if perc[9] > 90.0:
        lst.append("Likes to get out and run in transition")
    if perc[12] > 90.0:
        lst.append("Iso-Heavy")
    if perc[12] < 10.0:
        lst.append("Off-ball threat who scores off assists")
    if perc[10] > 90.0:
        lst.append("Get's to the line")

    if perc[11] > 90.0 and perc[7] > 90.0 and perc[26] > 90.0: 
        lst.append("Does most of his damage in the mid-range, at the elbow, and in the paint")
    elif perc[7] > 90.0 and perc[11] > 90.0:
        lst.append("Does most of his damage in the mid-range and in the paint")
    elif perc[26] > 90.0 and perc[11] > 90.0:
        lst.append("Does most of his damage at the elbow and in the paint")
    elif perc[26] > 90.0 and perc[7] > 90.0:
        lst.append("Does most of his damage in the mid-range and at the elbow")
    elif perc[26] > 90.0:
        lst.append("Does most of his damage at the elbow")
    elif perc[7] > 90.0:
        lst.append("Does most of his damage in the mid-range")
    elif perc[11] > 90.0:
        lst.append("Does most of his damage in the paint")

    if perc[44] > 90.0:
        lst.append("Likes to hold the ball")
    if perc[43] > 90.0:
        lst.append("Offense runs through him")

    if perc[52] > 90.0 and perc[56] > 90.0 and perc[55] > 90.0:
        lst.append("Attacks the basket --> can both finish and find teammates on the drive")  
    elif perc[52] > 90.0 and perc[56] > 90.0:
        lst.append("Likes to attack the basket --> pass-heavy on the drive")
    elif perc[52] > 90.0 and perc[55] > 90.0:
        lst.append("Likes to attack the basket --> shot-heavy on the drive")
    elif perc[52] > 90.0:
        lst.append("Likes to attack the basket")


    if perc[47] > 90.0 or perc[24] > 90.0:
        lst.append("Threat in the post")
    elif perc[46] > 90.0:
        lst.append("His game is revolves around the elbow")


    if perc[20] > 90.0 and perc[22] > 90.0:
        lst.append("Can score via catch & shoot or pull-up")
    elif perc[20] > 90.0:
        lst.append("Catch & shoot scorer")
    elif perc[22] > 90.0:
        lst.append("Pull-up scorer")


    if perc[1] > 90.0:
        lst.append("Finds teammates")



    return lst

# print(offtopThree("James Harden"))
dfScale = df.transpose(copy=True)
p = percentile("James Harden")
# print(p)

# print(iconSet(p, "James Harden"))
scalar = MinMaxScaler()
dfScale[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,28,29,30,31,32,33,34,35,36,37,38,40]] = scalar.fit_transform(dfScale[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,28,29,30,31,32,33,34,35,36,37,38,40]])
rowLabels = dfScale.index.values

dfScale2 = dfPhys.T
for x in range(17):
    if x!=4:
        dfScale2[x].replace([0],[None], inplace = True)

for col in dfScale2.columns:
    if col != 4 and col != 10:
        dfScale2[col]=(dfScale2[col]-dfScale2[col].min())/(dfScale2[col].max()-dfScale2[col].min())
rowLabels2 = dfScale2.index.values

# dfScale2[[0,1,2,3,5,6,7,8,9,11,12,13,14,15,16,17]] = scalar.fit_transform(dfScale2[[0,1,2,3,5,6,7,8,9,11,12,13,14,15,16,17]])
def euc(lst1, lst2):
    sum = 0
    for x in range(len(lst1)):
        minus = lst1[x]-lst2[x]
        sq = minus*minus
        sum+=sq
    return math.sqrt(sum)

def kNearProduction(player, k):
    dfProd = dfScale[[0,1,2,3,4,5,28,29,30,31,32,33,34,40,45]].copy()
    dude = dfProd.loc[player].values.tolist()
    nameDiffs = []
    for x in rowLabels:
        if x != player:
            comp = dfProd.loc[x].values.tolist()
            dist = euc(dude, comp)
            nameDiffs.append((x, dist))
    sort = sorted(nameDiffs, key = lambda x: x[1])
    return sort[:k]

def kNearPhys(player, k):
    df3 = dfScale2[[0, 1, 2, 4]].copy()
    dude = df3.loc[player].values.tolist()
    nameDiffs = []
    for x in rowLabels2:
        if x != player:
            comp = df3.loc[x].values.tolist()
            dist = euc(dude, comp)
            nameDiffs.append((x, dist))
    sort = sorted(nameDiffs, key = lambda x: x[1])
    return sort[:k]

def kNearPlayStyle(player, k):
    None

diction = setDic()
dfTran = pd.DataFrame(data=diction)
dfTran2 = pd.DataFrame(data=diction)
dfdf = dfTran.T 
dfdf2 = dfTran2.T
df2 = dfdf[[19, 23, 21]].copy()
df3 = df2.T

df4 = dfdf2[[14, 27, 4]].copy()
df5 = df4.T



# def compOff(player):
#     my_range=(range(1,len(df3.index)+1))
#     compsA = kNearPhys(player, 20)
#     comps = []
#     for x in compsA:
#         comps.append(x[0])


    # labels = ["fgper", "THptper", "drPer", "casPer", "pullPer", "postPer", "elbPer"]

#     compsDF = df2.loc[comps, :]
#     med = compsDF.median(axis=0)
#     med = med.values.tolist()

#     queryVals = df3["James Harden"].values.tolist()

#     myDFList = [['fg %', med[0], 'Comps'], ['3pt %', med[1], 'Comps'], ['Driveshot %', med[2], 'Comps'], ['Catch & Shoot %', med[3], 'Comps'], ['Pull-up %', med[4], 'Comps'], ['Post-up %', med[5], 'Comps'], ['Elbow %', med[6], 'Comps'], ['fg %', queryVals[0], player], ['3pt %', queryVals[1], player], ['Driveshot %', queryVals[2], player], ['Catch & Shoot %', queryVals[3], player], ['Pull-up %', queryVals[4], player], ['Post-up %', queryVals[5], player], ['Elbow %', queryVals[6], player]]
#     myDF = pd.DataFrame(myDFList, columns=['Stat', 'Percentage', 'Player'])

#     sns.catplot(x='Stat', y='Percentage', hue='Player', data=myDF, kind='bar')
#     plt.show()
    # plt.hlines(y=my_range, xmin=df3[player], xmax=med, color='grey', alpha=0.4)
    # plt.scatter(df3[player], my_range, color='skyblue', alpha=1, label=player)
    # plt.scatter(med, my_range, color='green', alpha=0.4 , label='Comps')
    # plt.legend()
    # plt.yticks(my_range, labels)
    # plt.title("Comparison of the value 1 and the value 2", loc='left')
    # plt.xlabel('Value of the variables')
    # plt.ylabel('Group')

    # strFile = "static/offComps_" + player + ".svg"
    # plt.savefig(strFile)
    # plt.show
    # plt.close()
    # return None

def compOff(player):
    fig = go.Figure()
    compsA = kNearPhys(player, 20)
    comps = []
    for x in compsA:
        comps.append(x[0])


    compsDF = df2.loc[comps, :]
    med = compsDF.median(axis=0)
    med = med.values.tolist()
    queryVals = df3[player].values.tolist()
    print(queryVals)

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = queryVals[0],
        delta = {'reference': med[0]},
        domain = {'x': [0.3, 1], 'y': [0.1, 0.3]},
        title = {'text': "Driving Shot %"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "blue", 'width': 5},
                'thickness': 0.75,
                'value': med[0]},
            'steps': [
                {'range': [0, 20], 'color': "#FFDD00"},
                {'range': [20, 40], 'color': "#FFB300"},
                {'range': [40, 60], 'color': '#FF8000'},
                {'range': [60, 80], 'color': '#FF5500'},
                {'range': [80, 100], 'color': '#FF0000'}],
            'bar': {'color': "black"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = queryVals[1],
        delta = {'reference': med[1]},
        domain = {'x': [0.3, 1], 'y': [0.4, 0.6]},
        title = {'text': "Pull-up %"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "blue", 'width': 5},
                'thickness': 0.75,
                'value': med[1]},
            'steps': [
                {'range': [0, 20], 'color': "#FFDD00"},
                {'range': [20, 40], 'color': "#FFB300"},
                {'range': [40, 60], 'color': '#FF8000'},
                {'range': [60, 80], 'color': '#FF5500'},
                {'range': [80, 100], 'color': '#FF0000'}],
            'bar': {'color': "black"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = queryVals[2],
        delta = {'reference': med[2]},
        domain = {'x': [0.3, 1], 'y': [0.7, 0.9]},
        title = {'text': "Catch & Shoot %"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "blue", 'width': 5},
                'thickness': 0.75,
                'value': med[2]},
            'steps': [
                {'range': [0, 20], 'color': "#FFDD00"},
                {'range': [20, 40], 'color': "#FFB300"},
                {'range': [40, 60], 'color': '#FF8000'},
                {'range': [60, 80], 'color': '#FF5500'},
                {'range': [80, 100], 'color': '#FF0000'}],
            'bar': {'color': "black"}}))


    fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

    strFile = "static/offComps_" + player + ".svg"
    fig.write_image(strFile)
    # print(med)
    # print(queryVals)
    return None

def compOff2(player):
    fig = go.Figure()
    compsA = kNearPhys(player, 20)
    comps = []
    for x in compsA:
        comps.append(x[0])


    compsDF = df4.loc[comps, :]
    med = compsDF.median(axis=0)
    med = med.values.tolist()


    queryVals = df5[player].values.tolist()

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = queryVals[2],
        delta = {'reference': med[2]},
        domain = {'x': [0.3, 1], 'y': [0.1, 0.3]},
        title = {'text': "Field Goal %"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "blue", 'width': 5},
                'thickness': 0.75,
                'value': med[2]},
            'steps': [
                {'range': [0, 20], 'color': "#FFDD00"},
                {'range': [20, 40], 'color': "#FFB300"},
                {'range': [40, 60], 'color': '#FF8000'},
                {'range': [60, 80], 'color': '#FF5500'},
                {'range': [80, 100], 'color': '#FF0000'}],
            'bar': {'color': "black"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = queryVals[1],
        delta = {'reference': med[1]},
        domain = {'x': [0.3, 1], 'y': [0.4, 0.6]},
        title = {'text': "Elbow Shot %"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "blue", 'width': 5},
                'thickness': 0.75,
                'value': med[1]},
            'steps': [
                {'range': [0, 20], 'color': "#FFDD00"},
                {'range': [20, 40], 'color': "#FFB300"},
                {'range': [40, 60], 'color': '#FF8000'},
                {'range': [60, 80], 'color': '#FF5500'},
                {'range': [80, 100], 'color': '#FF0000'}],
            'bar': {'color': "black"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = queryVals[0],
        delta = {'reference': med[0]},
        domain = {'x': [0.3, 1], 'y': [0.7, 0.9]},
        title = {'text': "3pt %"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "blue", 'width': 5},
                'thickness': 0.75,
                'value': med[0]},
            'steps': [
                {'range': [0, 20], 'color': "#FFDD00"},
                {'range': [20, 40], 'color': "#FFB300"},
                {'range': [40, 60], 'color': '#FF8000'},
                {'range': [60, 80], 'color': '#FF5500'},
                {'range': [80, 100], 'color': '#FF0000'}],
            'bar': {'color': "black"}}))


    fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

    strFile = "static/offComps2_" + player + ".svg"
    fig.write_image(strFile)
    # print(med)
    # print(queryVals)
    return None

# p = percentile("James Harden")
# print(p[4])
# print(p[27])
# print(p[24])
# print(p)
# compOff2("James Harden")
def kNearSalary(player, k):
    knear = kNearProduction(player, k)
    nums = []
    for x in knear:
        lst = dfSal[x[0]].tolist()
        nums.append(lst[1])
    return mean(nums)

print(kNearProduction("James Harden", 10))

# print(some_player_page("James Harden"))
# per = checkerG("James Harden", 90)
# print(per)
# print(iconSet(per, "James Harden"))
# print(kNearPhys("JJ Redick", 3))

# print(dfScale.loc[['James Harden']])
# B = pd.Series(dfScale.loc[['LeBron James']])
# xx = dfScale.loc[['LeBron James']]
# y = dfScale.loc[['James Harden']]
# dude = dfScale.loc["Tacko Fall"].values.tolist()
# dude1 = dfScale.loc["LeBron James"].values.tolist()
# print(euc(dude,dude1))
# dude = dfScale.loc["Russell Westbrook"].values.tolist()
# dude1 = dfScale.loc["Russell Westbrook"].values.tolist()
# print(euc(dude,dude1))
#dfScale = MINMAX SCALED VERSION OF DF
# print(dfScale)
# maxi = dfScale.max()

# print(dfScale.max())
# print(dfScale.idxmax())
# data = stat_list[15][1]
# plt.hist(data, bins='auto')
print(dic["Joe Ingles"][14])
print(dic["Joe Ingles"][27])
print(dic["Joe Ingles"][4])
print(percentile("Justin Holiday")[4])

# plt.show()
# for player, numbers in df.iteritems():
#     print(numbers)
# for col in df.columns:
#     print(col)
# df1 = pd.concat(df[', axis=1, keys=headers)
# df.plot.hist(alpha=0.5);
# pro = (kNearProduction("James Harden", 10))
# ls = []
# for x in pro:
#     ls.append(x[0])
#     ls.append(dfSal[x[0]].tolist()[1])
# print(ls)
# print(df3["James Harden"])
# print(df5["James Harden"])
# print(dic["James Harden"][29])

