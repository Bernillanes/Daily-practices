import keyboard
print("Presiona 'p' para salir...")

while True:
    if keyboard.is_pressed('p'):
        print("¡Detectado 'p'! Saliendo...")
        break
