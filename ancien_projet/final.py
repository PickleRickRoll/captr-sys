# Enregistrement de vidéo avec boutons start/stop et molette pour changer le frame rate                                                                                                                                                                                                                                                                                                                                
import cv2
from gpiozero import Button, LED
from datetime import datetime
from time import sleep
import lgpio

# Pins de la molette
GPIO = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(GPIO, 17) # LED de démarrage
lgpio.gpio_claim_output(GPIO, 21) # LED d'enregistrement

# Boutons
button_on = Button(3)
button_off = Button(2,bounce_time=0.2)

# Pour sortir de la boucle d'enregistrement
stop_enrg = True

# Interruption pour le bouton stop
def init():
    button_off.when_pressed = OFF

# Fonction appelée par l'interruption, met la variable stop_enrg à false pour sortir de la boucle d'enregistrement
def OFF():
    global stop_enrg
    stop_enrg = False
    for _ in range(3):
        lgpio.gpio_write(GPIO, 17, 1)
        sleep(0.2)
        lgpio.gpio_write(GPIO, 17, 0)
        sleep(0.2)
    lgpio.gpio_write(GPIO, 21, 0)

# Retourne la valeur choisie par la molette + 1
def molette():
    valeur_inv = [lgpio.gpio_read(GPIO, pin) for pin in [14, 15, 23, 24, 25]]
    valeur = [0 if inv else 1 for inv in valeur_inv]
    valeur_ = valeur[0] * 1 + valeur[1] * 2 + valeur[2] * 4 + valeur[3] * 8 + valeur[4] * 8 + 1
    return valeur_

def main():
    global stop_enrg
    while True:
        if button_on.is_pressed:
            stop_enrg = True
            # Lancement de l'enregistrement après 3 clignotements
            for _ in range(3):
                lgpio.gpio_write(GPIO, 17, 1)
                sleep(0.2)
                lgpio.gpio_write(GPIO, 17, 0)
                sleep(0.2)
            lgpio.gpio_write(GPIO, 21, 1)
            nom_fichier = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            video = cv2.VideoCapture(0)
            if not video.isOpened():
                print("Erreur de lecture du fichier")
                return
            frame_width = int(video.get(3))
            frame_height = int(video.get(4))
            size = (frame_width, frame_height)
            fps = molette()
            print("______________________frame", fps)
            # Modifier le chemin d'enregistrement des vidéos si necessaire
            result = cv2.VideoWriter('/home/abc/Projet/Videos/' + nom_fichier + '.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, size)
            while stop_enrg:
                print("enrg")
                ret, frame = video.read()
                if ret:
                    result.write(frame)
                else:
                    break
            # Relâcher tout à la fin
            video.release()
            result.release()
            print("Vidéo enregistrée\n")

if __name__ == "__main__":
    # Clignote 2 fois pour indiquer que le programme est lancé
    for _ in range(2):
        lgpio.gpio_write(GPIO, 17, 1)
        sleep(0.1)
        lgpio.gpio_write(GPIO, 17, 0)
        sleep(0.1)
    init()
    main()
