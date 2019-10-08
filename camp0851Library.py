from gfxhat import lcd;
from gfxhat import backlight;
from time import sleep;
import random;

#CREATE A VERTICAL LINE
def createVerticalLine():
    lcd.clear();
    lcd.show();
    y = 0;
    x = int(input('Set the x cordinate for the vertical line: '));

    while (y <= 63):
        lcd.set_pixel(x,y,1);
        y = y + 1;

    lcd.show();

#CREATE A HORIZONTAL LINE
def createHorizontalLine():
    lcd.clear();
    lcd.show();
    x = 0;
    y = int(input('Set the y cordinate for the horizontal line: '));

    while (x <= 127):
        lcd.set_pixel(x,y,1);
        x = x + 1;
    
    lcd.show();

#CREATE STAIRCASE (BROKEN)
def createStaircase():
    lcd.clear();
    lcd.show();
    x = 0;
    y = 0;
    w = 23 #int(input('Enter the stair width: '));
    h = 23 #int(input('Enter the height width: '));
    while(x <= 127 or y <= 63):
        while(x <= (x + w)):
            lcd.set_pixel(x,y,1);
            x = x + 1;
        
        while(y <= (y + h)):
            lcd.set_pixel(x,y,1);
            y = y + 1;
        x = x + 1;
        y = y + 1;

    lcd.show();

#DISPLAY A RANDOM PIXEL FOR A TIME
def randonPixel():
    lcd.clear();
    lcd.show();
    x = random.randint(0,127);
    y = random.randint(0,63);
    timer = int(input('Enter an amount of seconds for the pixel to appear on the screen: '));

    lcd.set_pixel(x,y,1);
    lcd.show();

    sleep(5);
    lcd.clear();
    lcd.show();

#CLEAR BACKLIGHT
def clearBacklight():
    lcd.clear();
    lcd.show();

    backlight.set_all(0,0,0);
    backlight.show();