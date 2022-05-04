#-*-coding:utf-8 -*-

import turtle
import winsound 

# Ecran
wn = turtle.Screen()
# Titre
wn.title("Ping par @vinc.flores")
# Fond écran
wn.bgcolor("black")
# Dimensions
wn.setup(width=800, height=600)
# Tracé
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Crosse A (bleue)
paddle_a = turtle.Turtle() # initialisation
paddle_a.speed(0) # vitesse
paddle_a.shape("square") # forme carrée
paddle_a.color("blue") # couleur
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # allongement en hauteur
paddle_a.penup() # aliasing
paddle_a.goto(-360, 0) # emplacement

# Crosse B (rouge)
paddle_b = turtle.Turtle() # initialisation
paddle_b.speed(0) # vitesse
paddle_b.shape("square") # forme carrée
paddle_b.color("red") # couleur
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # allongement en hauteur
paddle_b.penup() # aliasing
paddle_b.goto(360, 0) # emplacement


# Balle
ball = turtle.Turtle() # initialisation
ball.speed(0) # vitesse
ball.shape("circle") # disque
ball.color("pink") # couleur
ball.penup() # aliasing
ball.goto(0, 0) # emplacement
ball.dx = .2
ball.dy = -.2 # new : on change de sens

# Affichage score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # invisible
pen.goto(0, 260) # emplacement
pen.write("Joueur bleu: 0 Joueur rouge: 0", align="center", font=("Courier", 24, "normal"))

# Affichage touches joueurs
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle() # signe rendu invisible
pen2.goto(0, 230) 
pen2.write("[w-s  /  Haut-Bas]".format(score_a, score_b), align="center", font=("Courier", 16, "normal"))
        

# Crosse bleu
# Fonction (déplacement haut de 20px lorsqu'on presse sur la touche z)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
# Fonction (déplacement bas de 20px lorsqu'on presse sur la touche s)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
# Crosse rouge
# Fonction (déplacement haut de 20px)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
# Fonction (déplacement bas de 20px)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Attribution touches
wn.listen()
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Boucle
while True:
    wn.update()
    # Mouvement balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Bordure
    # Ecran fait 800 par 600 (600 - 20 / 2 = 290)
    # Bord supérieur
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # inversion de la direction
        winsound.PlaySound("son/choc-palet.wav", winsound.SND_ASYNC) # son
        
    # Bord inférieur
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        winsound.PlaySound("son/choc-palet.wav", winsound.SND_ASYNC) 
        
    # Bord droit, point marqué et remise en jeu au centre avec inversion de direction.
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("son/alerte.wav", winsound.SND_ASYNC) 
        score_a += 1 # +1 pour le joueur bleu
        pen.clear() # effacement de l'écran pour faire apparaitre le nouveau chiffre
        pen.write("Joueur bleu: {} Joueur rouge: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # affichage reactualisation score
        
    # Même chose, côté gauche cette fois.
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("son/alerte.wav", winsound.SND_ASYNC) 
        score_b += 1 # +1 pour le joueur rouge
        pen.clear()
        pen.write("Joueur bleu: {} Joueur rouge: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    # Si la balle touche le bord haut ou bas, ou qu'elle touche la crosse rouge : rebond de la balle.
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("son/choc-palet.wav", winsound.SND_ASYNC) 
        
    # Même chose, côté gauche de l'écran cette fois.
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("son/choc-palet.wav", winsound.SND_ASYNC) 
        

