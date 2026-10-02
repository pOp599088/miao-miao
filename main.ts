function on_button_pressed_a() {
    
    numero = numero - 1
    basic.showNumber(numero)
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    numero = numero - 1
    basic.showNumber(numero)
    input.onButtonPressed(Button.A, on_button_pressed_a)
})
let numero = 0
let segreto = randint(1, 100)
input.onButtonPressed(Button.A, on_button_pressed_a)
