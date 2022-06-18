
# importamos el modulo
#la palabra as es un alias
import pywhatkit as kit
import pyautogui
import keyboard as k
import time
# utilizaremos controles de excepciones
while True:
    try: 
     
        # enviando mensaje al receptor
        # usando pywhatkit 
        # kit.sendwhatmsg("celular","Prueba de python,enviando mensaje",21, 56) 
        #kit.sendwhatmsg_instantly("celular","https://www.youtube.com/shorts/iX_1d0c2R-8")#enviar mensaje instantaneo
        kit.sendwhatmsg_instantly("celular","Pruebas de python, enviando mensaje") 
        pyautogui.click(550, 700)
        k.press_and_release('enter')
        time.sleep(2)
        print("Envio Exitoso!") 
        break
   
    except: 
     
     # manejo de excepcion
     # e impresion del error
     print("Ha ocurrido un error!")