#Projet: Enigm'art
#Auteur: Elouan Bardy, Samuel Lallemand, Elena Longuet, Nathan Ghesquière


import game
import arcade

Hauteur = 500
Largeur = 500

def main():

    window = MyGame(Largeur, Hauteur)
    window.setup()
    arcade.run()

class MyGame(arcade.Window) :

    def __init__ (self, Largeur, Hauteur):
        super().__init__(Largeur, Hauteur, "Jeu")
        self.background = None
        self.set_mouse_visible(True)
        self.scene = 0

    def setup(self):
        self.background = arcade.load_texture("../Data/menu.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, Largeur, Hauteur, self.background)


    def on_mouse_press(self, x, y, button, modifiers):
        if self.scene == 0:
            if 100<x<400 and 255<y<380:
                arcade.close_window()
                game.main()
            if 100<x<400 and 90<y<215:
                self.scene=1
                self.background=arcade.load_texture("../Data/commande.png")
        if self.scene==1:
            if 425<x<470 and 420<y<480:
                self.scene=0
                self.background = arcade.load_texture("../Data/menu.png")





if __name__ == "__main__":
    main()

