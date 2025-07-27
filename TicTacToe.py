from tkinter import *
import random

def play(row, column):
    global p
    if buttons[row][column]['text'] == '' and checkwinner() is False:
        buttons[row][column]['text'] = p
        result = checkwinner()
        if result is False:
            p = player[1] if p == player[0] else player[0]
            l.config(text=p + ' turn')
        elif result is True:
            l.config(text=p + ' wins')
        elif result == 'Draw':
            l.config(text='Draw')

def checkwinner():
    # Rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            return True
    # Columns
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != '':
            return True
    # Diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    if empty() is False:
        return 'Draw'
    return False

def empty():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == '':
                return True
    return False

def restart():
    global p
    p = random.choice(player)
    l.config(text=p + ' turn')
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''

# GUI
window = Tk()
window.title('Tic Tac Toe')
window.config(bg='gray')

player = ['X', 'O']
p = random.choice(player)

Label(window, text='Tic Tac Toe Game', font=('Impact', 30), bg='gray').pack()
l = Label(window, text=p + ' turn', font=('Impact', 30), bg='gray')
l.pack()

frame = Frame(window)
frame.pack()

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text='', width=10, height=5,
                                   font=('Arial', 20),
                                   command=lambda row=row, col=col: play(row, col))
        buttons[row][col].grid(row=row, column=col)

restart_button = Button(window, text='Restart', font=('Impact', 20), command=restart)
restart_button.pack(pady=10)

window.mainloop()
