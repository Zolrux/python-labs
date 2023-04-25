import tkinter

def create_object(create_obj, object):
    if create_obj.__name__ == 'create_oval':
        create_obj(object['points'], fill=object['color'], outline=object['color'])
    elif create_obj.__name__ == 'create_text':
        create_obj(object['points'], text=object['text'], fill=object['color'])
    elif create_obj.__name__ == 'create_arc':
        create_obj(object['points'], style="pieslice", 
                   start=340, fill=object['color'], 
                   outline=object['color'], extent=180)


def main():
    width = height = 350
    objects = {
        'head': {
            'color': 'blue',
            'points': ((50, 50), (width - 50, height - 50))
        },
        'text': {
            'text': 'Непонятое',
            'color': 'black',
            'points': (35, 70)
        },
        'left_eye': {
            'color': 'white',
            'points': ((90, 85), (130, 125))
        },
        'right_eye': {
            'color': 'white',
            'points': ((170, 85), (210, 125))
        },
        "mouth": {
            'color': 'white',
            'points': ((170, 210), (210, 240))
        }
    }
    window = tkinter.Tk()
    window.title('Лабораторна робота №12')
    window.minsize(width, height)
    window.resizable(False, False)

    canvas = tkinter.Canvas(master=window, width=width,
                            height=height, background='yellow')
    canvas.pack(expand=1)

    create_object(canvas.create_oval, objects['head'])
    create_object(canvas.create_text, objects['text'])
    create_object(canvas.create_oval, objects['left_eye'])
    create_object(canvas.create_oval, objects['right_eye'])
    create_object(canvas.create_arc, objects['mouth'])

    window.mainloop()


if __name__ == '__main__':
    main()
