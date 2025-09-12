######################################################
### Main-Program                                   ###
### Projekt: Eurex_RP2040                          ###
### Version: 1.00                                  ###
### Datum  : 05.09.2025                            ###
######################################################
from machine import Timer                              # type: ignore
from random import randint # type: ignore
from libs.module_init import Global_Module as MyModule
import time                                                 # type: ignore

pixel_color = (250,230,10)
time_pause = 0.1
rand_min = 0
rand_max = 170
time_next_uboot = 8000
x = 0

def timer_1_CallBack(t):
    #print("Timer 1 Int.")
    update_leds()

def led_all_off():
    MyGPIO.i2c_write(0, True)
    MyGPIO.i2c_write(1, True)
    MyGPIO.i2c_write(2, True)
    MyGPIO.i2c_write(3, True)

def update_leds():
    global x
    #print(x)
    if x == 0:
        led_all_off()
    if x == 1:
        MyGPIO.i2c_write(0, False)
        MyGPIO.i2c_write(1, True)
        MyGPIO.i2c_write(2, True)
        MyGPIO.i2c_write(3, True)
    if x == 2:
        led_all_off()
    if x == 3:
        MyGPIO.i2c_write(0, True)
        MyGPIO.i2c_write(1, False)
        MyGPIO.i2c_write(2, True)
        MyGPIO.i2c_write(3, True)
    if x == 4:
        led_all_off()
    if x == 5:
        MyGPIO.i2c_write(0, True)
        MyGPIO.i2c_write(1, True)
        MyGPIO.i2c_write(2, False)
        MyGPIO.i2c_write(3, True)
    if x == 6:
        led_all_off()
    if x == 7:
        MyGPIO.i2c_write(0, True)
        MyGPIO.i2c_write(1, True)
        MyGPIO.i2c_write(2, True)
        MyGPIO.i2c_write(3, False)
    if x > 7:
        led_all_off()
    if x < 7:
        x = x + 1
    else:
        x = 0

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------

def main():

    print("=== Start Main ===")
    # periodic with 100ms period
    
    timer = Timer(period=time_next_uboot, mode=Timer.PERIODIC, callback=timer_1_CallBack)
    
    #MyWS2812.setup_ws2812()
    #MyGPIO.i2c_setup()
    MyGPIO.i2c_write(0, True)
    MyGPIO.i2c_write(1, True)
    MyGPIO.i2c_write(2, True)
    MyGPIO.i2c_write(3, True)

    MyWS2812.set_pixel_obj(0,0,(120,120,120),10)
    MyWS2812.set_pixel_obj(1,0,(120,120,120),10)
    MyWS2812.set_pixel_obj(2,0,(120,120,120),10)
    MyWS2812.do_refresh()

    try:
        print("Start Main Loop")
 
        while (True):
            MyWS2812.set_pixel_obj(0, 0, pixel_color, randint(rand_min, rand_max))
            MyWS2812.set_pixel_obj(1, 0, pixel_color, randint(rand_min, rand_max))
            MyWS2812.set_pixel_obj(2, 0, pixel_color, randint(rand_min, rand_max))
            MyWS2812.rotate_obj(0)
            MyWS2812.rotate_obj(1)
            MyWS2812.rotate_obj(2)
            MyWS2812.do_refresh()
            time.sleep(time_pause)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        print("Exiting the program")   

    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":

    if MyModule.inc_i2c:
        print("I2C_MCP23017 -> Load-Module")
        import libs.module_i2c as MyGPIO
        #print("I2C -> Setup")
        MyGPIO.i2c_setup()
        ### Test ###
        print("I2C -> SelfTest")
        for i in range(0,8):
            MyGPIO.i2c_write(i, True)
            time.sleep(0.3)
        for i in range(0,8):
            MyGPIO.i2c_write(i, False)
            time.sleep(0.3)
    else:
        print("I2C_MCP23017 -> nicht vorhanden")

    if MyModule.inc_ws2812:
        print("WS2812 -> Load-Module")
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        print("WS2812 -> Run self test")
        MyWS2812.self_test()
        print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()
    else:
        print("WS2812 -> nicht vorhanden")

    if MyModule.inc_random:
        print("Random -> Load-Module")
        import libs.module_random as MyRandom
        #print(MyRandom.random_int())
    else:
        print("Random -> nicht vorhanden")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___")
print("§§§> !!! STOP !!! <§§§")

# ##############################################################################
