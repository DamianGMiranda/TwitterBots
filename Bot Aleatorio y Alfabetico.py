import tweepy
import os
import random
import time

consumer_key = 
consumer_secret = 
access_key = 
access_secret = 

# Tweepy para conectarte a la API de Twitter y autenticarte
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Obtener lista de todos los archivos de imagen en la carpeta "C:\Users\Damián\Desktop\Gatoz"
image_files = os.listdir("C:\\Users\\Damián\\Desktop\\Gatoz")

# Crea un archivo de texto para guardar un registro de las imágenes que se han publicado
with open("published_images.txt", "w") as f:
    f.write("")

while True:
    # Seleccionar una imagen de la lista de archivos de imagen
    image_file = image_files[0]
    image_files.pop(0)
    
    #image_file = random.choice(image_files)

    # Comprueba si la imagen ya se ha publicado anteriormente
    with open("published_images.txt", "r") as f:
        published_images = f.read().splitlines()

    if image_file not in published_images:
        # Publica la imagen en Twitter utilizando la API de Twitter
        api.update_status_with_media(filename=image_file, status="#Berserk")

        # Añade la imagen al registro de imágenes publicadas
        with open("published_images.txt", "a") as f:
            f.write(image_file + "\n")

    # Duerme durante 30 minutos antes de publicar la siguiente imagen
    time.sleep(1800)

