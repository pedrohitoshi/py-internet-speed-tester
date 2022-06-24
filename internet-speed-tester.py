from tkinter import *
from PIL import Image, ImageTk
import speedtest


colorBlack = "#2a2a2a"
colorGrey = "#7f7e7e"
colorWhite = "#d4d3d3"

janela = Tk()
janela.title("PY INTERNET SPEED TESTER")
janela.geometry("400x300")
janela.configure(background=colorWhite)
janela.resizable(width=FALSE, height=FALSE)


# Separa a janela do app em 2 frames
frame_logo = Frame(janela, width=400, height=60, bg=colorBlack)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=400, height=240, bg=colorBlack)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


# Configuração do frame_logo
iconSpeed = Image.open('icon_speed.png')
iconSpeed = iconSpeed.resize((55,55))
iconSpeed = ImageTk.PhotoImage(iconSpeed)

label_logo_nome = Label(frame_logo, text="Py Internet Speed Tester", padx=10, anchor=NE, font=('Ivy 20 bold'), bg=colorBlack, fg=colorWhite)
label_logo_nome.place(x=50, y=10)

label_logo_imagem = Label(frame_logo, height=60, image=iconSpeed, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=colorBlack, fg=colorWhite)
label_logo_imagem.place(x=0, y=0)

label_logo_linha = Label(frame_logo, width=400, anchor=NW, font=('Ivy 1'), bg=colorGrey)
label_logo_linha.place(x=0, y=60)


def testarVelocidade():
  speed = speedtest.Speedtest()
  downSpeed = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
  upSpeed = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"
  ping = f"{'{:.0f}'.format(speed.results.ping)}"

  label_download['text'] = downSpeed
  label_upload['text'] = upSpeed
  label_ping['text'] = ping

  botao_testar['text'] = "Testar novamente"
  botao_testar.place(x=140, y=200)


# Configuração do frame_corpo
# Label VELOCIDADE DOWNLOAD
label_download = Label(frame_corpo, text="-", anchor=NW, font=('arial 28'), bg=colorBlack, fg=colorWhite)
label_download.place(x=25, y=30)
label_download_mbps = Label(frame_corpo, text="Mbps download", anchor=NW, font=('Ivy 10'), bg=colorBlack, fg=colorWhite)
label_download_mbps.place(x=40, y=80)

iconDownload = Image.open('icon_download.png')
iconDownload = iconDownload.resize((50,50))
iconDownload = ImageTk.PhotoImage(iconDownload)

label_icon_download = Label(frame_corpo, height=60, image=iconDownload, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=colorBlack, fg=colorWhite)
label_icon_download.place(x=155, y=35)

# Label VELOCIDADE UPLOAD
label_upload = Label(frame_corpo, text="-", anchor=NW, font=('arial 28'), bg=colorBlack, fg=colorWhite)
label_upload.place(x=260, y=30)
label_upload_mbps = Label(frame_corpo, text="Mbps upload", anchor=NW, font=('Ivy 10'), bg=colorBlack, fg=colorWhite)
label_upload_mbps.place(x=280, y=80)

iconUpload = Image.open('icon_upload.png')
iconUpload = iconUpload.resize((50,50))
iconUpload = ImageTk.PhotoImage(iconUpload)

label_icon_upload = Label(frame_corpo, height=60, image=iconUpload, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=colorBlack, fg=colorWhite)
label_icon_upload.place(x=200, y=35)

# Label TEMPO PING
label_ping = Label(frame_corpo, text="-", anchor=NW, font=('arial 28'), bg=colorBlack, fg=colorWhite)
label_ping.place(x=180, y=110)
label_ping_ms = Label(frame_corpo, text="ping ms", anchor=NW, font=('Ivy 10'), bg=colorBlack, fg=colorWhite)
label_ping_ms.place(x=180, y=150)


# Configuração do botão
botao_testar = Button(frame_corpo, command=testarVelocidade, text="Iniciar teste", font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=colorGrey, fg=colorWhite)
botao_testar.place(x=162, y=200)


janela.mainloop()