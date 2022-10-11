from Downloader \
    import YTDownload

from tkinter \
    import *

from tkinter \
    import filedialog, messagebox

import webbrowser

onlyaudiobool = True

def help_fun(event):
    def waithelp():
        help.config(image= helpUnPressed)
    help.config(image = helpPressed)
    webbrowser.open_new("https://milfuegosxd.github.io/RoKo.github.io/")
    help.after(250, waithelp)

def download_fun(event):
    def waitdownload():
        Download.config(image= DownloadUnPressed)
    url = LinkBox.get()
    output = filedialogBox.get()
    Download.config(image=DownloadPressed)
    try:
        if len(url) == 0 or len(output) == 0:
            messagebox.showwarning("Información incompleta", "Rellena correctamente los espacios.")
        elif onlyaudiobool == True:
            if 'list=' in url:
                question = messagebox.askyesno("Playlist encontrada", "El enlace insertado corresponde a una Playlist.\nLa descarga podría demorarse\n¿Deseas continuar?")
                if question == True:
                    download = YTDownload(url, output)
                    download.mp3_download()
                    messagebox.showinfo('Fin de la descarga', "La descarga ha finalizado")
                else:
                    pass
            else:
                download = YTDownload(url, output)
                download.mp3_download()
                messagebox.showinfo('Fin de la descarga', "La descarga ha finalizado")
        else:
            if "list=" in url:
                question = messagebox.askyesno("Playlist encontrada", "El enlace insertado corresponde a una Playlist.\nLa descarga podría demorarse\n¿Deseas continuar?")
                if question == True:
                    download = YTDownload(url, output)
                    download.mp4_download()
                    messagebox.showinfo('Fin de la descarga', "La descarga ha finalizado")
                else:
                    pass
            else:
                download = YTDownload(url, output)
                download.mp4_download()
                messagebox.showinfo('Fin de la descarga', "La descarga ha finalizado")
    except AttributeError:
        messagebox.showerror("YouTube Link", f"{url}\nNo es un enlace de YouTube")
    finally:
        Download.after(250, waitdownload)


def filedialog_fun(event):
    def waitfiledialog():
        filedialogButton.config(image= filedialogUnPressed)
    filedialogButton.config(image=filedialogPressed)

    out = filedialog.askdirectory()
    if out == "":
        pass
    else:
        filedialogBox.delete(0, END)
        filedialogBox.insert(0, out)
    filedialogButton.after(250, waitfiledialog)

def onlyaudio_fun(event):
    global onlyaudiobool
    if onlyaudiobool == False:
        video.config(image=videoUnPressed)
        onlyaudiobutton.config(image=onlyaudioPressed)
        onlyaudiobool = True
    else:
        video.config(image=videoPressed)
        onlyaudiobutton.config(image=onlyaudioUnPressed)
        onlyaudiobool = False

def centrar_fun():
    
    wtotal = window.winfo_screenwidth()
    htotal = window.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 1280
    hventana = 720

    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)

    #  Se lo aplicamos a la geometría de la ventana
    window.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))


window = Tk()
centrar_fun()
window.configure(bg = "#ffffff")
window.title("Roko!")

# --- Setting Canvas --- #
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# --- Background --- #
background_img = PhotoImage(file = f"src/assets/background.png")
background = canvas.create_image(
    595.0, 397.0,
    image=background_img)

# --- PhotoImages --- #
helpPressed = PhotoImage(file = f"src/assets/helpPressed.png")
helpUnPressed = PhotoImage(file = f"src/assets/helpUnPressed.png")
filedialogPressed = PhotoImage(file = f"src/assets/filedialogPressed.png")
filedialogUnPressed = PhotoImage(file = f"src/assets/filedialogUnPressed.png")
DownloadPressed = PhotoImage(file = f"src/assets/DownloadPressed.png")
DownloadUnPressed = PhotoImage(file = f"src/assets/DownloadUnPressed.png")
onlyaudioPressed = PhotoImage(file = f"src/assets/onlyaudioPressed.png")
onlyaudioUnPressed = PhotoImage(file = f"src/assets/onlyaudioUnPressed.png")
videoPressed = PhotoImage(file = f"src/assets/videoPressed.png")
videoUnPressed = PhotoImage(file = f"src/assets/videoUnPressed.png")


# --- Buttons --- #
help = Label(
    image = helpUnPressed,
    background="#2A50AF", 
    cursor="hand2")

help.place(
    x = 122, y = 579,
    width = 218,
    height = 65)
help.bind('<Button-1>', help_fun)

Download = Label(
    image = DownloadUnPressed,
    background="#ffffff", 
    cursor="hand2")


Download.place(
    x = 807, y = 528,
    width = 218,
    height = 64)

Download.bind("<Button-1>", download_fun)

onlyaudiobutton = Label(
    image = onlyaudioPressed,
    background="#ffffff", 
    cursor="hand2")

onlyaudiobutton.place(
    x = 630, y = 441,
    width = 218,
    height = 64)

onlyaudiobutton.bind("<Button-1>", onlyaudio_fun)



video = Label(
    image = videoUnPressed,
    background="#ffffff", 
    cursor="hand2")


video.place(
    x = 998, y = 441,
    width = 218,
    height = 64)

video.bind("<Button-1>", onlyaudio_fun)


filedialogButton = Label(
    image = filedialogUnPressed,
    background="#2A50AF", 
    cursor="hand2"
)

filedialogButton.place(
    x = 1168, y = 328,
    width = 48,
    height = 45)

filedialogButton.bind("<Button-1>", filedialog_fun)



# Entries
LinkBox = Entry(
    bd = 0,
    bg = "#d9d9d9",
    font = "curier 20",
    highlightthickness = 0)

LinkBox.place(
    x = 612, y = 170,
    width = 604,
    height = 73)

filedialogBox = Entry(
    bd = 0,
    bg = "#d9d9d9",
    font="curier 20",
    highlightthickness = 0)

filedialogBox.place(
    x = 612, y = 313.5,
    width = 544,
    height = 73)

window.resizable(False, False)
window.mainloop()
