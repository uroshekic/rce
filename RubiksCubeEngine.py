#! /usr/bin/env python3

import tkinter
from RCE import RCE

class RubiksCubeEngine:
    colorSets = [
        { 'U' : 'white', 'F' : 'green', 'R' : 'red', 'L' : 'orange', 'B' : 'blue', 'D' : 'yellow' , 'border' : 'black'},
        { 'U' : '#ffffff', 'F' : '#2ecc71', 'R' : '#c0392b', 'L' : '#e67e22', 'B' : '#3498db', 'D' : '#f1c40f' , 'border' : ''}
    ]
    colorSetNames = { 0 : 'Default', 1 : 'Modern' }
    views = { 0 : '3x2', 1 : 'Net', 2 : '3D (TO-DO)'}

    enableKeyboardShortcuts = True
    Alt = False
    
    def __init__(self):
        self.setView(1)
        self.colorSet(1)

        # GUI
        self.window = tkinter.Tk()
        self.window.title('Rubik\'s Cube Engine')

        # Menu
        menu = tkinter.Menu(self.window)
        self.window.config(menu=menu)

        # File
        file_menu = tkinter.Menu(menu)
        menu.add_cascade(label='RCE', menu=file_menu)
        
        file_menu.add_command(label='Reset', command=self.Reset)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.window.destroy)

        # Settings
        menu.add_command(label='Settings', command=self.Settings)

        # Help
        help_menu = tkinter.Menu(menu)
        menu.add_cascade(label='Help', menu=help_menu)

        help_menu.add_command(label='About', command=self.About)
        help_menu.add_separator()
        help_menu.add_command(label='Help', command=self.Help)

        
        self.labelAlg = tkinter.Label(self.window, text='Algorithm: ')
        self.entryAlg = tkinter.Entry(self.window, width=100)
        self.buttonApply = tkinter.Button(self.window, text='Apply!', command=self.Apply)
        self.buttonReset = tkinter.Button(self.window, text='Reset!', command=self.Reset)
        self.buttonClear = tkinter.Button(self.window, text='Clear!', command=self.Clear)
        self.c = tkinter.Canvas(self.window, width=600, height=475)

        # Position widgets
        self.labelAlg.grid(row=0, sticky=tkinter.E)
        self.entryAlg.grid(row=0, column=1, columnspan=2, sticky=tkinter.W)
        self.buttonReset.grid(row=1, column=0, sticky=tkinter.W)
        self.buttonClear.grid(row=1, column=1, sticky=tkinter.W)
        self.buttonApply.grid(row=1, column=2, sticky=tkinter.E)
        self.c.grid(row=2, columnspan=3)

        # Key bindings
        self.window.bind("<Alt_L>", self.AltOn)
        self.window.bind("<KeyRelease-Alt_L>", self.AltOff)
        self.window.bind("a", self.AltA)
        self.window.bind("c", self.AltC)
        self.window.bind("<Return>", self.ReturnKey)
        self.window.bind("<F1>", self.F1)

        self.entryAlg.focus_set()

        self.rc = RCE()
        self.draw() # Draw a solved cube
        
        self.window.mainloop()
        
    def colorSet(self, s):
        self.colorSetI = s
        self.colors = self.colorSets[self.colorSetI]

    def setView(self, v):
        self.view = v
    
    def draw(self):
        if self.view == 1:
            self.size = { 'cubie' : 42, 'space' : 3 }
            positions = [(1, 0), (1, 1), (2, 1), (0, 1), (3, 1), (1, 2)]
            self.c.delete(tkinter.ALL)
            for face in range(6):
                spaceX = positions[face][0]*3*(self.size['cubie']+self.size['space'])
                spaceY = positions[face][1]*3*(self.size['cubie']+self.size['space'])
                for line in range(3):
                    for sticker in range(3):
                        if face == 4:
                            i = 8-(3*line+sticker)
                        else:
                            i = 3*line+sticker
                        c = self.colors[self.rc.stickers[face][i][0]]
                        
                        self.c.create_rectangle(spaceX + 10 + sticker*(self.size['cubie']+self.size['space']),
                                                spaceY + 50 + line*(self.size['cubie']+self.size['space']),
                                                spaceX + 10 + (sticker+1)*self.size['cubie']+sticker*self.size['space'],
                                                spaceY + 50 + (line+1)*self.size['cubie']+line*self.size['space'],
                                                fill=c,
                                                outline=self.colors['border'])

        else:
            self.size = { 'cubie' : 50, 'space' : 5 }
            self.c.delete(tkinter.ALL)
            xSpace, ySpace = 0, 0
            space = (3*(self.size['cubie']+self.size['space']))
            for face in range(6):
                if face > 0: xSpace += 1.2*space
                if face == 3:
                    xSpace = 0
                    ySpace += 1.4*space
                
                self.c.create_text(10 + xSpace + 1.5*(self.size['cubie']+self.size['space']),
                                   10 + ySpace + 15, text=RCE.turns_i[face])
                for line in range(3):
                    for sticker in range(3):
                        self.c.create_rectangle(xSpace + 10 + sticker*(self.size['cubie']+self.size['space']),
                                                ySpace + 50 + line*(self.size['cubie']+self.size['space']),
                                                xSpace + 10 + (sticker+1)*self.size['cubie']+sticker*self.size['space'],
                                                ySpace + 50 + (line+1)*self.size['cubie']+line*self.size['space'],
                                                fill=self.colors[self.rc.stickers[face][3*line+sticker][0]],
                                                outline=self.colors['border'])

    def Apply(self):
        self.rc.alg(self.entryAlg.get().upper().split())
        self.draw()
        #self.entryAlg.delete(0, tkinter.END)

    def Reset(self):
        self.entryAlg.delete(0, tkinter.END)
        self.rc = RCE()
        self.draw()

    def Clear(self):
        self.entryAlg.delete(0, tkinter.END)

    def SettingsColorSetUpdate(self):
        self.colorSet(self.csi.get())
        self.draw()
    
    def SettingsViewUpdate(self):
        self.setView(self.vi.get())
        self.draw()

    def SettingsKeyboardShortcutsUpdate(self):
        self.enableKeyboardShortcuts = True if self.checkButtonShortcutsVar.get() == 1 else False
    
    def Settings(self):
        windowSettings = tkinter.Tk()
        windowSettings.title('Settings')

        # Color set
        labelColorSet = tkinter.Label(windowSettings, text='Select a color set: ')
        labelColorSet.grid(columnspan=2, sticky=tkinter.W)
        
        self.csi = tkinter.IntVar(master=windowSettings) # !!!
        for i in self.colorSetNames:
            a = tkinter.Radiobutton(windowSettings, text=self.colorSetNames[i], value=i, variable=self.csi, command=self.SettingsColorSetUpdate)
            a.grid(column=1, sticky=tkinter.W)
            if i == self.colorSetI:
                a.select()

        # View
        labelType = tkinter.Label(windowSettings, text='Select a view: ')
        labelType.grid(columnspan=2, sticky=tkinter.W)

        self.vi = tkinter.IntVar(master=windowSettings)
        for i in self.views:
            a = tkinter.Radiobutton(windowSettings, text=self.views[i], value=i, variable=self.vi, command=self.SettingsViewUpdate)
            a.grid(column=1, sticky=tkinter.W)
            if i == self.view:
                a.select()

        # Enable keyboard shorcuts
        self.checkButtonShortcutsVar = tkinter.IntVar(master=windowSettings)
        checkButtonShortcuts = tkinter.Checkbutton(windowSettings, text='Enable keyboard shortcuts', variable=self.checkButtonShortcutsVar, command=self.SettingsKeyboardShortcutsUpdate)
        if (self.enableKeyboardShortcuts): checkButtonShortcuts.select()
        checkButtonShortcuts.grid(columnspan=2)
                
        windowSettings.mainloop()
        
    def About(self):
        windowAbout = tkinter.Tk()
        windowAbout.title('About')
        label = tkinter.Label(windowAbout, text='This is a simple Rubik\'s Cube Engine written in Python by Uroš Hekić.')
        label.grid(sticky=tkinter.W)
        windowAbout.mainloop()
    
    def Help(self):
        windowHelp = tkinter.Tk()
        windowHelp.title('Help')

        label = tkinter.Label(windowHelp, text='''Turns/rotations: U, F, R, L, B, D, x, y, z. Suffixes: ', 2.
Turns/rotations in an algorithm should be separated by spaces.

There are 6 faces on a cube. Each face is represented by a letter, according to where it is located. 
These faces make the most sense when you hold the cube with one face parallel to the ground and one face facing you,  
but algorithm pages will often display the cube so that you can see the front, right, and top faces.  
The six faces are: 
- F (Front) - the side facing you. 
- U (Up) - the side facing upwards. 
- R (Right) - the side facing to the right. 
- B (Back) - the side facing away from you. 
- L (Left) - the side facing to the left. 
- D (Down) - the side facing downwards. 
 
A turn of one layer of one of the six faces of the cube is written by adding a suffix to the face\'s name.  
There are three possible turns that can be applied to a face, and all moves should be applied  
as if you were looking at the face straight-on. Using the U face as an example, the following are possible turns: 
- U - A 90-degree clockwise turn of the U face. 
- U\' - A 90-degree counterclockwise turn of the U face. 
- U2 - A 180-degree turn (either clockwise or counterclockwise) of the U face.
(From Wiki @ Speedsolving.com)

Keyboard shortcuts:
- Apply: Alt-A / Enter:
- Clear: Alt-C''', justify=tkinter.LEFT)
        label.grid(sticky=tkinter.W)

        windowHelp.mainloop()

    def AltOn(self, event):
        self.Alt = True

    def AltOff(self, event):
        self.Alt = False

    def AltA(self, event):
        if (self.enableKeyboardShortcuts and self.Alt): self.Apply()

    def AltC(self, event):
        if (self.enableKeyboardShortcuts and self.Alt): self.Clear()

    def ReturnKey(self, event):
        if (self.enableKeyboardShortcuts): self.Apply()

    def F1(self, event):
        if (self.enableKeyboardShortcuts): self.Help() # :D


cube = RubiksCubeEngine()
