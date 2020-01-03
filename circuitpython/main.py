# Imports
#
# circuit python 4.1.2
# install lib/neopixel.mpy to /lib/ on the filesystem
#
import time      # what time is it?
import board     # for board
import busio     # for i2c
import neopixel  # for led ring
import digitalio # for spi

try: 
  # i2c for the RFID-RC522
  i2c = busio.I2C(board.SCL, board.SDA)
  # Lock the I2C device before we try to scan
  while not i2c.try_lock():
      pass
  # Print the addresses found once
  print("I2C addresses found:", [hex(device_address)
                               for device_address in i2c.scan()])
 
  # Unlock I2C now that we're done scanning.
  i2c.unlock()
except:
  # 
  print("i2c seems to not be wired up right, check that a 10k pull up is on both SDA and SCL")
#
pixpin = board.D2  # what pin the LEDs are on
sensepin = digitalio.DigitalInOut(board.D12) # What pin the sense is on
numpix = 60  # number of LEDs in ring!
BPP = 3

ring = neopixel.NeoPixel(pixpin, numpix, bpp=BPP, brightness=0.1, auto_write=False)

half = int(numpix / 2)
quarter = int(numpix / 4)
mode = 1
sense_count = 0
while True:
    # Two lines for troubleshooting to see analog value in REPL
    ring.show()
    # slow spinning white ring
    if mode == 1:
        sense_count = 0
        print("Mode 1")
        for x in range(half-1, 0-1, -1):
#          print(x,x+half)
          ring[x] = (64,64,64)
          ring[x+half] = (64,64,64)
          ring.show()
          time.sleep(0.05)
          ring[x] = (0,0,0)
          ring[x+half] = (0,0,0)
          check_value = sensepin.value
          if check_value:
            lastpin = check_value
            mode = 2
            break

    # fast white spinning ring
    if mode == 2:
          print("Mode 2")
          print("D12 = ", sensepin.value)

          speed_range = int(numpix/3)
          for speed in range(quarter, 0, -1):
            for x in range(half-1, 0-1, -2):
              check_value = sensepin.value
              if check_value != lastpin:
                  sense_count = sense_count + 1
                  lastpin = check_value
#              print (speed, x, speed_range-speed+2, x-speed)
              ring[x] = (255,255,255)
              ring[x+half] = (255,255,255)
#              for y in range(x-speed_range-speed+2, x):
#                ring[y] = (255,255,255)
              if sense_count > 2:
                  break
              ring.show()
#              time.sleep(speed*.005)
              if (speed > 0):
                ring[x] = (0,0,0)
                ring[x+half] = (0,0,0)
#                for y in range(x-speed_range-speed+2, x):
#                  ring[y] = (0,0,0)
          mode = 3


    # green ring
    if mode == 3:
        print("Mode 3")
        print("D12 = ", sensepin.value)
        print("sense_count =", sense_count)
        if sense_count < 2:
            ring.fill((0,255, 0))
            ring.show()
            time.sleep(3)
        else:
            for z in range (0, 3):
                # blue dimming
                for y in range (255, 0, -32):
#                    print("y = ", y)
                    ring.fill((0, 0, y))
                    ring.show()
                # blue brightening 
                for y in range (0, 255, 32):
#                    print("y = ", y)
                    ring.fill((0, 0, y))
                    ring.show()

        mode = 1
        ring.fill((0,0,0))
        ring.show()


    if mode == 4:
        print("Tiki")

        ## tiki mode
        for x in range (0, 24):
          for y in range (0, 5): 
#            print("y = ", y)
            ring[0+y*12] = ( 255, 0, 0)
            ring[1+y*12] = ( 192, 64, 0)
            ring[2+y*12] = ( 128, 128, 0)
            ring[3+y*12] = ( 128, 128, 0)
            ring[4+y*12] = ( 64, 192, 0)
            ring[5+y*12] = ( 32, 255, 0)
            ring[6+y*12] = ( 0, 255, 0)
            ring[7+y*12] = ( 0, 192, 64)
            ring[8+y*12] = ( 0, 128, 128)
            ring[9+y*12] = ( 0, 64, 128)
            ring[10+y*12] = ( 0, 64, 192)
            ring[11+y*12] = ( 0,0,255)

          ring.show()
          ring.fill((0,0,0))
          ring.show()
        mode = 1


