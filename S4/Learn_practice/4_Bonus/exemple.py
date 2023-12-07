from threading import Thread
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import time
import numpy as np

def timer():
    start = time.time()
    
    while True:
        fin = time.time()
        diff = int(fin - start)
        h, s = divmod(diff, 3600)
        m, s = divmod(diff, 60)
        print( '<== {h} : {m} : {s} ==>'.format(
            h = str(h).zfill(2),
            m = str(m).zfill(2),
            s = str(s).zfill(2),
        ), end='\r')
        time.sleep(1)
        

def animation():

    # Create a figure and axis
    fig, ax = plt.subplots()
    x_data = np.linspace(0, 2*np.pi, 100)
    line, = ax.plot(x_data, np.sin(x_data))

    # Animation update function
    def update(frame):
        # Update the y-data of the line (sin function with a phase shift)
        line.set_ydata(np.sin(x_data + frame/10))
        return line,

    # Create the animation
    animation = FuncAnimation(fig, update, interval=50)

    # Display the animation
    plt.show()


thread1 = Thread(target= timer)
thread2 = Thread(target= animation)

thread1.start()
thread2.start()
