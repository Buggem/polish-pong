#### !!!! BLOCKLY EXPORT !!!! ####
import thumbyButton as buttons
Number = int
import time
import math
from thumbySprite import Sprite
import random
from thumbyGraphics import display
import gc
from thumbySaves import saveData

option = None
jsskjddjfkjfdksj = None
brightness = None
rsg_millis__ready_set_go_ = None
a_button = None
logo = None
rsgtime = None
speed = None
arrow = None
ready_set_go = None
game = None
game_text = None
xpos = None
ypos = None
rsgy = None
yplay = None
xspeed = None
yspeed = None

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

arrow = Sprite(1,1,bytearray([1]))

logo = Sprite(1,1,bytearray([1]))

game_text = Sprite(1,1,bytearray([1]))

# Describe this function...
def select():
  global option, jsskjddjfkjfdksj, brightness, rsg_millis__ready_set_go_, a_button, logo, rsgtime, speed, arrow, ready_set_go, game, game_text, xpos, ypos, rsgy, yplay, xspeed, yspeed
  if buttons.buttonU.justPressed() or buttons.buttonD.justPressed():
    option = (option if isinstance(option, Number) else 0) + 1
    option = option % 2
  if 750 < time.ticks_ms() % 1000:
    arrow.setFrame(1)
  elif 500 < time.ticks_ms() % 1000:
    arrow.setFrame(2)
    logo.setFrame(2)
  elif 250 < time.ticks_ms() % 1000:
    arrow.setFrame(3)
  else:
    arrow.setFrame(4)
    logo.setFrame(1)
  arrow.x = 2 + random.randint(-300, 300) / 100
  arrow.y = (2 + random.randint(-300, 300) / 100) + 20 * option
  display.drawSprite(arrow)
  game_text.x = 30 + random.randint(-50, 50) / 100
  game_text.y = 4 + random.randint(-50, 50) / 100
  display.drawSprite(game_text)
  display.update()
  display.fill(1)

ready_set_go = Sprite(1,1,bytearray([1]))

a_button = Sprite(1,1,bytearray([1]))

# Describe this function...
def ready_set_go2():
  global option, jsskjddjfkjfdksj, brightness, rsg_millis__ready_set_go_, a_button, logo, rsgtime, speed, arrow, ready_set_go, game, game_text, xpos, ypos, rsgy, yplay, xspeed, yspeed
  rsg_millis__ready_set_go_ = time.ticks_ms()
  rsgtime = time.ticks_ms() - rsg_millis__ready_set_go_
  while rsgtime < 2500:
    rsgtime = time.ticks_ms() - rsg_millis__ready_set_go_
    if rsgtime < 1000:
      ready_set_go.y = 20
    elif rsgtime < 2000:
      ready_set_go.y = 12
    else:
      ready_set_go.y = 4
      ready_set_go.x = -4
    display.drawSprite(ready_set_go)
    rsgy = 0
    for count5 in range(20):
      display.drawLine(0, rsgy, 72, rsgy, 0)
      rsgy = (rsgy if isinstance(rsgy, Number) else 0) + 1
    rsgy = 28
    for count6 in range(12):
      display.drawLine(0, rsgy, 72, rsgy, 0)
      rsgy = (rsgy if isinstance(rsgy, Number) else 0) + 1
    display.update()
    display.fill(0)
  display.update()
  display.fill(0)
  gc.collect()

# Describe this function...
def title_screen():
  global option, jsskjddjfkjfdksj, brightness, rsg_millis__ready_set_go_, a_button, logo, rsgtime, speed, arrow, ready_set_go, game, game_text, xpos, ypos, rsgy, yplay, xspeed, yspeed
  if 1700 < time.ticks_ms() % 2000:
    a_button.setFrame(1)
  else:
    a_button.setFrame(2)
  logo.x = 15 + random.randint(-100, 100) / 100
  display.drawSprite(logo)
  display.drawSprite(a_button)
  display.update()
  display.fill(1)
  logo.y += -0.2
  if logo.y < -100:
    logo.y = 100

saveData.setName(globals().get('__file__', 'FAST_EXECUTE').replace('/Games/','').strip('/').split('/')[0].split('.')[0])

# ping pong peng ping
def pong_main_subroutine():
  global option, jsskjddjfkjfdksj, brightness, rsg_millis__ready_set_go_, a_button, logo, rsgtime, speed, arrow, ready_set_go, game, game_text, xpos, ypos, rsgy, yplay, xspeed, yspeed
  if not saveData.hasItem('high score'):
    saveData.setItem('high score', 0)
    saveData.save()
  speed = 100
  game = True
  saveData.setItem('score', 0)
  saveData.save()
  xpos = 36
  ypos = 20
  yplay = 10
  playh = 10
  playspeed = 2
  xspeed = (random.randint(4, 7) * -1) / speed
  yspeed = random.randint(-5, 5) / speed
  display.setFont("/lib/font3x5.bin", 3, 5, display.textSpaceWidth)
  while game:
    yplay += (buttons.buttonD.pressed()-buttons.buttonU.pressed())/playspeed;
    yplay = clamp(yplay, 0, 40-playh)
    display.drawRectangle(65, math.floor(yplay), 2, playh, 1)
    display.setPixel(math.floor(xpos), math.floor(ypos), 1)
    xpos = (xpos) + xspeed
    ypos = (ypos) + yspeed
    if xpos <= 0:
      xspeed = xspeed * -1
    if ypos <= 0 or ypos >= 40:
      yspeed = yspeed * -1
    if xpos >= 72:
      game = False
    if xpos >= 64 and xpos <= 66 and ypos >= yplay and ypos <= yplay + playh and xspeed >= 0:
      saveData.setItem('score', int(saveData.getItem('score')) + 25)
      saveData.save()
      xspeed = xspeed * -1.1
      yspeed = random.randint(-5, 5) / speed
    display.update()
    display.fill(0)
    display.drawText(str('o:' + str(saveData.getItem('score'))), 0, 0, 1)
  display.setFont("/lib/font5x7.bin", 5, 7, display.textSpaceWidth)


option = 0
brightness = 127
display.brightness(brightness)
ready_set_go = Sprite(72,24,bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,243,115,243,255,239,0,255,255,255,219,219,219,219,90,0,254,255,255,119,255,255,254,0,255,255,255,247,255,255,62,0,7,15,255,252,255,15,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,223,223,223,255,247,247,230,0,255,255,255,219,219,219,219,219,219,90,0,7,7,255,255,255,255,7,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,28,62,34,34,99,99,99,99,99,99,115,115,114,0,28,62,99,99,99,99,99,99,99,99,99,62,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),ready_set_go.x,ready_set_go.y,ready_set_go.key,ready_set_go.mirrorX,ready_set_go.mirrorY)
game_text = Sprite(50,25,bytearray([255,255,255,255,255,255,159,143,175,143,159,31,255,255,255,159,159,143,143,31,255,255,255,63,191,63,191,191,191,63,255,255,255,63,191,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,223,31,255,255,0,132,241,255,255,255,127,127,191,159,88,19,81,76,15,15,15,143,143,142,174,193,195,196,192,203,79,79,95,79,95,95,31,255,255,255,255,255,255,255,255,255,255,255,255,255,247,234,242,242,216,225,244,148,226,224,240,248,248,252,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,255,255,255,255,255,255,255,255,255,255,255,255,255,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,255,255,255,255,127,127,127,127,127,127,255,255,255,63,63,127,255,255,255,255,127,127,127,127,255,127,127,127,255,255,255,63,191,159,63,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,252,248,250,250,248,0,63,255,252,121,186,24,80,39,111,80,79,79,108,14,79,199,144,191,255,255,252,120,123,112,102,47,31,159,95,223,223,207,207,239,255,255,255,255,255,255,255,255,252,222,206,238,166,150,166,199,243,241,213,212,198,195,227,233,249,244,228,240,248,232,252,236,238,236,238,236,226,250,252,254,252,254,248,248,253,252,253,255,255,255,255,255,255,255,255,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),game_text.x,game_text.y,game_text.key,game_text.mirrorX,game_text.mirrorY)
arrow = Sprite(25,20,bytearray([31,223,223,223,223,223,223,223,223,239,239,239,239,239,225,253,243,239,31,255,255,255,255,255,255,255,252,251,253,253,253,253,251,251,251,253,253,253,243,143,191,223,239,243,252,255,255,255,255,255,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,255,207,51,251,247,247,231,239,239,239,239,223,223,191,191,159,199,247,239,239,223,191,127,255,255,15,119,120,127,127,63,191,191,191,159,223,223,223,239,239,15,255,255,255,255,31,239,243,252,255,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,12,13,13,13,14,15,15,15,15,15,15,239,223,191,191,191,127,255,255,255,255,3,251,247,247,239,239,223,191,63,255,255,255,255,255,0,255,255,127,191,223,223,238,238,238,238,14,255,255,255,255,127,63,143,224,255,255,255,255,255,8,13,14,15,15,15,15,15,15,15,15,12,13,12,14,14,14,15,15,15,15,15,15,15,15,3,251,247,247,239,239,223,223,223,223,223,191,191,191,191,191,191,131,253,251,247,239,223,63,255,0,255,255,255,255,127,127,191,191,191,191,191,191,191,191,191,191,63,255,255,255,255,127,159,224,8,11,13,14,14,15,15,15,15,15,15,15,15,15,15,15,15,8,7,11,13,14,15,15,15]),arrow.x,arrow.y,arrow.key,arrow.mirrorX,arrow.mirrorY)
a_button = Sprite(8,8,bytearray([131,29,34,52,52,34,29,131,199,187,69,105,105,69,187,199]),a_button.x,a_button.y,a_button.key,a_button.mirrorX,a_button.mirrorY)
logo = Sprite(40,80,bytearray([255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,127,129,237,253,253,105,125,125,61,53,53,61,61,29,29,29,29,61,1,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,63,195,240,244,242,240,244,241,248,251,248,242,241,236,192,192,196,196,192,192,198,241,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,248,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,3,251,243,15,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,
           255,255,255,255,255,255,255,15,224,253,254,255,255,255,127,31,239,7,255,0,255,255,251,203,159,127,255,255,255,231,215,183,63,248,7,127,159,191,127,255,
           255,255,255,255,255,63,192,255,255,255,255,255,255,255,255,248,251,188,159,207,240,255,255,255,255,255,254,241,255,255,249,252,254,255,252,248,255,255,254,252,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,192,250,248,255,192,222,222,222,192,255,192,254,254,253,253,251,251,247,247,239,239,223,192,255,224,238,238,206,255,255,255,255,255,
           255,227,251,247,251,227,255,227,243,227,255,235,247,235,255,255,227,243,243,255,227,243,227,255,227,243,243,239,255,227,243,243,239,255,243,231,243,255,235,255]), logo.x,logo.y,logo.key,logo.mirrorX,logo.mirrorY)
a_button.x = 5
a_button.y = 5
while not buttons.buttonA.pressed():
  title_screen()
for count in range(127):
  brightness = (brightness if isinstance(brightness, Number) else 0) + -1
  time.sleep_ms(10)
  display.brightness(brightness)
  title_screen()
gc.collect()
for count2 in range(127):
  brightness = (brightness if isinstance(brightness, Number) else 0) + 1
  time.sleep_ms(2)
  display.brightness(brightness)
  select()
while not buttons.buttonA.pressed():
  select()
for count3 in range(127):
  brightness = (brightness if isinstance(brightness, Number) else 0) + -1
  time.sleep_ms(5)
  display.brightness(brightness)
  select()
gc.collect()
for count4 in range(127):
  display.fill(0)
  brightness = (brightness if isinstance(brightness, Number) else 0) + 1
  time.sleep_ms(2)
  display.brightness(brightness)
  display.update()
time.sleep_ms(600)
ready_set_go2()
pong_main_subroutine()

#### !!!! BLOCKLY EXPORT !!!! ####
