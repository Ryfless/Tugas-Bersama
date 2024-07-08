import tkinter as tkr
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from tkinter.messagebox import askokcancel, showinfo

root = tkr.Tk()
class Simple(tkr.Frame):
    def __init__(self, parent=None, file=None):
        tkr.Frame.__init__(self, parent)
        self.frm = tkr.Frame(parent)
        self.frm.pack(fill=tkr.X)
        self.layoutKolom = tkr.Frame(root)
        self.buatNameFile()
        parent.title('Text editor by kabane shirotsuki')
        self.buatTombol()
        self.kolomTextUtama()
        self.indeks = 1.0
        self.path = ''
        
    def buatNameFile(self):
        self.label = tkr.Label(self.frm, text="File Name: ")
        self.label.pack(side=tkr.LEFT)
        self.nameVar = StringVar()
        self.nameEntry = tkr.Entry(self.frm, textvariable=self.nameVar)
        self.nameEntry.pack(side=tkr.LEFT, fill=tkr.X, expand=True)
        
    def buatTombol(self):
        tkr.Button(self.frm, text='Open', 
                   command=self.openFile).pack(side=tkr.LEFT)
        tkr.Button(self.frm, text='Save', 
                   command=self.commandSave).pack(side=tkr.LEFT)
        tkr.Button(self.frm, text='Exit',
                   command=self.commandExit).pack(side=tkr.LEFT)
                   
    def kolomTextUtama(self):
        scroll = tkr.Scrollbar(self)
        kolomTeks = tkr.Text(self, relief=SUNKEN)
        scroll.config(command=kolomTeks.yview)
        kolomTeks.config(yscrollcommand=scroll.set)
        scroll.pack(side=tkr.RIGHT, fill=tkr.Y)
        kolomTeks.pack(side=tkr.LEFT, expand=tkr.YES, fill=tkr.BOTH)
        self.kolomTeks = kolomTeks
        self.pack(expand=tkr.YES, fill=tkr.BOTH)
        
    def commandSave(self):
        if self.path:
            alltext = self.gettext()
            open(self.path, 'w').write(alltext)
            showinfo('Berhasil', 'File telah disimpan')
        else:
            tipeFile = [('Text file', '*.txt'), ('Python File', '*.py'), ('All files', '.*')]
            filename = asksaveasfilename(filetypes=tipeFile)
            if filename:
                alltext = self.gettext()
                open(filename, 'w').write(alltext)
                self.path = filename
                self.nameVar.set(os.path.basename(filename))
                showinfo('Berhasil', 'File telah disimpan')
                
    def openFile(self):
        tipeFile = [('Text file', '*.txt'), ('Python File', '*.py'), ('All files', '.*')]
        filename = askopenfilename(filetypes=tipeFile)
        if filename:
            alltext = open(filename, 'r').read()
            self.kolomTeks.delete(1.0, END)
            self.kolomTeks.insert(1.0, alltext)
            self.path = filename
            self.nameVar.set(os.path.basename(filename))
            
    def gettext(self):
        return self.kolomTeks.get(1.0, END)
        
    def commandExit(self):
        ans = askokcancel('Exit', 'Anda yakin ingin keluar?')
        if ans:
            tkr.Frame.quit(self)

Simple(root)
tkr.mainloop()

