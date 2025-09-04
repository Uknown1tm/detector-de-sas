def on_button_pressed_a():
    basic.show_number(humesas)
input.on_button_pressed(Button.A, on_button_pressed_a)

humesas = 0
basic.show_string("humedad")

def on_forever():
    global humesas
    humesas = pins.analog_read_pin(AnalogReadWritePin.P1)
    if humesas <= 1016:
        # el 1016 es un valor que tenemos que
        # dar con los datos nuestros que obtuvimos
        basic.show_icon(IconNames.NO)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)
