from tkinter import *
from PIL import Image
import pygame
import random


# генерируем и возвращаем ключ
def GetKey():
    indexes = [int(i) for i in lbl_dec.get()]
    if len(indexes) != 3:
        lbl_key.delete(0, last=END)
        lbl_key.insert(0, "Неправильно введён код!")
    else:
        key = ' KEY: '
        pool = list('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
        random.shuffle(pool)

        # я решил, что если делать на смещение на index влево и вправо поочерёдно,
        # то будут постоянно встречаться повторяющиеся элементы, так чтодопольнительно делаем сдвиг на 5 символов.
        # берём последовательность посередине
        index = len(pool)//2
        key += ''.join(pool[index: index+5]) + '-'
        # двигаем ВПРАВО последовательность на indexes[0] + 5
        index += indexes[0] + 5
        key += ''.join(pool[index: index+4]) + '-'
        # двигаем ВЛЕВО последовательность на indexes[1] + 5
        index -= indexes[1] + 5
        key += ''.join(pool[index: index+3]) + '-'
        # двигаем ВПРАВО последовательность на indexes[2] + 5
        index += indexes[2] + 5
        key += ''.join(pool[index: index+2])

        lbl_key.delete(0, last=END)
        lbl_key.insert(0, key)


# отрисовка анимации
def update(index):
    frame = image[index]
    index += 1
    if index == frames:
        index = 0
    gif_label.configure(image=frame)
    window.after(50, update, index)


# интерфейс
window = Tk()
window.title('Skeletons Keys')
window.geometry('500x480')
window['background'] = 'black'

gif_label = Label()
gif_label.grid(column=0, row=0, columnspan=3, sticky='w', padx=55, pady=15)

lbl_key = Entry(width=28, bg='black', fg="white", font=("Arial", 15))
lbl_key.insert(0, " KEY: ")
lbl_key.grid(column=0, row=1, sticky='w', padx=55)

btn = Button(text="Get Key", font=("Arial", 13), bg="black", fg="white", padx=25, pady=5, command=GetKey)
btn.grid(column=0, row=2, sticky='w', padx=55, pady=10)

lbl_dec = Entry(width=10, bg='black', fg='white', justify=CENTER, font=("Arial", 20))
lbl_dec.grid(column=0, row=2, padx=200)


# музыка
music = "skeletons8bit.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()

# список фреймов гифки
gif = 'skeletons.gif'
frames = Image.open(gif).n_frames
image = [PhotoImage(file=gif, format=f'gif -index {i}') for i in range(frames)]

window.after(0, update, 0)
window.mainloop()
