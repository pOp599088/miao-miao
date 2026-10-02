def on_button_pressed_a():
    global numero
    numero = numero - 1
    basic.show_number(numero)

def on_button_pressed_b():
    global numero
    numero = numero - 1
    basic.show_number(numero)
    input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

numero = 0
segreto = randint(1, 100)
input.on_button_pressed(Button.A, on_button_pressed_a)