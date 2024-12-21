import pygame
import pygame
import requests
from io import BytesIO
from PIL import Image as PILImage
import os
import requests
from urllib.parse import urlparse

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.basename(urlparse(url).path) or 'image.png'
        os.makedirs('./static', exist_ok=True)
        with open(f'./static/{file_name}', 'wb') as file:
            file.write(response.content)
        print(f"Image saved as ./static/{file_name}")
pygame.init()

color = (255,255,255)
position = (0,0)

# CREATING CANVAS

# TITLE OF CANVAS
pygame.display.set_caption("Show Image")

image = pygame.image.load(f"./static/pkmn_back.png")
canvas = pygame.display.set_mode((image.get_width(),image.get_height()))

exit = False
url = "https://pokeapi.co/api/v2/pokemon/mew"




def main():
	# Initialize Pygame
	pygame.init()

	# URL of the PNG image
	url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/151.png"
	download_image(url)
	# Download and load the image

	if image is None:
		pygame.quit()
		return  # Exit if the image wasn't successfully loaded

	# Create a Pygame window to display the image
	screen = pygame.display.set_mode((image.get_width(), image.get_height()))
	pygame.display.set_caption("Loaded Image")

	# Main game loop
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			value = pygame.sprite.Sprite()

		# Display the image on the screen
		screen.blit(image, (0, 0))
		pygame.display.flip()

	# Quit Pygame
	pygame.quit()



if __name__ == "__main__":
	main()