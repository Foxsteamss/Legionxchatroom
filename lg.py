import socket
import threading
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()

notification_sound = pygame.mixer.Sound('Notif.mp3')

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.YELLOW +"       ███████████████████████████████████████████████████████████████████████████████████████████████")
print(style.YELLOW +"       █░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█")	
print(style.YELLOW +"       █░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█")
print(style.YELLOW +"       █░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█") 
print(style.YELLOW +"       █░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█") 
print(style.YELLOW +"       █░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█")
print(style.YELLOW +"       █░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█")  
print(style.YELLOW +"       █░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█")  
print(style.YELLOW +"       █░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█")  
print(style.YELLOW +"       █░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█")  
print(style.YELLOW +"       █░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█")	
print(style.YELLOW +"       █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█")  
print(style.YELLOW +"       █░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█")  
print(style.YELLOW +"       ███████████████████████████████████████████████████████████████████████████████████████████████")  

print(style.GREEN +"       -----------------------------------------------------------------------------------------------")
print(style.GREEN +"                         Legion X Society v2.3 Created With ❤ By Legion Tech ©2023") 
print(style.GREEN +"       -----------------------------------------------------------------------------------------------")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('51.79.161.21', 4200))
print(style.BLUE + "       ----------------------------------------------------------------------------------------------")
print(style.GREEN +"                         WELCOME TO LEGION X SOCIETY, STAY SAFE AND KEEP ANONYMOUS")
print(style.BLUE + "       ----------------------------------------------------------------------------------------------")
print(style.BLUE + "       ----------------------------------------------------------------------------------------------")

(style.RESET)

notification_sound.play()



def clear_screen():

    if os.name == 'posix':  # LINUX OS
        os.system('clear')
    elif os.name == 'nt':   # WINDOWS OS
        os.system('cls')

def send_message():
    while True:
        message = input(style.BLACK)
        client.send(message.encode('utf-8'))


def send_message():
    while True:
        message = input(style.GREEN)
        if message == "/clear":
            clear_screen()
        elif message == "/onusers":
            client.send("/onusers".encode('utf-8'))
        elif message == "/exit":
            client.send("/exit".encode('utf-8'))
            break
        else:
            client.send(message.encode('utf-8'))

def receive_message():
    while True:
        message = client.recv(1024).decode('utf-8')
        print(style.MAGENTA + message)
        notification_sound.play()



send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()
