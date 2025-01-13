
#Import Pygame and Constants.py and Player.py
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
#Begin Game

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
    #field = AsteroidField()
    print("Asteroids spawning!")
    Asteroid.containers = (asteroids, updatable, drawable) 
    Player.containers = (updatable, drawable)
    player  = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for updatables in updatable:
             updatables.update(dt)
        for asteroid in asteroids:
             if player.collision(asteroid):
                print ("GAME OVER MAN!")
                exit()
        for shot in shots:
             shot.update(dt)
             shot.draw(screen)
             
        for drawables in drawable:
             drawables.draw(screen)
        
        
        pygame.display.flip()
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
	main()

