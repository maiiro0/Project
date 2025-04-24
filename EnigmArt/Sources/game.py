#Projet: Enigm'art
#Auteur: Elouan Bardy, Samuel Lallemand, Elena Longuet, Nathan Ghesquière


import arcade,random

#initialisation
Hauteur = 1000
Largeur = 1200
VITESSE_DEPLACEMENT = 5


#class et fonction du programme
class MyGame(arcade.Window) :
    '''class de la fenêtre principale qui gère tout les jeux'''

    def __init__ (self, Largeur, Hauteur):
        super().__init__(Largeur, Hauteur, "Jeu")
        self.background = None

        self.set_mouse_visible(True)
        self.Cercle = Cercle(610, 530, 0, 0, 30, arcade.color.RED,0)
        self.Simons = Simons()
        self.scene = 0
        self.ePress = False
        self.iPress = False
        self.fleche = None
        self.Dessin = Dessin()
        self.Dance = danse()
        self.jeuxfinis = 0

    def setup(self):
        self.background = arcade.load_texture("../Data/Principal.png")

    def on_draw(self):
        '''méthode qui gère tout ce qui doit être dessiné dans chacun des jeux'''
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, Largeur, Hauteur, self.background)
        if self.jeuxfinis==3:
                output1=f"Félicitations, vous avez résolu les 3 énigmes !!"
                arcade.draw_text(output1,175, 950, arcade.color.WHITE, 30)

        if self.Dance.inGuithero != True:
            if not (self.Dessin.enigme1 or self.Dessin.enigme2 or self.Dessin.enigme3 or self.Dessin.enigme4):
                self.Cercle.draw()
        else:
           self.Dance.draw()
        if self.scene == 1:
            self.Simons.draw()

        if self.scene == 3:
            self.Dessin.draw()

            #affichage des indices
        if self.iPress== True :
            if self.scene==1:
                 # Affiche la regle de la scene 1
                output0=f"Salle Musique:"
                output1=f"Dans cette vous jouez à un jeu de reproduction de paternr musical."
                output2=f"Retenez la séquence sonore et reproduisez là en appuyant sur E, l'erreur est accapeté."
                output3=f"Rendez vous sur le S et appuyé sur E pour déclencher la séquence."
                output4=f"Rendez vous sur la couleur correspondante et recommencez pour compléter les 8 manches."

                arcade.draw_text(output0,500, 950, arcade.color.WHITE, 25)   #format: texte,x,y,couleur,taille en px
                arcade.draw_text(output1,10, 920, arcade.color.WHITE, 15)
                arcade.draw_text(output2,10, 900, arcade.color.WHITE, 15)
                arcade.draw_text(output3,10, 880, arcade.color.WHITE, 15)
                arcade.draw_text(output4,10, 860, arcade.color.WHITE, 15)

            if self.scene==0:
                # Affiche la regle salle principal
                output0=f"Salle principale:"
                output1=f"Bienvenue dans EnigmArt !"
                output2=f"Ce jeu est conçu pour faire réflechir sur l'art et comment celui-ci peut être représenté en informatique."
                output3=f"Votre objectif est de parcourir différentes salles représentant différents arts où vous trouverez des minis-jeu ."
                output4=f"Suivez les chemins pour entrer dans différentes salles."
                output5=f"Réussi chacun des minis-jeu disponibles pour gagner."
                output6=f"Jeux Réussis:",self.jeuxfinis,"/3"

                arcade.draw_text(output0,500, 950, arcade.color.WHITE, 25)
                arcade.draw_text(output1,10, 920, arcade.color.WHITE, 15)
                arcade.draw_text(output2,10, 900, arcade.color.WHITE, 15)
                arcade.draw_text(output3,10, 880, arcade.color.WHITE, 15)
                arcade.draw_text(output4,10, 860, arcade.color.WHITE, 15)
                arcade.draw_text(output5,10, 840, arcade.color.WHITE, 15)
                arcade.draw_text(output6,10, 820, arcade.color.WHITE, 15)

            if self.scene==2:
                # Affiche la regle salle Dance
                output0=f"Salle de Danse:"
                output1=f"Dans cette salle vous allez devoir cliquer sur les flèches avec le bon rythme."
                output2=f"Avancez sur le tapis de danse alumé et appuyez sur E."
                output3=f"Appuyez sur les flèches en rythme avec celles qui défiles."
                output4=f"Atteignez un score de 75000 pour gagner."

                arcade.draw_text(output0,500, 950, arcade.color.WHITE, 25)
                arcade.draw_text(output1,10, 920, arcade.color.WHITE, 15)
                arcade.draw_text(output2,10, 900, arcade.color.WHITE, 15)
                arcade.draw_text(output3,10, 880, arcade.color.WHITE, 15)
                arcade.draw_text(output4,10, 860, arcade.color.WHITE, 15)

            if self.scene==3:
                # Affiche la regle salle Dessin
                output0=f"Salle de Dessin:"
                output1=f"Dans cette salle vous allez devoir reproduire des paternes."
                output2=f"Avancez sur l'un des quatres paternes au sol, puis appuyez sur E."
                output3=f"Reproduisez le paterne de droite en cliquant avec la souris sur les cases du paterne de gauche."
                output4=f"Attention chaque case cliquée change l'état des cases adjacentes."
                output5=f"Finissez les quatres paternes pour gagner"

                arcade.draw_text(output0,500, 950, arcade.color.WHITE, 25)
                arcade.draw_text(output1,10, 920, arcade.color.WHITE, 15)
                arcade.draw_text(output2,10, 900, arcade.color.WHITE, 15)
                arcade.draw_text(output3,10, 880, arcade.color.WHITE, 15)
                arcade.draw_text(output4,10, 860, arcade.color.WHITE, 15)
                arcade.draw_text(output5,10, 840, arcade.color.WHITE, 15)



    def update(self, delta_time):
        '''méthode qui gère tout les changements de variable du programme ainsi que tout ce qui ce passe par actualisation de l'image'''
        if self.Dance.inGuithero != True: #on actualise pas les déplacements dans ce minijeu
            self.Cercle.update(self) #ici self == window
        self.scene = self.Cercle.scene
        if self.scene == 1:
            self.Simons.update(self.scene, self, self.ePress, (self.Cercle.position_x,self.Cercle.position_y))
        if self.scene == 2:
            self.Dance.update(self.scene,self.Cercle.position_x, self.Cercle.position_y, self, self.ePress, self.fleche, self.jeuxfinis)
        if self.scene == 3:
            self.Dessin.update(self.scene,self.Cercle.position_x, self.Cercle.position_y, self, self.ePress,self.jeuxfinis)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.Cercle.change_x = -VITESSE_DEPLACEMENT
            self.fleche = 'g'
        elif key == arcade.key.RIGHT:
            self.Cercle.change_x = VITESSE_DEPLACEMENT
            self.fleche = 'd'
        elif key == arcade.key.UP:
            self.Cercle.change_y = VITESSE_DEPLACEMENT
            self.fleche = 'h'
        elif key == arcade.key.DOWN:
            self.Cercle.change_y = -VITESSE_DEPLACEMENT
            self.fleche = 'b'
        elif key == arcade.key.E:
            self.ePress = True
        elif key == arcade.key.I:
            self.iPress = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.Cercle.change_x = 0
            self.fleche = None
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.Cercle.change_y = 0
            self.fleche = None
        elif key == arcade.key.E:
            self.ePress = False
        elif key == arcade.key.I:
            self.iPress = False

    def on_mouse_press(self, x, y, button, modifiers):
        if self.scene == 3: #souris utilisé que par l'égnime 3   cet fonction peut être codé dans la classe dessin mais par simplicité et étant la seule salle l'utilisant l'utilité n'a pas été trouvé
           if self.Dessin.enigme1 == True: #chercher que parmis la grille 1
              for case in self.Dessin.grille1Enigme1.grille:
                  for i in range(4):
                      if case[i].image.collides_with_point((x,y)) == True: #utitlisation de la fonctio, integrer dans la librairie pour simplification
                         self.Dessin.grille1Enigme1.clicksurID(case[i].id)
                         self.Dessin.nbCoups -= 1
           if self.Dessin.enigme2 == True: #chercher que parmis la grille 2
              for case in self.Dessin.grille1Enigme2.grille:
                  for i in range(4):
                      if case[i].image.collides_with_point((x,y)) == True:
                         self.Dessin.grille1Enigme2.clicksurID(case[i].id)
                         self.Dessin.nbCoups -= 1
           if self.Dessin.enigme3 == True: #chercher que parmis la grille 3
              for case in self.Dessin.grille1Enigme3.grille:
                  for i in range(4):
                      if case[i].image.collides_with_point((x,y)) == True:
                         self.Dessin.grille1Enigme3.clicksurID(case[i].id)
                         self.Dessin.nbCoups -= 1
           if self.Dessin.enigme4 == True: #chercher que parmis la grille 4
              for case in self.Dessin.grille1Enigme4.grille:
                  for i in range(4):
                      if case[i].image.collides_with_point((x,y)) == True:
                         self.Dessin.grille1Enigme4.clicksurID(case[i].id)
                         self.Dessin.nbCoups -= 1


class Cercle:
    '''méthode gérant le personnage'''
    def __init__(self, position_x, position_y, change_x, change_y, rayon, couleur,scene):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.couleur = couleur
        self.scene=scene

    def draw(self):
        arcade.draw_circle_filled(self.position_x,self.position_y,self.rayon,self.couleur)

    def update(self,window):

        self.position_y += self.change_y
        self.position_x += self.change_x
        if self.scene==0: #salle principale

            if self.position_x<75:
                #mur gauche
                    self.position_x=75
            if self.position_y<105:
                #mur bas
                    self.position_y=105

            if self.position_y>900: #mur haut
                if  510<self.position_x<695 :
                    #rentrer dans le Simons
                    if self.position_y>1000:
                        self.scene=1
                        newBackground(window,window.Cercle.scene)
                        self.position_y=10
                        self.position_x=555
                elif 90<self.position_x<275:
                    #rentrer dans le Dessin
                    if self.position_y>1000:
                        self.scene=3
                        newBackground(window,window.Cercle.scene)
                        self.position_y=10
                        self.position_x=555
                else:
                    self.position_y=900


            if self.position_x>1110:    #mur droit
                if 430<self.position_y<605:
                    #rentrer dans la Danse
                    if self.position_x>1200:
                        self.scene=2
                        newBackground(window,window.Cercle.scene)
                        self.position_y=530
                        self.position_x=10
                else:
                    self.position_x=1110


        if self.scene==1: #salle simon

            if self.position_y>900:
                #mur haut
                self.position_y=900
            if self.position_x<110:
                #mur gauche
                    self.position_x=110
            if self.position_x>1085:
                #mur droit
                    self.position_x=1085
            if self.position_y<=130:
                #mur bas
                if 450<self.position_x<670: # test sortie
                    if self.position_y<0:
                        self.scene=0
                        newBackground(window,window.Cercle.scene)
                        self.position_y=990
                        self.position_x=605
                else:
                    self.position_y=130


        if self.scene==2: #salle danse
            if self.position_y>900:
                #mur haut
                self.position_y=900
            if self.position_x>1085:
                #mur droit
                self.position_x=1085
            if self.position_y<=130:
                #mur bas
                self.position_y=130
            if self.position_x<110:
                #mur gauche
                if 440<self.position_y<625: # test sortie
                    if self.position_x<0:
                        self.scene=0
                        newBackground(window,window.Cercle.scene)
                        self.position_y=515
                        self.position_x=1190
                else:
                    self.position_x=110

        if self.scene==3: #salle dessin
            if self.position_y>900:
                #mur haut
                self.position_y=900
            if self.position_x<110:
                #mur gauche
                self.position_x=110
            if self.position_x>1085:
                #mur droit
                self.position_x=1085
            if self.position_y<=130:
                #mur bas
                if 450<self.position_x<670: # test sortie
                    if self.position_y<0:
                        self.scene=0
                        newBackground(window,window.Cercle.scene)
                        self.position_y=990
                        self.position_x=185
                else:
                    self.position_y=130

class Simons():
    def __init__(self):
        self.Lcouleur = ['Jaune', 'Rouge', 'Vert', 'Bleu']
        self.sequence = [self.Lcouleur[random.randint(0,3)] for i in range(8)]
        self.LsoundLoad = [arcade.load_sound("../Data/"+self.Lcouleur[i]+'.wav') for i in range(4)]
        self.etape = 1
        self.etapeReussi = 0
        self.etapeJoueur = 0
        self.compteur = 0
        self.sequenceAff = False
        self.sequenceEC = False #en cours d'affichage
        self.enigme=False
        self.point = [PointSimons((805,815)),PointSimons((955,690)),PointSimons((945,360)),PointSimons((800,190)),
        PointSimons((370,190)),PointSimons((200,325)),PointSimons((205,675)),PointSimons((365,810))]

    def draw(self):
        if self.sequenceAff == True:
            for i in range(self.etapeReussi + 1):

                self.point[i].draw()
        if self.enigme:
            output0=f"Epruve Réussite"
            arcade.draw_text(output0,500, 950, arcade.color.WHITE, 25)

    def update(self, scene, window, ePress,postion):
        if scene == 1 and not self.enigme:
            if ((ePress == True and (500<window.Cercle.position_x<660 and 435<window.Cercle.position_y<570))or self.sequenceEC) and not self.sequenceAff:
                self.sequenceEC=True
                if not self.sequenceAff:
                    if 0<=self.compteur<10:
                        newBackground(window,1)
                        self.compteur += 1
                        if not self.LsoundLoad[self.Lcouleur.index(self.sequence[self.etape-1])].is_playing(arcade.play_sound(self.LsoundLoad[self.Lcouleur.index(self.sequence[self.etape-1])])):
                            arcade.play_sound(self.LsoundLoad[self.Lcouleur.index(self.sequence[self.etape-1])])
                    else:
                        window.background=arcade.load_texture("../Data/"+self.sequence[self.etape-1]+'.png')
                        self.compteur += 1
                        if self.compteur > 100:   #valeur modifiable en fonction du temps qu'on veut afficher
                            if self.etape -1 < self.etapeReussi :
                                self.etape += 1
                                self.compteur = 0
                            else:
                                newBackground(window,1)
                                self.compteur = 0
                                self.sequenceAff = True
                                self.sequenceEC = False
            elif self.sequenceAff == True:
                self.compteur += 1
                couleur = estInCouleur(postion) #fonction à coder qui renvoie une couleur si sur une case de la couleur et none s'il n'y est pas
                if couleur in self.Lcouleur:
                    if couleur == self.sequence[self.etapeJoueur] and ePress == True and not 0<=self.compteur<25:
                        if not self.LsoundLoad[self.Lcouleur.index(self.sequence[self.etapeJoueur])].is_playing(arcade.play_sound(self.LsoundLoad[self.Lcouleur.index(self.sequence[self.etapeJoueur])])):
                            arcade.play_sound(self.LsoundLoad[self.Lcouleur.index(self.sequence[self.etapeJoueur])])
                        self.point[self.etapeJoueur].changeEnVert()
                        self.etapeJoueur += 1
                        self.compteur = 0

                        if self.etapeJoueur == self.etape:
                            self.etapeReussi +=1
                            if self.etapeReussi<8:
                                self.mettrePointAZero()
                                self.sequenceAff = False
                                self.etape=1
                                self.etapeJoueur = 0

                            else:
                                self.enigme = True
                                self.sequenceAff = False
                                window.jeuxfinis += 1

    def mettrePointAZero(self):
        for i in range(self.etapeReussi):
            self.point[i].changeEnRouge()


class danse:
    def __init__(self):
        self.Lfleche = [FlecheDanse(random.randint(0,3)) for i in range(25)] #liste de 25 fleche choisi au hasard répété x fois nécessaires
        self.i = 0 #i variable pour savoir où on se trouve dans la liste des flèches et donc qu'elle est la prochaine à afficher
        self.compteur = 0 #compteur pour afficher les fleches
        self.score = 0 #score du joueur
        self.inGuithero = False #true si dans le guitare hero
        self.coefVitesse = 1
        self.compteentre = 0
        self.enigme = False


    def draw(self):
        for fleche in self.Lfleche:
            if fleche.flag == 1:
               fleche.draw()
        arcade.draw_text('score' ,1110, 950,arcade.color.WHITE, 15)
        arcade.draw_text(str(self.score),1110,935, arcade.color.WHITE)
        arcade.draw_text('/75000',1110, 900,arcade.color.WHITE, 15)

    def update(self, scene, position_x, position_y,window, ePress, flecheP, jeuxfinis):

        if scene == 2 and not self.enigme:
            #test d'entrée
            if 485 < position_x < 635 and 635<position_y < 790 and ePress == True and self.inGuithero == False and self.compteur > 25:
                window.background = arcade.load_texture('../Data/guithero.png')
                self.i = 0
                self.compteur = 0
                self.score = 0
                self.inGuithero = True


            if self.inGuithero == True:

               #test de sortie
               if ePress == True and not 0<=self.compteur<5:
                   newBackground(window,scene)
                   self.inGuithero = False
                   self.compteur = 0
                   self.coefVitesse = 1
                   self.i=0
                   for fleche in self.Lfleche:
                       fleche.flag = 2

               #mise à jour de la position des flèches
               for fleche in self.Lfleche:
                   fleche.update(self.coefVitesse)

               #ajout d'une nouvelle flèche
               if self.compteur > 90 - (self.coefVitesse*20):
                  self.Lfleche[self.i].flag = 1
                  if self.Lfleche[self.i - 7].flag == 1:
                     self.score -= 500 #a laissé passé la flèche
                  self.Lfleche[self.i -7].flag = 2
                  self.i += 1
                  if self.i == 24:
                     self.i = 0
                     self.coefVitesse += 1
                     if self.coefVitesse ==4:
                        self.coefVitesse = 3
                  self.compteur =0

               #test d'une entrée
               if flecheP is not None:
                    if self.compteentre>10:
                      if flecheP == 'g':
                        Lg=[]
                        for fleche in self.getFlecheAffiche():
                            if fleche[1]==0:
                                Lg.append((fleche[0],fleche[0].distanceABase()))
                      if flecheP == 'h':
                        Lg=[]
                        for fleche in self.getFlecheAffiche():
                            if fleche[1]==1:
                                Lg.append((fleche[0],fleche[0].distanceABase()))
                      if flecheP == 'b':
                        Lg=[]
                        for fleche in self.getFlecheAffiche():
                            if fleche[1]==2:
                                Lg.append((fleche[0],fleche[0].distanceABase()))
                      if flecheP == 'd':
                        Lg=[]
                        for fleche in self.getFlecheAffiche():
                            if fleche[1]==3:
                                Lg.append((fleche[0],fleche[0].distanceABase()))
                      minDist = 1000 #1000 étant la valeur de la hauteur il ne peut pas avoir de distance + grande
                      flecheMin = None
                      for fg in Lg:
                        if fg[1] < minDist:
                            minDist = fg[1]
                            flecheMin = fg[0]
                      if flecheMin is not None:
                        flecheMin.flag = 2
                      if minDist > 175: #a appuyé au dela de la ligne ou a loupé son coup
                         self.score -= 500
                      else:
                         self.score += 750 - minDist
                      self.compteentre = 0
               else:
                    self.compteentre += 1
            self.compteur +=1

            #test de réussite
            if self.score > 75000:
               self.inGuithero = False
               self.enigme = True

               window.jeuxfinis += 1
               newBackground(window, scene)



    def getFlecheAffiche(self):
        '''renvoie la liste des flèches affichés'''
        L=[]
        for fleche in self.Lfleche:
            if fleche.flag == 1:
                L.append((fleche,fleche.colonne))
        return L


class FlecheDanse:
    def __init__(self, colonne):
        y = 945
        if colonne == 0:
            x = 255
            self.sprite = arcade.Sprite('../Data/gauche.png')
        if colonne == 1:
            x = 485
            self.sprite = arcade.Sprite('../Data/haut.png')
        if colonne == 2:
            x = 720
            self.sprite = arcade.Sprite('../Data/bas.png')
        if colonne == 3:
            x = 960
            self.sprite = arcade.Sprite('../Data/droite.png')
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.colonne = colonne
        self.flag = 0 #flag => 0 pas affiché, 1 entrain de descendre, 2 a été joué


    def draw(self):
        self.sprite.draw()
    def update(self, coefVitesse):
        if self.flag == 1:
              vitesseDeplacementBase = 2
              self.sprite.center_y = self.sprite.center_y - (vitesseDeplacementBase * coefVitesse)
        if self.flag ==2:
           self.sprite.center_y = 945
           self.flag = 0

    def distanceABase(self):
        '''Renvoie la distance à la base en y'''
        return abs(self.sprite.center_y - 160)


class PointSimons:
    def __init__(self, position):
        self.position_x = position[0]
        self.position_y = position[1]
        self.couleur = arcade.color.RED_BROWN #rouge = étape en train d'être réussi à l'init forcément pas encore réussi | vert étape réussi
    def draw(self):
        arcade.draw_circle_filled(self.position_x,self.position_y,40, self.couleur)
    def changeEnVert(self):
        self.couleur = arcade.color.GREEN
    def changeEnRouge(self):
        self.couleur = arcade.color.RED_BROWN


class CASE:
    '''/!\ class pour les cases de l'egnime dessin

    L'état est allumé(1) ou éteint(0)
    ID est la position sur la grille à laquelle la case appartient
    '''
    def __init__(self,IDcase, etat: int = 0, x = 0, y = 0):
        self.id=IDcase
        self.etat=etat
        self.image = arcade.Sprite("../Data/Image_case_eteinte.png")
        self.imNoire = arcade.load_texture('../Data/Image_case_eteinte.png')
        self.imBlanc = arcade.load_texture('../Data/Image_case_allumer.png')
        self.image.center_x = x
        self.image.center_y = y
    def getEtat(self):
        return self.etat

    def draw(self):
        self.image.draw()

    def changeEtat(self):
        self.etat = (self.etat + 1)%2
        if self.etat == 1:
           self.image.texture = self.imBlanc

        if self.etat == 0:
           self.image.texture = self.imNoire
    def __str__(self):
        return str(self.etat)

    def setEtat(self,etat):
        self.etat = etat
        if self.etat == 1:
           self.image.texture = self.imBlanc
        if self.etat == 0:
           self.image.texture = self.imNoire

class GRILLE:
    '''Grille de 4x4 d'objet cases'''
    def __init__(self):
        self.grille=[[0,0,0,0] for i in range (4)]
        for ligne in range(4):
            for j in range(4):
                self.grille[ligne][j] = CASE(ligne*4+j,0) #case haut gauche id 0, bas droit id 15

    def clicksurLigneColonne(self, ligne, colonne):
        if colonne == 0 :
            if ligne == 0 : #a cliqué en haut à gauche
                self.grille[ligne][colonne].changeEtat()
                self.grille[ligne+1][colonne].changeEtat()
                self.grille[ligne][colonne+1].changeEtat()
                self.grille[ligne+1][colonne+1].changeEtat()
            elif ligne == 3 : #a cliqué en bas à gauche
                self.grille[ligne][colonne].changeEtat()
                self.grille[ligne-1][colonne].changeEtat()
                self.grille[ligne][colonne+1].changeEtat()
                self.grille[ligne-1][colonne+1].changeEtat()

            else: #a cliqué au milieu à gauche
                self.grille[ligne][colonne].changeEtat()
                self.grille[ligne][colonne+1].changeEtat()
                self.grille[ligne+1][colonne].changeEtat()
                self.grille[ligne+1][colonne+1].changeEtat()
                self.grille[ligne-1][colonne].changeEtat()
                self.grille[ligne-1][colonne+1].changeEtat()

        elif colonne == 3:
            if ligne == 0 : #a cliqué en haut à droite
                self.grille[ligne][colonne].changeEtat()
                self.grille[ligne+1][colonne].changeEtat()
                self.grille[ligne][colonne-1].changeEtat()
                self.grille[ligne+1][colonne-1].changeEtat()
            elif ligne == 3 : #a cliqué en bas à droite
                self.grille[ligne][colonne].changeEtat()
                self.grille[ligne-1][colonne].changeEtat()
                self.grille[ligne][colonne-1].changeEtat()
                self.grille[ligne-1][colonne-1].changeEtat()

            else: #a cliqué au milieu à droite
                self.grille[ligne][colonne].changeEtat()
                self.grille[ligne][colonne-1].changeEtat()
                self.grille[ligne+1][colonne].changeEtat()
                self.grille[ligne+1][colonne-1].changeEtat()
                self.grille[ligne-1][colonne].changeEtat()
                self.grille[ligne-1][colonne-1].changeEtat()



        elif ligne == 0:
            self.grille[ligne][colonne].changeEtat()
            self.grille[ligne][colonne-1].changeEtat()
            self.grille[ligne][colonne+1].changeEtat()
            self.grille[ligne+1][colonne-1].changeEtat()
            self.grille[ligne+1][colonne].changeEtat()
            self.grille[ligne+1][colonne+1].changeEtat()

        elif ligne == 3:
            self.grille[ligne][colonne].changeEtat()
            self.grille[ligne][colonne-1].changeEtat()
            self.grille[ligne][colonne+1].changeEtat()
            self.grille[ligne-1][colonne-1].changeEtat()
            self.grille[ligne-1][colonne].changeEtat()
            self.grille[ligne-1][colonne+1].changeEtat()

        else:


            self.grille[ligne][colonne].changeEtat()
            self.grille[ligne][colonne-1].changeEtat()
            self.grille[ligne][colonne+1].changeEtat()
            self.grille[ligne+1][colonne].changeEtat()
            self.grille[ligne+1][colonne-1].changeEtat()
            self.grille[ligne+1][colonne+1].changeEtat()
            self.grille[ligne-1][colonne].changeEtat()
            self.grille[ligne-1][colonne-1].changeEtat()
            self.grille[ligne-1][colonne+1].changeEtat()

    def clicksurID(self, IDcase):
        #donc la casse dans la grille ligne: id//4, colonne id%4
        ligne = IDcase // 4
        colonne = IDcase % 4
        self.clicksurLigneColonne(ligne,colonne)

    def setEtatID(self,IDcase, etat):
        self.grille[IDcase//4][IDcase%4].setEtat(etat)

    def setCoord(self,IDcase, coord):
        self.grille[IDcase//4][IDcase%4].image.center_x = coord[0]
        self.grille[IDcase//4][IDcase%4].image.center_y = coord[1]
    def getEtat(self, ligne, colonne):
        return self.grille[ligne][colonne].getEtat()

    def __str__(self):
        chaine = '   '
        for ligne in range(4):
            for colonne in range(4):
                chaine = chaine + str(self.grille[ligne][colonne]) + '   '
            chaine = chaine + '\n   '
        return chaine

class Dessin:
    def __init__(self):
        self.position_x1  = 125  #position des cases de gauche
        self.position_y1  = 640 #position des cases de droite
        self.position_x2  = 815  #position des cases de gauche
        self.position_y2  = 640 #position des cases de droite
        self.nbCoups = 0

        self.compteApresReussite = 0

        self.enigme1 = False
        self.enigme2 = False
        self.enigme3 = False
        self.enigme4 = False

        self.grille1Enigme1 = construireGrilleParList([1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,0],listeCoordonneeCase(self.position_x1,self.position_y1,[]))
        self.grille2Enigme1 = construireGrilleParList([1,0,0,1,1,1,0,1,1,0,1,1,1,0,0,1],listeCoordonneeCase(self.position_x2,self.position_y2,[]))

        self.grille1Enigme2 = construireGrilleParList([1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0],listeCoordonneeCase(self.position_x1,self.position_y1,[]))
        self.grille2Enigme2 = construireGrilleParList([0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],listeCoordonneeCase(self.position_x2,self.position_y2,[]))

        self.grille1Enigme3 = construireGrilleParList([1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1],listeCoordonneeCase(self.position_x1,self.position_y1,[]))
        self.grille2Enigme3 = construireGrilleParList([1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1],listeCoordonneeCase(self.position_x2,self.position_y2,[]))

        self.grille1Enigme4 = construireGrilleParList([0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,1],listeCoordonneeCase(self.position_x1,self.position_y1,[]))
        self.grille2Enigme4 = construireGrilleParList([1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1],listeCoordonneeCase(self.position_x2,self.position_y2,[]))



    def draw(self):
        if self.enigme1 == True:
           for case in self.grille1Enigme1.grille:
               for i in range(4):
                  case[i].draw()
           for case in self.grille2Enigme1.grille:
               for i in range(4):
                  case[i].draw()

        if self.enigme2 == True:
           for case in self.grille1Enigme2.grille:
               for i in range(4):
                  case[i].draw()
           for case in self.grille2Enigme2.grille:
               for i in range(4):
                  case[i].draw()

        if self.enigme3 == True:
           for case in self.grille1Enigme3.grille:
               for i in range(4):
                  case[i].draw()
           for case in self.grille2Enigme3.grille:
               for i in range(4):
                  case[i].draw()

        if self.enigme4 == True:
           for case in self.grille1Enigme4.grille:
               for i in range(4):
                  case[i].draw()
           for case in self.grille2Enigme4.grille:
               for i in range(4):
                  case[i].draw()

        if self.enigme1 == True or self.enigme2 == True or self.enigme3 == True or self.enigme4 == True:
            if not self.nbCoups == "réussi":
                if self.nbCoups == 1:
                    arcade.draw_text(str(self.nbCoups),590, 540, arcade.color.WHITE, 35)
                    arcade.draw_text("coup",575, 500, arcade.color.WHITE, 20)
                    arcade.draw_text("restant",560, 460, arcade.color.WHITE, 20)
                else:
                   arcade.draw_text(str(self.nbCoups),590, 540, arcade.color.WHITE, 35)
                   arcade.draw_text("coups",568, 500, arcade.color.WHITE, 20)
                   arcade.draw_text("restant",560, 460, arcade.color.WHITE, 20)
            else:
                arcade.draw_text(self.nbCoups,565, 540, arcade.color.WHITE, 20)

        if not (self.enigme1 or self.enigme2 or self.enigme3 or self.enigme4):
            if self.enigme1 == None :
                arcade.draw_text("Réussi !",250, 870, arcade.color.GREEN, 40)
            if self.enigme2 == None :
                arcade.draw_text("Réussi !",740, 870, arcade.color.GREEN, 40)
            if self.enigme3 == None :
                arcade.draw_text("Réussi !",250, 495, arcade.color.GREEN, 40)
            if self.enigme4 == None :
                arcade.draw_text("Réussi !",740, 495, arcade.color.GREEN, 40)

    def update(self, scene, position_x, position_y,window, ePress, jeuxfinis):
        if scene == 3:
            if 190 < position_x < 485 and 566<position_y < 835 and ePress == True and self.enigme1 is not None:
                print(1)
                window.background = arcade.load_texture('../Data/Jeu_dessin.png')
                self.nbCoups = 1
                self.enigme1 = True

            if 665 < position_x < 975 and 565<position_y < 825 and ePress == True and self.enigme2 is not None:
                window.background = arcade.load_texture('../Data/Jeu_dessin.png')
                self.nbCoups = 2
                self.enigme2 = True

            if 190 < position_x < 470 and 195<position_y < 445 and ePress == True and self.enigme3 is not None:
                window.background = arcade.load_texture('../Data/Jeu_dessin.png')
                self.nbCoups = 3
                self.enigme3 = True

            if 670 < position_x < 965 and 185 <position_y < 445 and ePress == True and self.enigme4 is not None:
                window.background = arcade.load_texture('../Data/Jeu_dessin.png')
                self.nbCoups = 3
                self.enigme4 = True

            if self.nbCoups == 0:
                if self.enigme1 == True:
                   if grilleEgale(self.grille1Enigme1, self.grille2Enigme1) and self.compteApresReussite == 0:
                      print(2)
                      self.compteApresReussite = 1
                      self.nbCoups = "réussi"
                   else:
                        self.grille1Enigme1 = construireGrilleParList([1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,0],listeCoordonneeCase(self.position_x1,self.position_y1,[]))
                        self.nbCoups = 1

                if self.enigme2 == True:
                   if grilleEgale(self.grille1Enigme2, self.grille2Enigme2) and self.compteApresReussite == 0:
                      self.compteApresReussite = 1
                      self.nbCoups = "réussi"
                   else:
                        self.grille1Enigme2 = construireGrilleParList([1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0],listeCoordonneeCase(self.position_x1,self.position_y1,[]))
                        self.nbCoups = 2

                if self.enigme3 == True:
                   if grilleEgale(self.grille1Enigme3, self.grille2Enigme3) and self.compteApresReussite == 0:
                      self.compteApresReussite = 1
                      self.nbCoups = "réussi"
                   else:
                        self.grille1Enigme3 = construireGrilleParList([1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1],listeCoordonneeCase(self.position_x1,self.position_y1,[]))
                        self.nbCoups = 3

                if self.enigme4 == True:
                   if grilleEgale(self.grille1Enigme4, self.grille2Enigme4) and self.compteApresReussite == 0:
                      self.compteApresReussite = 1
                      self.nbCoups = "réussi"
                   else:
                        self.grille1Enigme4 = construireGrilleParList([0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,1],listeCoordonneeCase(self.position_x1,self.position_y1,[]))
                        self.nbCoups = 3

            if self.compteApresReussite > 0:
               if self.compteApresReussite > 50:
                  if self.enigme1 == True:
                     self.enigme1 = None
                  if self.enigme2 == True:
                     self.enigme2 = None
                  if self.enigme3 == True:
                     self.enigme3 = None
                  if self.enigme4 == True:
                     self.enigme4 = None
                  newBackground(window,3)
                  if self.enigme1 ==None and self.enigme2 == None and self.enigme3 == None and self.enigme4 == None :
                     window.jeuxfinis +=1
                  self.compteApresReussite = 0
               else:
                    self.compteApresReussite += 1






def construireGrilleParList(liste, listecoord):
    grille = GRILLE()
    for i in range (len(liste)):
        grille.setEtatID(i,liste[i])
        grille.setCoord(i,listecoord[i])
    return grille


def grilleEgale(grille1,grille2):
    for i in range (4):
        for j in range(4):
            if grille1.getEtat(i,j) != grille2.getEtat(i,j):
                return False

    return True

def estInCouleur(position):
    # test jaune
    if 435<position[0]<720 and 205<position[1]<395:
        return 'Jaune'
    if 705<position[0]<935 and 390<position[1]<620:
        return 'Bleu'
    if 450<position[0]<700 and 615<position[1]<810:
        return 'Rouge'
    if 245<position[0]<450 and 385<position[1]<605:
        return 'Vert'
    return None



def newBackground(window,scene):
    if scene==0:
        window.background=arcade.load_texture("../Data/Principal.png")
    if scene==1:
        window.background=arcade.load_texture("../Data/Simons.png")
    if scene==2:
        window.background=arcade.load_texture("../Data/Danse.png")
    if scene==3:
        window.background=arcade.load_texture("../Data/Dessin.png")

def listeCoordonneeCase(position_x ,position_y ,listeCase):
    for j in range(4):
        position_x1 = position_x
        for i in range(4):
            listeCase.append((position_x1,position_y))
            position_x1 = position_x1 + 90
        position_y = position_y - 90

    return listeCase





def main():

    window = MyGame(Largeur, Hauteur)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
