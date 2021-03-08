import random
import math
import arcade

SCREEN_WIDTH = 1920                                                                                                         # Szerokosc
SCREEN_HEIGHT = 1080                                                                                                        # Wysokosc
SCREEN_TITLE = "Obrazek 2D - Grafika i komunikacja czlowiek - komputer (PROJEKT 1)"                                         # Tytul


class Star:                                                                                                                 # Klasa star, reprezentuje kazda gwiazde
    def __init__(self):                                                                                                     # Konsturktor klasy Star
        self.x = 0                                                                                                          # Obszar startowy gwiazdy (x)
        self.y = 0                                                                                                          # Obszar startowy gwiazdy (y)

    def resetPosition(self):                                                                                                # Resetowanie pozycji gwiazd
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)                                                       # Obszar od MAX gory do MAX gory + 100
        self.x = random.randrange(SCREEN_WIDTH)                                                                             # Obszar szerokosci


class Picture(arcade.Window):                                                                                               # Glowna klasa obrazka
    def __init__(self, width, height, title):                                                                               # Konstruktor klasy Picture
        super().__init__(width, height, title, resizable=True)                                                              # Wywolanie konstruktora z arcade.Window
        self.star_list = None                                                                                               # Lista gwiazd


    def startStarFall(self):                                                                                                # Poruszanie sie gwiazd
        self.star_list = []                                                                                                 # Stworzenie listy gwiazd, tablicy
        for i in range(400):                                                                                                # Petla od 0 do 50
            star = Star()                                                                                                   # Stworzenie obiektu klasy Star()

            star.x = random.randrange(SCREEN_WIDTH)                                                                         # Randomowa pozycja x star
            star.y = random.randrange(3)                                                                                    # Randomowa pozycja y star

            star.size = random.randrange(4)                                                                                 # Randomowa wielkosc gwiazdy do max 4
            star.speed = random.randrange(20, 60)                                                                           # Randomowa szybkosc gwiazdy od 20 do 40
            star.angle = random.uniform(math.pi, math.pi * 2)                                                               # Kat gwiazdy

            self.star_list.append(star)                                                                                    # Dodanie do listy okreslonej gwiazdy

        self.set_mouse_visible(True)                                                                                       # Widocznosc myszki false


    def on_draw(self):                                                                                                      # Funkcja do rysowania
        arcade.start_render()                                                                                               # Umozliwia rysowanie
        
        arcade.draw_lrtb_rectangle_filled (0, SCREEN_WIDTH, 1080, SCREEN_HEIGHT * (1 / 3), arcade.color.SKY_BLUE)           # Kolor tla
        arcade.draw_lrtb_rectangle_filled (0, SCREEN_WIDTH, SCREEN_HEIGHT * (1 / 3), 0, arcade.color.DARK_GREEN)            # Kolor tla

        arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 1
        arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)                                                 # Drzewo 1

        arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 2
        arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)                                            # Drzewo 2

        arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 3
        arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)                                       # Drzewo 3

        arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 4
        arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)                               # Drzewo 4

        arcade.draw_rectangle_filled(350, 200, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 5
        arcade.draw_circle_filled(350, 255, 30, arcade.csscolor.DARK_GREEN)                                                 # Drzewo 5

        arcade.draw_rectangle_filled(250, 100, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 7
        arcade.draw_circle_filled(250, 150, 30, arcade.csscolor.DARK_GREEN)                                                 # Drzewo 7

        arcade.draw_rectangle_filled(100, 100, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 8
        arcade.draw_circle_filled(100, 150, 30, arcade.csscolor.DARK_GREEN)                                                 # Drzewo 8

        arcade.draw_rectangle_filled(140, 200, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 9
        arcade.draw_circle_filled(140, 240, 30, arcade.csscolor.DARK_GREEN)                                                 # Drzewo 9

        arcade.draw_rectangle_filled(230, 220, 20, 60, arcade.csscolor.SIENNA)                                              # Drzewo 10
        arcade.draw_circle_filled(230, 240, 30, arcade.csscolor.DARK_GREEN)                                                 # Drzewo 10

        arcade.draw_rectangle_filled(SCREEN_WIDTH / 1.3, 400, 500, 400, arcade.csscolor.BROWN)                              # DOM
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 1.20, 400, 70, 80, arcade.csscolor.MEDIUM_BLUE)                         # DOM
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 1.40, 400, 70, 80, arcade.csscolor.MEDIUM_BLUE)                         # DOM

        arcade.draw_triangle_filled(1160, 550, 1500, 800, 1800, 550, arcade.csscolor.SANDY_BROWN)

        arcade.draw_rectangle_filled(1500, 250, 60, 100, arcade.csscolor.SADDLE_BROWN)                                      # DOM
        arcade.draw_circle_filled(1515, 250, 5, arcade.csscolor.BLACK)

                                                                                                                            # CHMURA
        arcade.draw_circle_filled(1100, 950, 80, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_circle_filled(1200, 950, 80, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_circle_filled(1100, 860, 80, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_circle_filled(1200, 850, 80, arcade.csscolor.WHITE_SMOKE)


        arcade.draw_circle_filled(500, 950, 80, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_circle_filled(600, 940, 80, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_circle_filled(500, 900, 80, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_circle_filled(600, 880, 80, arcade.csscolor.WHITE_SMOKE)

      #  arcade.draw_circle_filled(100, 1000, 200, arcade.color.YELLOW)                                                     # Slonce
            
        arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)                                                     
 
        arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3) 
        arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3) 
        arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3) 
        arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3) 

        arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3) 
        arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3) 
        arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3) 
        arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3) 
                                                                                                                            # Traktor
       
        arcade.draw_rectangle_filled(600, 180, 140, 70, arcade.color.GRAY)
        arcade.draw_rectangle_filled(590, 160, 90, 40, arcade.color.BLACK)

    
        arcade.draw_rectangle_filled(650, 230, 10, 40, arcade.color.BLACK)

        arcade.draw_circle_filled(510, 170, 50, arcade.color.BLACK)
        arcade.draw_circle_filled(510, 170, 45, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(510, 170, 35, arcade.color.OLD_LACE)
        arcade.draw_circle_filled(510, 170, 10, arcade.color.RED)

        arcade.draw_circle_filled(650, 150, 30, arcade.color.BLACK)
        arcade.draw_circle_filled(650, 150, 25, arcade.color.BLACK_OLIVE)
        arcade.draw_circle_filled(650, 150, 18, arcade.color.OLD_LACE)
        arcade.draw_circle_filled(650, 150, 5, arcade.color.RED)
                                                                                                                            # Balwan

        arcade.draw_circle_filled(900, 200, 60, arcade.color.WHITE)
        arcade.draw_circle_filled(900, 280, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(900, 340, 40, arcade.color.WHITE)

        arcade.draw_circle_filled(910, 350, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(890, 350, 5, arcade.color.BLACK)



        arcade.draw_rectangle_filled(1600, 700, 50, 100, arcade.color.DARK_SLATE_GRAY)

        for x in range(100):
            arcade.draw_circle_outline(1600 + x, 780 + x, 20, arcade.color.ASH_GREY)


        for star in self.star_list:                                                                                         # Petla po wszystkich obiektach w star_list
            arcade.draw_circle_filled(star.x, star.y, star.size, arcade.color.WHITE)                                        # Nadanie ksztaltu gwiezdzie i uzupelnienie bialym kolorem

        for x in range(1, 100, 12):
            arcade.draw_arc_outline(1000 + x, 600 - x, 20, 20, arcade.color.BLACK, 0, 90)
            arcade.draw_arc_outline(1020 + x, 600 - x, 20, 20, arcade.color.BLACK, 90, 180)
            x+=1

        for x in range(1, 100, 20):
            arcade.draw_arc_outline(980 - x, 590 - x, 20, 20, arcade.color.BLACK, 0, 90)
            arcade.draw_arc_outline(1000 - x, 590 - x, 20, 20, arcade.color.BLACK, 90, 180)
            x+=1

 
            




    def on_update(self, delta_time):                                                                                        # Funkcja update
        for star in self.star_list:                                                                                         # Update kazdego obiektu star
            star.y -= star.speed * delta_time                                                                               # Nadanie randomowej predkosci spadania
            if(star.y < 850):                                                                                               # Jesli wyjdzie poza ekran
                star.resetPosition()                                                                                        # Wywoluje funkcje resetujaca pozycje gwiazdy

            star.x += star.speed * math.cos(star.angle) * delta_time                                                        # poruszanie sie gwiazd
            star.angle += 1 * delta_time                                                                                    # kat gwiazd
                
    




def main():                                                                                                                  # Funkcja glowna ktora wywoluje na koncu
   window = Picture(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)                                                               # Stworzenie obiektu o nazwie window, przypisanie mu wielkosci okna
   window.startStarFall()
   arcade.run()                                                                                                              # Wyświetla wszystko

    
main()                                                                                                                       # Wywolanie funkcji main

