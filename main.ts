radio.onReceivedNumber(function (receivedNumber) {
    music.play(music.tonePlayable(165, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.showNumber(0)
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(0)
})
radio.onReceivedString(function (receivedString) {
    music.play(music.stringPlayable("- - - - - - - - ", 120), music.PlaybackMode.InBackground)
    basic.showString("")
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("")
})
radio.sendNumber(0)
radio.setTransmitPower(7)
