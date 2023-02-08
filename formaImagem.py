from tkinter import *
from tkinter import  filedialog
from PIL import Image,ImageTk
from tkinter import messagebox
from pathlib import Path



class Aplica(Tk):
    def __init__(self) -> None:
        super().__init__()
        
        self.posicao = self.winfo_screenwidth()
        self.tamanho_da_imagem = ''
       
        self.a = 400
        self.b = 400

        self.pos_a = StringVar()
        self.pos_b = StringVar()

        self.canvas_menu = Canvas(self,width=180,height=500,bg='grey31')
        self.canvas_menu.config(highlightcolor='white')
        self.canvas_menu.config(highlightthickness=2)
        self.canvas_menu.place(x=10,y=10)

        self.title(string='Formatação de imagem')
        
        self.iconbitmap('formata.ico')

        self.fichero = Button(self,text='Selecione uma imagem',command=self.funcao,width=20,overrelief='groove',cursor='hand2')
        self.fichero.bind('<Motion>',self.cor1)
        self.fichero.config(font='arial 13 bold')
        self.fichero.place(x=self.posicao/2.8,y=550)

        self.altura = Entry(self.canvas_menu,textvariable=self.pos_a)
        self.altura.place(x=10,y=10)

        self.lagura = Entry(self.canvas_menu,textvariable=self.pos_b)
        self.lagura.place(x=10,y=40)


        self.al = Button(self.canvas_menu,text='Aplicar',command=self.formata_foto,overrelief='groove',cursor='hand2')
        self.al.config(font='arial 10')
        self.al.config(activebackground='black')
        self.al.config(activeforeground='red')
        self.al.place(x=10,y=70)

        self.ja = Button(self.canvas_menu,text='Salvar',command=self.janela_adm,overrelief='groove',cursor='hand2')
        self.ja.config(font='arial 10')
        self.ja.config(activebackground='black')
        self.ja.config(activeforeground='red')
        self.ja.place(x=10,y=150)

        self.bt_apaga = Button(self,text='Apagar',overrelief='groove',cursor='hand2')
        self.bt_apaga.config(font='arial 10')
        self.bt_apaga.config(activebackground='black')
        self.bt_apaga.config(activeforeground='red')
        self.bt_apaga.config(command=self.apagar_imagem)
        self.bt_apaga.place(x=120,y=160)


        self.canvas = Canvas(self,width=979,height=500,bg='grey31')
        self.canvas.place(x=200,y=10)

        self.vertical = self.canvas.winfo_reqwidth()
        self.orizontal = self.canvas.winfo_reqheight()

        self.label_tamanho_imagem = Label(self)
        self.label_tamanho_imagem.config(font='arial 10 bold')
        self.label_tamanho_imagem.config(bg='grey11')
        self.label_tamanho_imagem.config(fg='white')
        self.label_tamanho_imagem.place(x=10,y=550)

    def apagar_imagem(self):
        self.canvas.delete('all')
        self.label_tamanho_imagem['text'] = ''
        self.pos_a.set('')
        self.pos_b.set('')

    def janela_adm(self):
        try:
            if self.path:
                self.janela_admin = Toplevel()
                self.janela_admin.title('janela 2')
                self.janela_admin.config(bg='lightblue')
                self.janela_admin.geometry('400x200+200+30')
                self.janela_admin.resizable(0,0)
                self.janela_admin.focus_force()
                self.janela_admin.grab_set()
                self.janela_admin.overrideredirect(True)

                self.caca = StringVar()
                self.dada = StringVar()
                tuple_ = ['png','jpg','ico']

                for a in tuple_:
                    self.radio_bt = Radiobutton(self.janela_admin,variable=self.caca,text=a,value=a,activeforeground='red')
                    self.radio_bt.config(font='arial 10 bold')
                    self.radio_bt.config(command=self.pega_radiobutton)
                    self.radio_bt.pack(anchor='w',padx=17,pady=5)

                self.bt_qui = Button(self.janela_admin,text='Salvar',activeforeground='blue',activebackground='orange')
                self.bt_qui.config(font='arial 10 bold')
                self.bt_qui.config(cursor='hand2')
                self.bt_qui.config(command=self.salva_imagem)
                self.bt_qui.place(x=200,y=120)

                self.bt_sair = Button(self.janela_admin,text='Sair',command=self.xau,width=5)
                self.bt_sair.config(activebackground='orange')
                self.bt_sair.config(activeforeground='blue')
                self.bt_sair.config(font='arial 10 bold')
                self.bt_sair.place(x=100,y=120)

                self.entry_la = Entry(self.janela_admin)
                self.entry_la.place(x=150,y=50)

                self.simbolo = Label(self.janela_admin,text='.png',bg='lightblue',font='arial 10 bold')
                self.simbolo.place(x=275,y=50)
        except:
            messagebox.showinfo('','Selecione uma imagem')

    def pega_radiobutton(self):
        self.simbolo['text'] = '.' + self.caca.get()

    def salva_imagem(self):
        if self.entry_la.get() != '':
            res = self.entry_la.get() + self.simbolo['text'] 
            print(res)
            from tkinter import ttk
            import time
            caminho = Path.home() /'Pictures'/ 'imagens'
            caminho.mkdir(exist_ok=True)
            
            self.barras = ttk.Progressbar(self.janela_admin,length=250)
            self.barras.place(x=80,y=150)
            for a in range(0,100):
                self.barras['value'] = a
                time.sleep(0.02)
                self.janela_admin.update()
            self.img2.save(f'{caminho}/{self.entry_la.get()}{self.simbolo["text"]}')
            self.canvas.delete('all')
            self.pos_a.set('')
            self.pos_b.set('')
            self.janela_admin.destroy() 
        else:
            messagebox.showinfo('','Selecione o Nome da Imagem')
        
    def cor1(self,s):
        self.fichero.config(bg='blue')
        if( s.x >= 209 or s.x <= 0) :
            self.fichero.config(bg='white')
        if(s.y >= 32 or s.y <= 1):
             self.fichero.config(bg='white')
        if self.fichero['bg'] == 'blue':
            self.fichero['fg'] = 'white'
        else:
            self.fichero['fg'] = 'black'
     
    def funcao(self):
        self.fichero['bg'] = 'white'
        self.fichero['fg'] = 'black'

        global ler_img,foto
        self.path = filedialog.askopenfilename(initialdir='/Acesso rápido',title='imagem')

        if self.path:
            ler_img = open(self.path,'rb')
            foto = ler_img.read()
            ler_img.close()
            self.img = Image.open(self.path)
            self.tamanho_da_img = self.img.size
            self.label_tamanho_imagem['text'] = f'Tamanho Original: {self.tamanho_da_img[0]} x {self.tamanho_da_img[1]} Pixel'
            self.img = self.img.resize((400,400))
            self.img_w = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(self.vertical/2,self.orizontal/2,image=self.img_w)
            self.pos_a.set(400)
            self.pos_b.set(400)
            self.formata_foto()
            self.ver_foto()
        
    def ver_foto(self):
        if self.path:
            self.img1 = Image.open(self.path).convert("RGB")
            self.img2 = self.img1.resize((int(self.b),int(self.a)))
            self.img = ImageTk.PhotoImage(self.img2)
            self.canvas.create_image(self.vertical/2,self.orizontal/2,image=self.img)

    def formata_foto(self):
        if self.altura.get() != '' and self.lagura.get() != '':
            num1 = self.altura.get()
            num2 = self.lagura.get()
            if num1.isnumeric() and num2.isnumeric():
                self.a = int(self.altura.get())
                self.b = int(self.lagura.get())
                self.ver_foto()
            else:
                messagebox.showinfo('','Digita so Números')
        
    def xau(self):
        res = self.janela_admin.winfo_geometry()
        num1 = (int(res[0:3])) + 1
        for a in range(0,num1,4):
            ba = num1 - a
            self.janela_admin.geometry('%dx%d+%d+%d' % (ba,ba/2,200,30))
            self.janela_admin.update()
        if ba == 1:
            self.janela_admin.destroy()

if __name__ == '__main__':
    root = Aplica()
    root['bg'] = 'grey11'
    root.config(highlightcolor='grey31')
    root.config(highlightthickness=3)
    root.geometry('1200x600+100+30')
    root.resizable(0,0)
    root.mainloop()