from tkinter import *
import tkinter.messagebox
import spacy
from spacy.language import Language
from spacy.matcher import Matcher, phrasematcher
from spacy.tokens import Doc, DocBin, Span, Token
from functools import partial

from app.genie_attrs import Gfile
from app.genie_comps import genies
from app.genie_tmplt import genie_htm

import spacy

nlp = spacy.load("./app/genie/model-best")



class genie_guis():

    def __init__(self):
        self.genie = Tk()
        print("genie started...")
        stores = []
    
    def create_window(self,title,w):
        self.genie.wm_title(title)
        self.genie.wm_geometry(w)
        print("genie loading a window..")

    @staticmethod
    def genie_half_screen(z,ww,hh):
        global w,h 
        w,h = z.winfo_screenwidth(),z.winfo_screenheight()
        z.geometry("{}x{}+{}+{}".format(ww, hh, int((w/2) - (ww/1.9)), int((h/2.2) - (hh/2))))


    def genie_config(self,vals):
        self.genie.config(background=vals)
        print("genie config...")

    def genie_resize(self,b,s):
        self.genie.wm_resizable(b,s)


    def splash_for_genie(self,photo):
        okey = self.genie
        st = okey
        st.overrideredirect(True)
        genie_guis.genie_half_screen(st,476,240)
        l = PhotoImage(file='.\{0}'.format(photo))
        z = Label(st, image=l, background="white")
        z.pack()
        z.after(3000,st.destroy)
        st.mainloop()
        print("genie loaded welcome screen...")

    def genie_icon(self,m):
        m.iconbitmap("./app/imgs/genie.ico")


    def genie_npopups(texst):
        okey = Tk()
        st = okey
        st.overrideredirect(True)
        st.config(background="#000")
        genie_guis.genie_half_screen(st,400,90)
        z = Label(st, text=texst, background="#000", fg="white", font=16, wraplength=390)
        z.pack()
        z.place(relx=0.029,rely=1.0,anchor="sw",height=90)
        z.after(3000,st.destroy)
        st.mainloop()
        print("genie popups...")

    def genie_entry_box(self,ss):
        print("genie mwindow...")
        g_wish = Entry(ss, width=100, bg="#3EB4F1", fg="#fff", font=('Arial', 14), border=0)
        g_wish.pack(padx=0,pady=0, side="bottom")
        g_wish.place(relx=0.029,rely=1.0,anchor="sw",height=80)
        def gamy(e):
            mm = []
            mm.append(g_wish.get())
            Doc = mm


            doc = []
            yyz = []
            for x in nlp.pipe(Doc):
                doc.append(x)
                x = str(x).strip()
                yyz.append(x)


            def hubs(token):
                cc = [
                "download","npm","pkg","minify","css","me","email",
                "yarn","give","typeface","goldenratio","get","hashtag","grid",
                "make","create","random","text","system","12","validate"
                ]
                return token.text in cc

            Token.set_extension("is_hubs",getter=hubs, force=True)


            pp = {}
            count = 0
            for m in range(0, len(doc)):
                count += 1
                pp[str(doc[m])] = {yy._.is_hubs for yy in doc[m]}

            def g_commands(name,okey=None,ind=None):
                for xx, yy in pp.items():
                    if name in str(xx):
                        for xxxx in range(0, len(yyz)):
                            if name in yyz[xxxx]:
                                return name

            def genie_mtch():
                g_cmds = partial(g_commands)
                g_mtch = {
                "0": g_cmds("npm page") == "npm page",
                "1": g_cmds("give me goldenratio") == "give me goldenratio",
                "2": g_cmds("get hashtag") == "get hashtag",
                "3": g_cmds("download npm pkg") == "download npm pkg",
                "4": g_cmds("minify css") == "minify css",
                "5": g_cmds("create random text") == "create random text",
                "6": g_cmds("make 12 grid") == "make 12 grid",
                "7": g_cmds("validate email") == "validate email"
                }

                ll = "".join([x  for x,y in g_mtch.items() if y == True])

                try:
                    match(ll):
                        case "0":
                            genies.g_np(mm)
                            self.z = genies.g_jthat("npm page")
                            genie_guis.genie_npopups(texst=self.z) 
                        case "1":
                            genie_htm.genie_base(genies.g_fontscale(1.618))
                            self.z = genies.g_jthat("give me goldenratio")
                            genie_guis.genie_npopups(texst=self.z)  
                        case "2":
                            genies.g_hashtg(mm)
                            self.z = genies.g_jthat("get hashtag")
                            genie_guis.genie_npopups(texst=self.z) 
                        case "3":
                            genies.g_pkgdwld(mm)
                            self.z = genies.g_jthat("download npm pkg")
                            genie_guis.genie_npopups(texst=self.z) 
                        case "4":
                            genies.g_cssoneliner(mm)
                            self.z = genies.g_jthat("minify css")
                            genie_guis.genie_npopups(texst=self.z)
                        case "5":
                            genies.g_crtrndm()
                            self.z = genies.g_jthat("create random text")
                            genie_guis.genie_npopups(texst=self.z) 
                        case "6":
                            genies.g_gdsytm(mm)
                            self.z = genies.g_jthat("make 12 grid")
                            genie_guis.genie_npopups(texst=self.z) 
                        case "7":
                            genies.g_chkmail(mm)
                            self.z = genies.g_jthat("validate email")
                            genie_guis.genie_npopups(texst=self.z)
                        case "_":
                            genie_guis.genie_npopups([zz for zz in mm])
                except:
                    genie_guis.genie_npopups("gerror")
            g_wish.delete(0,END)
            genie_mtch()
            print("genie cmds succesfully runs..")
        self.genie.bind('<Return>',gamy)


    def genie_close(self):
        genie_ifs = tkinter.messagebox.askyesnocancel("HMM :(", "do you want to close ?")
        if genie_ifs == True:
            self.genie.destroy()
            print("genie closed")
        elif genie_ifs == False:
            tkinter.messagebox.showinfo("master","welcome back")
            print("genie re-call again")
    
    def genie_popup(self,ll):
        okey = ll
        st = okey
        genie_guis.genie_half_screen(st,476,240)
        z = Label(st, background="white", width=100, text="sdafasfsadf")
        z.pack()
        st.mainloop()


    def genie_protocols(self,m,k):
        self.genie.wm_protocol(m, k)


    def end_genie(self):
        self.genie.mainloop()
        print("genie ends..")