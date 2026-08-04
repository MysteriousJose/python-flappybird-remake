
from cmu_graphics import *
### Directions ###
# Welcome To Flappy Bird #
# Click Play to start the simulation, #
# The bird is controlled by mouseY, #
# The goal is to get your score as high as possible, #
# Your score will increase after every pillar, #
# the game ends if you collide with any of the pillars. #

### GOOD LUCK ###

###TODO###
# Change Jump Value Depending on level and score
# Test Gavity based on score and level

#Defining All Variables
#Anything used in more than one function is here and needs app. to be global#
#app.open()
app.stepsPerSecond=30
app.playerAlive=True
app.pillarMove=-3
app.pillarWait=0
app.birdY=0
app.admin=False
app.cloudWait=0
app.gameStart=False
app.pillarAccel=0
app.levelSelected=1
app.playPressed=False
app.restartCheck=True
app.colorSelected=1
app.cityColor=1
app.targetAngle=0
app.ai=False
upcomingPipe=None

minGapSelected = {
    1:175,
    2:150,
    3:125
}
maxGapSelected = {
    1:275,
    2:250,
    3:225
}


###                #
highScoreLevel = { #Change These For High Score Change
    1:52,          #Easy
    2:46,          #Medium
    3:66           #Hard
}                  #
###                #
gapScaler = {
    1:2,
    2:3,
    3:4
}

speedScaler = {
    1:1,
    2:1.25,
    3:1.5
}

JumpScaler = {
    1:8,
    2:10,
    3:12
}

speedLimiter = {
    1:-8,
    2:-10,
    3:-12
}
backColor = {
    1:rgb(61,165,255),
    2:'black'
}
cityColor = {
    1:None,
    2:'yellow'
}

app.highScore=highScoreLevel[app.levelSelected]
# Background #
app.background=backColor[app.colorSelected]
Rect(0,250,400,200, fill=rgb(42,185,62))
Rect(0,200,400,50, fill=rgb(241,240,238))

# Definineing all objects #
#Groups Folded For easy of use#
#Group Clouds#
clouds = Group(
    Oval(0,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(25,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(50,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(75,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(100,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(125,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(150,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(175,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(200,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(225,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(250,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(275,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(300,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(325,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(350,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(375,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(400,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(425,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    Oval(450,200,80,50, rotateAngle=randrange(-30,30), fill=rgb(241,240,238)),
    
    Oval(0,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(25,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(50,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(75,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(100,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(125,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(150,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(175,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(200,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(225,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(250,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(275,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(300,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(325,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(350,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(375,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(400,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(425,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
    Oval(450,250,80,50, rotateAngle=randrange(-30,30), fill=rgb(42,185,62)),
)
#Group Title Screen#
title = Group(
    Label("Flappy",65,60, size=45, rotateAngle=-45, bold=True, border=rgb(237,249,217), borderWidth=2, fill=rgb(156,231,89), font='orbitron'),
    Label("Bird",100,95, size=45, rotateAngle=-45, bold=True,border=rgb(237,249,217), borderWidth=2, fill=rgb(156,231,89), font='orbitron'),
    Rect(125,280,150,80, fill=rgb(249,164,73)),
    Label("PLAY",200,320,bold=True, border=rgb(237,249,217), borderWidth=2, fill=rgb(156,231,89), font='orbitron', size=45)
)
#Group City#

city = Group(
    Rect(0,300,20,100, fill='darkGrey'),
    Rect(20,340,20,100, fill='darkGrey'),
    Rect(40,375,20,100, fill='darkGrey'),
    Rect(60,310,20,100, fill='darkGrey'),
    Rect(80,340,20,100, fill='darkGrey'),
    Rect(100,310,20,100, fill='darkGrey'),
    Rect(120,300,20,100, fill='darkGrey'),
    Rect(140,340,20,100, fill='darkGrey'),
    Rect(160,375,20,100, fill='darkGrey'),
    Rect(180,310,20,100, fill='darkGrey'),
    Rect(200,340,20,100, fill='darkGrey'),
    Rect(220,310,20,100, fill='darkGrey'),
    Rect(240,300,20,100, fill='darkGrey'),
    Rect(260,340,20,100, fill='darkGrey'),
    Rect(280,375,20,100, fill='darkGrey'),
    Rect(300,310,20,100, fill='darkGrey'),
    Rect(320,340,20,100, fill='darkGrey'),
    Rect(340,310,20,100, fill='darkGrey'),
    Rect(360,310,20,100, fill='darkGrey'),
    Rect(380,340,20,100, fill='darkGrey'),
    Rect(400,310,20,100, fill='darkGrey')
)
# Group Windows #
window = Group(
    Line(10,300,10,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(2,4)),
    Line(30,340,30,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(1,4)),
    Line(50,375,50,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(3,4)),
    Line(70,310,70,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(2,4)),
    Line(90,340,90,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(1,4)),
    Line(110,310,110,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(6,4)),
    Line(130,300,130,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(2,4)),
    
    Line(150,340,150,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(1,4)),
    Line(170,375,170,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(3,4)),
    Line(190,310,190,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(2,4)),
    Line(210,340,210,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(1,4)),
    Line(230,310,230,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(6,4)),
    Line(250,300,250,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(2,4)),
    
    Line(270,340,270,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(1,4)),
    Line(290,375,290,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(3,4)),
    Line(310,310,310,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(2,4)),
    Line(330,340,330,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(1,4)),
    Line(350,310,350,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(6,4)),
    Line(370,310,370,400,fill=cityColor[app.cityColor], lineWidth=20, dashes=(2,4)),
    Line(390,340,390,400,fill=cityColor[app.cityColor],lineWidth=20,dashes=(1,4))
    )

    
#Group Bird#
bird = Group(
    
)
body = Oval(130,65, 30,20, fill=gradient(rgb(248,255,46),rgb(249,241,36),rgb(249,194,44), start='top'),border=rgb(83,56,70), borderWidth=1, visible=False)
bird.add(body)
bird.add(Oval(139,62, 8,9, fill=rgb(253,255,250), rotateAngle=-60, border=rgb(83,56,70), borderWidth=1),
    Oval(140,62,3,3, fill=rgb(83,56,70)),
    Oval(120,60,12,8, fill=gradient(rgb(250,252,233),rgb(248,255,46), start='top'),border=rgb(83,56,70), borderWidth=1, rotateAngle=15),
    Line(135,70, 140,68, fill=rgb(232,80,64)),
    Line(140,68,147,68, fill=rgb(232,80,64)))
pillars = Group(
    )
ovals = Group(
    )
bird.visible=False
city.visible=False
window.visible=False
nightTime = Rect(0,0,400,400, fill='black', opacity=60,visible=False)
score = Label(-1,375,20, fill='white', size=40, visible=False, bold=True)
lose = Label('You Lose!', 200,200, fill='red', size=70, visible=False)
loading = Label("Loading...", 200,200, fill='Black', size=60, visible=False, bold=True)
go = Label("GO!", 200,200, fill='black', size=70, visible=False, bold=True)
highScore = Label(0,125,20, fill='white', size=40, visible=False, bold=True)
labels = Group(Label('Highscore:', 50,20, fill='white', size=20),
Label('Score:', 320,20, fill='white', size=20))
labels.visible=False
#hiddenScore used for speedup timing#
hiddenScore = Label(-1,200,40,fill=None, size=0, visible=False)

# hide menu and start Game logic/Functions #
def start():
    bird.visible=True
    bird.centerY=200
    title.visible=False
    pillar()
    app.gameStart=True
    app.playerAlive=True
    score.visible=True
    city.visible=True
    window.visible=True
    pillars.visible=True
    ovals.visible=True
    nightTime.visible=False
    app.colorSelected=1
    app.cityColor=1
    bird.rotateAngle=0
    highScore.visible=True
    labels.visible=True
    app.highScore=highScoreLevel[app.levelSelected]
def spawnPowerUp():
    y=randrange(50,350)
    powerup=Oval(400,y20,20, fill='gold', border='orange', borderWidth=20)
    powerup.add(powerup)
    
def pillar():
    #Draw The pillars using randrange for the height variation
    shrinkMulti=gapScaler[app.levelSelected]
    #height = randrange(20,260)
    minGap=minGapSelected[app.levelSelected]
    maxGap=maxGapSelected[app.levelSelected]-app.pillarAccel
    shrinkRate = score.value*shrinkMulti
    gap = max(minGap,maxGap-shrinkRate)
    height = randrange(20,260)
    bottomStart= height+gap
    app.val1=height
    app.val2=bottomStart
    
    
    
    pillars.add(Rect(365,0,40,height,fill='darkGreen'))
    pillars.add(Rect(360,0,40,height,fill=rgb(104,138,50)))
    ovals.add(Oval(385,height+10,60,25,fill='darkGreen'))
    ovals.add(Oval(380,height+10, 60,25, fill=rgb(104,138,50)))
    
    
    
    pillars.add(Rect(365,bottomStart,40,400-height,fill='darkGreen'))
    pillars.add(Rect(360,bottomStart,40,400-height,fill=rgb(104,138,50)))
    ovals.add(Oval(385,bottomStart-10,60,25,fill='darkGreen'))
    ovals.add(Oval(380,bottomStart-10, 60,25, fill=rgb(104,138,50)))
    pass
#speedup#
def speedup():
    speedMulti=speedScaler[app.levelSelected]
    baseSpeed=-3
    
    #print(baseSpeed)
    speedIncrease=min(score.value*-0.3,-4)*speedMulti
    #print(speedIncrease)
    app.pillarMove = baseSpeed + speedIncrease
    app.pillarAccel = min(score.value*2.5,30)
    if hiddenScore.value==10:
        hiddenScore.value=0
        if app.colorSelected==1:
            app.colorSelected=2
            app.cityColor=2
            nightTime.visible=True
        else:
            app.colorSelected=1
            app.cityColor=1
            nightTime.visible=False
        
#Bird Controls mouseControls #
#def onMouseMove(mouseX,mouseY):
 #   bird.centerY=mouseY 
    #checking if we can go faster evey time the mouse is moved, only runs if score is a multiple of ten
  #  speedup()
  
#Button Functions #
def onMousePress(mouseX,mouseY):
    if app.playPressed == False and mouseX>125 and mouseX<275 and mouseY<360 and mouseY>280 and app.gameStart==False:
        app.playPressed=True
        app.Select = Group()
        app.tempBack = Rect(0,0,400,400, fill='peachPuff', border=rgb(237,249,217))
        app.btn1 = Rect(0,240,100,80, fill='lightGreen',border=rgb(237,249,217))
        app.btn2 = Rect(150,240,100,80, fill='khaki',border=rgb(237,249,217))
        app.btn3 = Rect(300,240,100,80, fill='darkSalmon',border=rgb(237,249,217))
        app.lbl1 = Label('Easy', 47,280, size=24, fill='green',border=rgb(237,249,217))
        app.lbl2 = Label('Medium', 200,280, size=24, fill='gold', bold=True,border=rgb(237,249,217))
        app.lbl3 = Label('Hard', 350,280, size=24, fill='fireBrick',border=rgb(237,249,217))
        app.btn9 = Rect(40,40,320,80, fill=rgb(61,165,255),border=rgb(237,249,217))
        app.lbl9 = Label("Select Your Level", 200,80, fill=rgb(156,231,89),font='orbitron', bold=True, size=30,border=rgb(237,249,217))
        sleep(0.5)
    elif app.playPressed==True:
        if app.btn1.contains(mouseX,mouseY):#Fill for button area
            app.Select.visible=False
            app.levelSelected=1
            app.playPressed=False
            app.Select.add(app.tempBack,app.btn1,app.btn2,app.btn3,app.btn9,app.lbl1,app.lbl2,app.lbl3,app.lbl9)
            start()
            app.Select.visible=False
        if app.btn2.contains(mouseX,mouseY):#Fill for button area
            app.Select.visible=False
            app.levelSelected=2
            app.playPressed=False
            app.Select.add(app.tempBack,app.btn1,app.btn2,app.btn3,app.btn9,app.lbl1,app.lbl2,app.lbl3,app.lbl9)
            start()
            app.Select.visible=False
        if app.btn3.contains(mouseX,mouseY):#Fill for button area
            app.Select.visible=False
            app.levelSelected=3
            app.playPressed=False
            app.Select.add(app.tempBack,app.btn1,app.btn2,app.btn3,app.btn9,app.lbl1,app.lbl2,app.lbl3,app.lbl9)
            start()
            app.Select.visible=False
        
    app.birdY=9 
    speedup()
    
    if app.restartCheck==False:
        sleep(.5)
        pillars.visible=False
        pillars.clear()
        ovals.visible=False
        ovals.clear()
        app.playerAlive=True
        bird.centerY=200
        score.value=-1
        hiddenScore.value=-1
        app.pillarMove=-3
        app.pillarAccel=0
        lose.visible=False
        app.restartCheck=True
        app.pillarWait=0
        loading.visible=True
        sleep(randrange(1,5))
        loading.visible=False
        go.visible=True
        sleep(0.1)
        go.visible=False
        start()
        
def onKeyPress(key):
    if key =='a':
        app.admin=True
    if key =='s':
        app.admin=False
    if key =='p':
        app.ai=True
    if key == 'space':
        app.birdY=9
        if app.restartCheck==False:
            sleep(.5)
            pillars.visible=False
            pillars.clear()
            ovals.visible=False
            ovals.clear()
            app.playerAlive=True
            bird.centerY=200
            score.value=-1
            hiddenScore.value=-1
            app.pillarMove=-3
            app.pillarAccel=0
            lose.visible=False
            app.restartCheck=True
            app.pillarWait=0
            loading.visible=True
            sleep(randrange(1,5))
            loading.visible=False
            go.visible=True
            sleep(0.1)
            go.visible=False
            start()
    
        
# Precedural Clouds and adding pillar Functions #
def onStep():
    if app.ai==True:
        target_pipe_top = None
        Target_pipe_bottom = None
        for i in range(0,len(pillars.children),4):
            pipe_check = pillars.children[i]
            
            if pipe_check.right >bird.left:
                target_pipe_top = pipe_check
                target_pipe_bottom = pillars.children[i+2]
                break
            
        if target_pipe_top !=None:
            safety_buffer = 15
            targetY=(target_pipe_top.bottom+target_pipe_bottom.top)/2 + safety_buffer
        
            if bird.centerY>targetY and app.birdY<1:
                app.birdY=9
                print(target_pipe_top)
            #    print(bird.centerY)
            #elif targetY<bird.centerY:
             #   bird.centerY-=2
              #  print(bird.centerY)
            #else:
             #   app.birdY=0
    #print(app.pillarMove)
    speedMulti=JumpScaler[app.levelSelected]
    JumpLevel=min(score.value*-0.3,-4)*speedMulti
    app.highScore=highScoreLevel[app.levelSelected]
    highScore.value=app.highScore
    if score.value>app.highScore:
        highScoreLevel[app.levelSelected]=score.value
    baseInterval=25
    minInterval=20
    Interval=max(minInterval, baseInterval - score.value*0.5)
    speedup()
    if app.pillarAccel>30:
        app.pillarAccel=30
    if app.pillarMove<speedLimiter[app.levelSelected]:
        app.pillarMove=speedLimiter[app.levelSelected]

    bird.centerY-=app.birdY
    
    
    if app.birdY<0.1:
        app.targetAngle=25
        app.birdY-=1
        
    if app.birdY>0.1:
        app.targetAngle=-25
        app.birdY-=0.95
    bird.rotateAngle+=(app.targetAngle - bird.rotateAngle) *0.4
    if app.birdY==0:
        bird.rotateAngle=0
    if bird.rotateAngle>25:
        bird.rotateAngle=25
    if bird.rotateAngle<-25:
        bird.rotateAngle=-25
        
    if app.birdY <=-12:
        app.birdY=-12
        
    app.background=backColor[app.colorSelected]
    window.fill=cityColor[app.cityColor]
    if app.cloudWait>6:
        for cloud in clouds:
            cloud.rotateAngle=randrange(-30,30)
        app.cloudWait=0
    for cloud in clouds:
        cloud.centerX+=app.pillarMove/2
        if cloud.right <0:
            cloud.centerX=450
    if app.gameStart==True:
        #Collisions#
        if score.value>0:
            if body.hitsShape(pillars) and app.admin==False:
                lose.visible=True 
                app.playerAlive=False
                app.gameStart=False
                app.playPressed=False
                app.restartCheck=False
            
        #move the pillars
        pillars.centerX+=app.pillarMove
        ovals.centerX+=app.pillarMove
        for p in list(pillars.children):
            if p.right <0:
                p.visible=False
                pillars.remove(p)
        for o in list(ovals.children):
            if o.right <0:
                o.visible=False
                ovals.remove(o)
        
        app.pillarWait+=1
        #Spawn new pillars and update score
        if app.pillarWait>=Interval and app.playerAlive==True:
            pillar()
            score.value+=1
            hiddenScore.value+=1
            app.pillarWait=0
        app.cloudWait+=1
cmu_graphics.run()