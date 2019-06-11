# By: Barry Guglielmo

# This code is written to build a 3d INTERACTIVE graph of a
# 96 well ELISA plate.

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *
import os
#ggplot must also be downloaded
#xlrd needed

def ELISA_3D():
    """Return 3D Bar Graph of all Plates"""
    #Get file directory
    file = filedialog.askopenfilename()
    #read file
    myfile = pd.ExcelFile(file)
    #Get Sheet Name and select appropriate cells
    data = myfile.parse(E2.get()).iloc[0:8,1:13] #If cells differ change here
    #ggplot is the library for interaction
    style.use('ggplot')
    #The pandas dataframe needs to be handled as a matrix for this
    datamatrix = data.as_matrix()
    #The matrix needs to be flattened
    flat = datamatrix.flatten()
    #Build the plt object
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(111, projection='3d')
    #This is the grid layout (there may be a more programatic way to do it)
    x3 = [1,1,1,1,1,1,1,1,1,1,1,1,
          2,2,2,2,2,2,2,2,2,2,2,2,
          3,3,3,3,3,3,3,3,3,3,3,3,
          4,4,4,4,4,4,4,4,4,4,4,4,
          5,5,5,5,5,5,5,5,5,5,5,5,
          6,6,6,6,6,6,6,6,6,6,6,6,
          7,7,7,7,7,7,7,7,7,7,7,7,
          8,8,8,8,8,8,8,8,8,8,8,8]
    y3 = [1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12]
    #set the axes
    z3 = np.ones(96)
    dx = np.ones(96)
    dy = np.ones(96)
    dz = flat
    #set the 3d bar up
    ax1.bar3d(x3, y3, z3, dx, dy, dz,color='#00ceaa' )
    #set the labels
    ax1.set_xlabel(E2.get())
    ax1.set_ylabel(E2.get())
    ax1.set_zlabel('Absorbance')
    #save the figure
    plt.savefig(E1.get()+'.png')
    #show the figure
    plt.show()
    #close the figure
    plt.close()
    root.destroy()


#Tkinter window to gather info and run program
root = tk.Tk()
#shape of the tk window
root.geometry = ("20x10")
#Label the text field for the outfile
L1 = Label(root, text="Save As: ")
L1.pack()
#Entry space for the outfile name
E1 = Entry(root, bd =10)
E1.pack()
#Sheet to be addressed
L2 = Label(root, text="Sheet ID: ")
L2.pack()
#Entry space for Sheet
E2 = Entry(root, bd =10)
#Auto Fill with Serotonin
E2.insert(0,"SEROTONIN")
E2.pack()
#Submit/Run button labeled compile files
B1 = Button(root, text = "Show Graph", command = ELISA_3D)
B1.pack()
#the main loop for the window we created
root.mainloop()
