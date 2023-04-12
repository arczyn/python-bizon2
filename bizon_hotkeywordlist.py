from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory



root_frazy = Tk()
root_frazy.title("Bizon - frazy użytkownika")
root_frazy.geometry("600x600")
list_chk_status = []
lista_fraz = []
entries = []
chk_fraza = []
entry_fraza = []
button_fraza_minus = []
frazy_output = []

def phrase_adder_hurtowy10():
    global filepath_frazy
    global propo_list
    filepath_frazy = filedialog.askopenfilename(initialdir="c:\\Users", title="Dialog box")
    label_path_frazy = Label(frame_odpalaj, text=filepath_frazy, fg="blue")
    label_path_frazy.pack(anchor="w")

    my_file = open(filepath_frazy, "r", encoding="utf-8")  # adres pliku z propozycjami fraz do analizy
    propo_file = my_file.read()
    my_file.close()
    propo_list = propo_file.split("\n")

    lista_fraz.clear() #czyścimy listę fraz
    chk_fraza.clear() #czyścimy listy samych czeckboksów
    button_fraza_minus.clear() #czyścimi listę przycisków z minusem
    for pole in entry_fraza: #dla każdego pola z frazami w okienku
        lista_fraz.append(str(pole.get()))  #na listę fraz wpisz jego zawartość
    #lista_fraz.append(str(entry_adder.get())) #dopisujemy też nową frazę
    lista_fraz.extend(propo_list)
    for i in range(len(propo_list)):
        list_chk_status.append("")  # dopisuję nową zmienną statusu czeckboksa, na potrzeby nowej frazy
        list_chk_status[len(list_chk_status) - 1] = Variable()  # tworzę z niej zmienną tkinterową

    entry_fraza.clear() #czyścimy listę pól z frazami
    for widget in frame_frazy.winfo_children(): #niczymy wszystkie widżety w ramce, żeby stworzyć nowe
        widget.destroy()
    for fraza in range(len(lista_fraz)): #odbudowujemy ramkę
        frame_frazy_wiersz = Frame(frame_frazy)
        frame_frazy_wiersz.pack(anchor="w")
        chk_fraza.append("")
        chk_fraza[fraza] = Checkbutton(frame_frazy_wiersz, variable=list_chk_status[fraza])
        chk_fraza[fraza].pack(anchor="w", side="left")
        entry_fraza.append("")
        entry_fraza[fraza] = Entry(frame_frazy_wiersz, width=80)
        entry_fraza[fraza].insert(END, lista_fraz[fraza])
        entry_fraza[fraza].pack(anchor="w", side="left")
        button_fraza_minus.append("")
        tekst = " - "
        button_fraza_minus[fraza] = Button(frame_frazy_wiersz, text=tekst, command=lambda x2=fraza: delete_phrase10(x2))
        button_fraza_minus[fraza].pack(anchor="w", side="left")
    entry_adder.delete(0, END) #czyszczenie pola do wprowadzania nowej frazy

def phrase_adder10():
    lista_fraz.clear() #czyścimy listę fraz
    chk_fraza.clear() #czyścimy listy samych czeckboksów
    button_fraza_minus.clear() #czyścimi listę przycisków z minusem
    for pole in entry_fraza: #dla każdego pola z frazami w okienku
        lista_fraz.append(str(pole.get()))  #na listę fraz wpisz jego zawartość
    lista_fraz.append(str(entry_adder.get())) #dopisujemy też nową frazę
    entry_fraza.clear() #czyścimy listę pól z frazami
    for widget in frame_frazy.winfo_children(): #niczymy wszystkie widżety w ramce, żeby stworzyć nowe
        widget.destroy()
    list_chk_status.append("") #dopisuję nową zmienną statusu czeckboksa, na potrzeby nowej frazy
    list_chk_status[len(list_chk_status) - 1] = Variable() #tworzę z niej zmienną tkinterową
    for fraza in range(len(lista_fraz)): #odbudowujemy ramkę
        frame_frazy_wiersz = Frame(frame_frazy)
        frame_frazy_wiersz.pack(anchor="w")
        chk_fraza.append("")
        chk_fraza[fraza] = Checkbutton(frame_frazy_wiersz, variable=list_chk_status[fraza])
        chk_fraza[fraza].pack(anchor="w", side="left")
        entry_fraza.append("")
        entry_fraza[fraza] = Entry(frame_frazy_wiersz, width=80)
        entry_fraza[fraza].insert(END, lista_fraz[fraza])
        entry_fraza[fraza].pack(anchor="w", side="left")
        button_fraza_minus.append("")
        tekst = " - "
        button_fraza_minus[fraza] = Button(frame_frazy_wiersz, text=tekst, command=lambda x2=fraza: delete_phrase10(x2))
        button_fraza_minus[fraza].pack(anchor="w", side="left")
    entry_adder.delete(0, END) #czyszczenie pola do wprowadzania nowej frazy

def delete_phrase10(numer_frazy):
    lista_fraz.clear()
    for pole in entry_fraza: #dla każdego pola z frazami w okienku
        lista_fraz.append(str(pole.get()))  #na listę fraz wpisz jego zawartość
    lista_fraz.pop(numer_frazy)
    list_chk_status.pop(numer_frazy)
    chk_fraza.clear()  # czyścimy listy samych czeckboksów
    button_fraza_minus.clear() #czyścimi listę przycisków z minusem
    entry_fraza.clear()  # czyścimy listę pól z frazami
    for widget in frame_frazy.winfo_children(): #niczymy wszystkie widżety w ramce, żeby stworzyć nowe
        widget.destroy()
    for fraza in range(len(lista_fraz)): #odbudowujemy ramkę
        frame_frazy_wiersz = Frame(frame_frazy)
        frame_frazy_wiersz.pack(anchor="w")
        chk_fraza.append("")
        chk_fraza[fraza] = Checkbutton(frame_frazy_wiersz, variable=list_chk_status[fraza])
        chk_fraza[fraza].pack(anchor="w", side="left")
        entry_fraza.append("")
        entry_fraza[fraza] = Entry(frame_frazy_wiersz, width=80)
        entry_fraza[fraza].insert(END, lista_fraz[fraza])
        entry_fraza[fraza].pack(anchor="w", side="left")
        button_fraza_minus.append("")
        tekst = " - "
        button_fraza_minus[fraza] = Button(frame_frazy_wiersz, text=tekst, command=lambda x2=fraza: delete_phrase10(x2))
        button_fraza_minus[fraza].pack(anchor="w", side="left")
    entry_adder.delete(0, END) #czyszczenie pola do wprowadzania nowej frazy

def something10():
    frazy_output.clear()
    for pole in entry_fraza: #dla każdego pola z frazami w okienku
        frazy_output.append(str(pole.get()))  #na listę fraz wpisz jego zawartość
    entry_list = ''
    for y in frazy_output:
        entry_list = entry_list + y + "\n"
    my_label.config(text=entry_list)

#Nagłówek
text_label = Label(root_frazy, text = "Frazy użytkownika", font='Helvetica 16 bold')
text_label.pack()

#Odrzucanie rzadkich fraz
frame_drobne = Frame(root_frazy)
frame_drobne.pack(anchor="w")
label_drobne =Label(frame_drobne, text="Lista fraz", font='Helvetica 10 bold')
label_drobne.pack(anchor="w")

frame_frazy = Frame(root_frazy)
frame_frazy.pack(anchor="w")

frame_nowe = Frame(root_frazy)
frame_nowe.pack(anchor="w")

#Odpalamy!
frame_odpalaj = Frame(root_frazy)
frame_odpalaj.pack(anchor="w")

label_adder =Label(frame_odpalaj, text="Nowa fraza")
label_adder.pack(anchor="w")

entry_adder = Entry(frame_odpalaj, width=80)
entry_adder.insert(END, "tu wpisz nową frazę")
entry_adder.pack(anchor="w")

btn_xls_akc = Button(frame_odpalaj, text='Wczytaj plik z frazami', command=phrase_adder_hurtowy10)
btn_xls_akc.pack(anchor="w")

adder = Button(frame_odpalaj, text="Dodaj frazę", command=phrase_adder10)
adder.pack()
rozrusznik = Button(frame_odpalaj, text="Zapisz frazy z okienek", command=something10)
rozrusznik.pack()

my_label = Label(frame_odpalaj, text="Zapisane frazy...")
my_label.pack()

root_frazy.mainloop()
for i in frazy_output:
    print(i)
