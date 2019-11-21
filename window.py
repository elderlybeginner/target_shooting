#!/usr/bin/env python3
'''Input it into target shooting'''


import tkinter

# Create window
main_window = tkinter.Tk()

# Create two frames
left_frame = tkinter.Frame(main_window, borderwidth=1, relief='solid')
right_frame = tkinter.Frame(main_window, borderwidth=1, relief='solid')
left_frame.pack(side=tkinter.LEFT, expand=True, fill='both')
right_frame.pack(side=tkinter.RIGHT, expand=True, fill='both')

# Create three frames on the left
lu_frame = tkinter.Frame(left_frame, borderwidth=0, relief='solid')
lm_frame = tkinter.Frame(left_frame, borderwidth=0, relief='solid')
ld_frame = tkinter.Frame(left_frame, borderwidth=0, relief='solid')
lu_frame.pack(expand=True, fill='both')
lm_frame.pack(expand=True, fill='both')
ld_frame.pack(expand=True, fill='both')

# Divide left upper frame vertically
lul_frame = tkinter.Frame(lu_frame, borderwidth=0, relief='solid')
lur_frame = tkinter.Frame(lu_frame, borderwidth=0, relief='solid')
lul_frame.pack(side=tkinter.LEFT, expand=True, fill='both')
lur_frame.pack(side=tkinter.RIGHT, expand=True, fill='both')

# Add buttons into left-upper-left frame
lul_b1 = tkinter.Button(lul_frame, text='Calibrate')
lul_b2 = tkinter.Button(lul_frame, text='Find Holes')
lul_b3 = tkinter.Button(lul_frame, text='Fix Holes')
lul_b4 = tkinter.Button(lul_frame, text='Find Holes')
lul_b1.pack(fill='both')
lul_b2.pack(fill='both')
lul_b3.pack(fill='both')
lul_b4.pack(fill='both')

# Add buttons into left-upper-right frame
lur_l1 = tkinter.Label(lur_frame, text='Tolerance: ')
lur_l1.pack(anchor='w')
lur_l2 = tkinter.Label(lur_frame, text='Date: ')
lur_l2.pack(anchor='w', side='bottom')

# Add labels and values into left-middle frame
lm_l1 = tkinter.Label(lm_frame, text='Cp: ')
lm_l1.pack(anchor='w')
lm_l2 = tkinter.Label(lm_frame, text='Cpk: ')
lm_l2.pack(anchor='w')
lm_l3 = tkinter.Label(lm_frame, text='Centroid X, Y: ')
lm_l3.pack(anchor='w')
lm_l4 = tkinter.Label(lm_frame, text='Amount of Holes: ')
lm_l4.pack(anchor='w')
lm_l5 = tkinter.Label(lm_frame, text='Probability of:')
lm_l5.pack(anchor='w')
lm_l6 = tkinter.Label(lm_frame, text='50% in target: ')
lm_l6.pack(anchor='center')
lm_l7 = tkinter.Label(lm_frame, text='75% in target: ')
lm_l7.pack(anchor='center')
lm_l8 = tkinter.Label(lm_frame, text='95% in target: ')
lm_l8.pack(anchor='center')

# Add buttons into left-down frame
ld_b1 = tkinter.Button(ld_frame, text='Save Result')
ld_b2 = tkinter.Button(ld_frame, text='Load Result')
ld_b3 = tkinter.Button(ld_frame, text='Stats')
ld_b1.pack(fill='both')
ld_b2.pack(fill='both')
ld_b3.pack(fill='both')


# Set window parameters
main_window.geometry('640x400')
main_window.title('Target Shooting')

main_window.mainloop()
