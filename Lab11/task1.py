import tkinter

def init_frame(w, dct):
	frame = tkinter.Frame(master=w, pady=5)
	frame.grid(row=dct["position"][0], column=dct["position"][1])
	label = tkinter.Label(master=frame, text=dct["title"])
	label.grid()
	entry = tkinter.Entry(master=frame)
	entry.grid()
	return entry

def init_button(w, dct):
	btn = tkinter.Button(master=w, text=dct["title"], pady=10)
	btn.grid(row=dct["position"][0], column=dct["position"][1], 
	  			padx=10, pady=25, sticky="we")
	return btn

def calculate(event, *args):
	sum = 0
	clear_entries = []
	for entry in args[0]:
		value = entry.get()
		if not entry.get():
			value = 0
		else:
			if float(value) < 0:
				clear_entries.append(entry)
				continue
		sum += float(value)
	if len(clear_entries):
		clear_widgets(event, clear_entries, [args[1]])
	args[1]['text'] = "Итоговая сумма: {:.2f}".format(sum)

def clear_widgets(event, *args):
	for widgets in args:
		for widget in widgets:
			if isinstance(widget, tkinter.Entry):
				widget.delete(0, 'end')
			if isinstance(widget, tkinter.Label):
				widget['text'] = "Итоговая сумма: 0.0"

def main():
	set_frames = [
		{ "title": "Вода", "position": [1, 0]	},
		{ "title": "Газ",  "position": [1, 1]	},
		{ "title": "Свет", "position": [2, 0]	},
		{ "title": "Отопление",	"position": [2, 1] }]
	set_buttons = [
		{ "title": "Рассчитать", "position": [3, 0]	},
		{ "title": "Очистить", "position": [3, 1]	}]	
	get_entries = []
	get_buttons = []
	
	window = tkinter.Tk()
	window.title("Лабораторна робота №11")
	window.minsize(350, 280)
	window.resizable(False, False)
	title = tkinter.Label(master=window, 
		       				 text="Подсчет расходов по квартире", 
		       				 font=("Arial", 16))
	title.grid(row=0, column=0, columnspan=2, padx=25)

	for i in range(len(set_frames)):
		get_entries.append(init_frame(window, set_frames[i]))
	
	for i in range(len(set_buttons)):
		get_buttons.append(init_button(window, set_buttons[i]))

	frame = tkinter.Frame(master=window, padx=10)
	frame.grid(row=4, column=0, columnspan=2)
	result_label = tkinter.Label(master=frame, background="#fff", text="Итоговая сумма: 0.0")
	result_label.grid()

	get_buttons[0].bind('<ButtonPress>', 
		     				  lambda arg: calculate(tkinter.Event, get_entries, result_label))
	
	get_buttons[1].bind('<ButtonPress>', 
		     				  lambda arg: clear_widgets(tkinter.Event, get_entries, [result_label]))
	window.mainloop()

if __name__ == '__main__':
	main()