def on_received_number(receivedNumber):
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(10)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    music.play(music.string_playable("- - - - - - - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("Bonjour")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.send_number(1)
radio.set_transmit_power(5)