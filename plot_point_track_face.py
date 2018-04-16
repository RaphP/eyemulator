import matplotlib.pyplot as plt
import subprocess

def get_array(pipe):
    char = pipe.stdout.read(1)
    while char != b'[': #Wait for the start of a sequence
        char = pipe.stdout.read(1)

    line = b''
    char = pipe.stdout.read(1)
    while char != b']':
        line += char
        char = pipe.stdout.read(1)

    array = [float(e) for e in line.decode().split(';\n')]
    return array


command = ['/Users/yvon/Downloads/OpenFace-master/bin/FaceLandmarkVid', '-device', '0']
pipe = subprocess.Popen(command, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.PIPE)


#Wait for 'Starting tracking'
print('starting tracking program')
line = b''
while line != b'Starting tracking':
    line = pipe.stdout.readline().rstrip()

print('tracking started')
#



#animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up formatting for the movie files
fig, ax = plt.subplots()
ax.axis([0,500,0,500])
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
#ax.axis(Xlim+Ylim)

pos = get_array(pipe)
partPlotx = pos[:68]
partPloty = pos[68:]

line = ax.plot(partPlotx, partPloty, ls="", marker="o")

def update(frame_number):
    pos = get_array(pipe)
    posX = pos[:68]
    posY = pos[68:]
    line[0].set_data(posX, posY)
    return line[0],

ani = animation.FuncAnimation(fig, update, frames=1000, blit='false', interval=30)
plt.show()

pipe.kill()
