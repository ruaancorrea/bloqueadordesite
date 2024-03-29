# importando Tkinter

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox


# importaando pillow

from PIL import Image, ImageTk
from matplotlib.pyplot import text

import csv

# cores --------------------------------

co0 = "#f0f3f5" # Preta
co1 = "#feffff" # branca
co2 = "#3fb5a3" # verde
co3 = "#fc766d" # vermelha / red
co4 = "#403d3d" # letra
co5 = "#4a88e8" # Azul / Bblue

# criando janela ------------------------


janela = Tk ()
janela.title ("")
janela.geometry("390x350")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


# Frames --------------------------------

frame_logo = Frame(janela,width=400, height=60,bg=co1, relief="flat")
frame_logo.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela,width=400, height=400,bg=co1, relief="flat")
frame_corpo.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)


#configurando frame logo

imagem = Image.open("G:/Meu Drive/PROJETOS PYTHON/ProjetosIniciantes/bloqueadorsite/i.png")
imagem = imagem.resize((42, 42))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_logo, height=60, image=imagem, bg=co1 )
l_imagem.place(x=20, y=2)

l_logo = Label(frame_logo, text='Bloqueador De Sites', height=1, anchor=NE, font=("Ivy 25"), bg=co1, fg=co4 )
l_logo.place(x=70, y=10)

l_linha = Label(frame_logo, text='',width=445, height=1, anchor=NW, font=("Ivy 1"), bg=co2 )
l_linha.place(x=0, y=58)

# criando funcoes ----------------

global iniciar
global websites

iniciar = BooleanVar()


# funcao ver sites 

def ver_site():
    listbox.delete(0,END) 

   # ACESSANDO ARQUIVO CSV
    with open('sites.csv') as file:
       ler_csv = csv.reader(file)
       for row in ler_csv:
           listbox.insert(END,row)


# funcao inserir_site salvar ficheiro ----

def salvar_site(i):
    # acessando arquivo csv
    with open('sites.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i])
        messagebox.showinfo('Site','O site foi adicionado com sucesso')


    ver_site()


# funcao eliminar site

def deletar_site(i):

    def adicionar(i):
        # acessando arquivo csv
        with open('sites.csv', 'w', newline='') as file:
          writer = csv.writer(file)
          writer.writerows(i)
          messagebox.showinfo('Site','O site foi removido com sucesso')

         
    ver_site()
    

    nova_lista = []
    with open('sites.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            nova_lista.append(row)
            for campo in row:
                if campo==i:
                    print(campo)
                    nova_lista.remove(row)
                    
    adicionar(nova_lista)




# funcao adicionar na lista --------------

def adicionar_site():
    site = e_site.get()
    if site=='':
        pass
    else:
        listbox.insert(END, site)
        e_site.delete(0,END)

    salvar_site(site)


# funcao remover site

def remover_site():
    site = listbox.get(ACTIVE)
    sites = []
    for i in site:
        sites.append(i)
    deletar_site(sites[0])
        
    ver_site() 

def desbloquear_site():
    iniciar.set(False)
    messagebox.showinfo("Site", "Os sites na lista foram Desbloqueados")
    bloqueador_site()

def bloquear_site():
    iniciar.set(True)
    messagebox.showinfo("Site", "Os sites na lista foram Bloqueados")
    bloqueador_site()




# funcao bloqueador site
    
def bloqueador_site():

    local_do_host = r"C:\Windows\System32\drivers\etc\hosts"
    redirecionar = "127.0.0.1"

    websites = []

# acessando o ficheiro CSV 

    with open('sites.csv', newline='') as file:
         ler_csv = csv.reader(file)
         for row in ler_csv:
             websites.append(row[0])

# Verificar e escrever nos arquivos
    if iniciar.get() == True:
            with open(local_do_host, 'r') as arquivo:
                conteudo = arquivo.read()

            with open(local_do_host, 'a') as arquivo:
                for site in websites:
                    if site not in conteudo:
                     arquivo.write(redirecionar + " " + site + "\n")

    
    else:

         with open(local_do_host, 'r+') as arquivo:
            conteudo= arquivo.readlines()
            arquivo.seek(0)

            for line in conteudo:
                if not any(site in line for site in websites):
                    arquivo.write(line)

            arquivo.truncate()

    

# configurando frame corpo

l_site = Label(frame_corpo, text='DIGITE O SITE QUE DESEJA BLOQUEAR NO CAMPO ABAIXO *', height=1, anchor=NE, font=("Ivy 9 bold"), bg=co1, fg=co4 )
l_site.place(x=20, y=20)
e_site = Entry(frame_corpo, width=21, justify='left', font=("", 15), highlightthickness=1, relief=SOLID)
e_site.place(x=23, y=50)

b_adicionar = Button(frame_corpo,command=adicionar_site, text='Adicionar',width=10, height=1, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1 )
b_adicionar.place(x=267, y=50)

b_remover = Button(frame_corpo,command=remover_site, text='Remover',width=10, height=1, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1 )
b_remover.place(x=267, y=100)

b_desbloquear = Button(frame_corpo, command=desbloquear_site, text='Desbloquear',width=10, height=1, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1 )
b_desbloquear.place(x=267, y=150)

b_bloquear = Button(frame_corpo, command=bloquear_site, text='Bloquear',width=10, height=1, font=("Ivy 10 bold"), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1 )
b_bloquear.place(x=267, y=200)

listbox = Listbox(frame_corpo, font=('Arial 9 bold'), width=33, height=10)
listbox.place(x=23,y=100)



ver_site()

janela.mainloop ()