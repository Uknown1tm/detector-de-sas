input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(humesas)
})
let humesas = 0
basic.showString("humedad")
basic.forever(function on_forever() {
    
    humesas = pins.analogReadPin(AnalogReadWritePin.P1)
    if (humesas <= 1016) {
        //  el 1016 es un valor que tenemos que
        //  dar con los datos nuestros que obtuvimos
        basic.showIcon(IconNames.No)
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    } else {
        basic.showIcon(IconNames.Yes)
    }
    
})
