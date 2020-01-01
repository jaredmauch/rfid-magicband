# rfid-magicband

This repo includes the PCB layout for a ItsyBitsy M4 to Raspberry Pi Zero setup to adapt with a MFRC522 board and NeoPixel ring and Adafruit LiIon/LiPoly Backpack to provide for mobile reading of RFID devices, including things like the Magic Bands and park tickets.

You can configure on the Raspberry Pi a whitelist of the cards that are permissible to make the ring go green.

This is mostly an example and reference for others and I may update it as I refine the hardware and software over time.

Requirements:
Neopixel Ring
MFRC522
Raspberry Pi (zero - but pin compatible with any 40 pin Pi2-4)
ItsyBitsy M4 (M0 will also work)
PCB Adapter (from hardware directory, or breadboard it yourself)

Optional:
LiIon Battery/Backpack

It's recommended if you're in a theme park to turn off bluetooth, wifi, hdmi and anything else on the device that may cause power draw.  I may script something later that does this and makes installation easier.

I coded it in python3 and circuitpython because I'm not a heathen.
