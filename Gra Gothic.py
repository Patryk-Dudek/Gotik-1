import pygame
from random import randint

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1024, 768))

print(pygame.font.get_fonts())

exchange_square_coordinates = [520, 40]

class Player:
    def __init__(self):
        self.x_cord = exchange_square_coordinates[0] #pierwotne położenie
        self.y_cord = exchange_square_coordinates[1]
        self.image = pygame.image.load("gracz.png") #wczytuje grafikę
        self.width = self.image.get_width() #rozmiary
        self.height = self.image.get_height()
        self.speed = 7 #premtkość
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, keys): #ruch, raz na powtórzenie pętli
        if keys[pygame.K_w]:
            self.y_cord -= self.speed
        if keys[pygame.K_a]:
            self.x_cord -= self.speed
        if keys[pygame.K_s]:
            self.y_cord += self.speed
        if keys[pygame.K_d]:
            self.x_cord += self.speed
        
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Cash:
    def __init__(self):
       self.x_cord = randint(0, 800)
       self.y_cord = randint(0, 500)
       self.image = pygame.image.load("chrzaszcz3.png")
       self.width = self.image.get_width() #rozmiary
       self.height = self.image.get_height()
       self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

def main():
    run = True
    player = Player()
    clock = 0
    banknotes = []
    score = 0
    background = pygame.image.load("tło.jpg")
    
    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        print(clock) #stoper

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #zamykanie okna
                run = False

        if clock >= 1: #wyświetlania banknotów
            clock = 0
            Cash()
            banknotes.append(Cash())
        
        for banknote in banknotes:
            banknote.tick()
        
        for banknote in banknotes: #zbieranie banknotów
            if player.hitbox.colliderect(banknote.hitbox):
                banknotes.remove(banknote)
                score += 10

        score_image = pygame.font.Font.render(pygame.font.SysFont("gothictiteloffiziellnormalny", 70), f"Doswiadczenie: {score} xp", True, (0, 0, 0)) #definicja tekstu

        keys = pygame.key.get_pressed() #kierowanie postacią
        player.tick(keys)

        #window.fill((15, 78, 171)) #rysowanie tła
        window.blit(background, (0, 0)) #rysowanie tła z pliku
        window.blit(score_image, (25, 15)) # rysowanie tekstu
        player.draw() #rysowanie gracza
        for banknote in banknotes: #rysowanie banknotów
            banknote.draw()
        pygame.display.update() #odświeżanie ekranu

        keys = pygame.key.get_pressed()

    level = 0 #obliczenie posiomu doswiadczenia
    if score >= 500:
        level += 1
        if score >= 1500:
            level += 1
            if score >= 3000:
                level += 1
                if score >= 5000:
                    level += 1
    print(f"\nZdobyłeś {score} punktów doświadczenia i osiągnąłeś {level} poziom.")

if __name__ == "__main__":
    main()