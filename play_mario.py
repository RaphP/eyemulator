import subprocess
import pyautogui

def get_face_intensity(pipe):
    pipe.stdout.flush()
    line = pipe.stdout.readline().decode()
    while line[:4] != 'AU02': #Wait for the start of a sequence
        line = pipe.stdout.readline().rstrip().decode()

    lever = float(line.split(' ')[1]) #lever sourcil
    line = pipe.stdout.readline().rstrip().decode()
    froncer = float(line.split(' ')[1]) #froncer
    line = pipe.stdout.readline().rstrip().decode()
    sourire = float(line.split(' ')[1]) #sourire
    line = pipe.stdout.readline().rstrip().decode()
    fps = float(line) #fps

    return [lever, froncer, sourire, fps]


command = ['/Users/yvon/Desktop/OpenFace-dev/bin/FeatureExtraction', '-device', '0']
pipe = subprocess.Popen(command, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.PIPE)

#Wait for 'Starting tracking'
print('starting tracking program')
line = b''
while line != b'Starting tracking':
    line = pipe.stdout.readline().rstrip()
print('tracking started')
#

seuils = [2, 1.2, 0.6]
is_pressed = [False, False, False]
while 1:
    intensisty = get_face_intensity(pipe)
    print( [intensisty[i] > seuils[i] for i in range(3)] + [intensisty[3]])
    #print(intensisty)

    if intensisty[0] > seuils[0] and is_pressed[0] == False:
        is_pressed[0] = True
        pyautogui.keyDown('left')
    elif intensisty[0] < seuils[0] and is_pressed[0] == True:
        is_pressed[0] = False
        pyautogui.keyUp('left')

    if intensisty[1] > seuils[1] and is_pressed[1] == False:
        is_pressed[1] = True
        pyautogui.keyDown('right')
    elif intensisty[1] < seuils[1] and is_pressed[1] == True:
        is_pressed[1] = False
        pyautogui.keyUp('right')

    if intensisty[2] > seuils[2] and is_pressed[2] == False:
        is_pressed[2] = True
        pyautogui.keyDown('x')
    elif intensisty[2] < seuils[2] and is_pressed[2] == True:
        is_pressed[2] = False
        pyautogui.keyUp('x')


pipe.kill()
