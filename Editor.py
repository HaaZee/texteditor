from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox
from tkinter import *
import os

class Text_Editor:
    def __init__(self, root):
        self.root = root
        self.fileOpen = ""
        root.title(" Text Editor | Unsaved Document")
        root.geometry("900x900+500+70")
        menubar = Menu(root)
        root.config(menu=menubar)

        fileMenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New File", command=self.file_new)
        fileMenu.add_separator()
        fileMenu.add_command(label="Save As", command=self.file_saveAs)
        fileMenu.add_command(label="Save", command=self.file_save)
        fileMenu.add_command(label="Open", command=self.file_open)

        helpMenu = Menu(menubar)
        menubar.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="Help", command=self.editorHelp)
        helpMenu.add_command(label="About", command=self.editorAbout)


        self.textArea = scrolledtext.ScrolledText(root, width=900, height=900)
        self.textArea.pack()

    # def checkChanged(self):
    #     if self.fileOpen != "":
    #         file = open(self.fileOpen)
    #         fContent = file.read()
    #         file.close()
    #         if self.textArea.get("1.0", END+"-1c") != fContent:
    #             self.fileOpen += "*"
    #     else:
    #         root.title(" Text Editor | Unsaved Document*")

    def file_new(self):
        root.title(" Text Editor | Unsaved Document")
        if self.textArea.get("1.0", END+"-1c") != "":
            f = open(self.fileOpen)
            fContent = f.read()
            f.close()
            if self.textArea.get("1.0", END+"-1c") != fContent:
                result = messagebox.askyesno("Careful!", "It looks like you have some unsaved work, would you like to save it?")
                if result:
                    self.file_save()
                    self.textArea.delete("1.0", END)
                else:
                    self.textArea.delete("1.0", END)
            else:
                self.textArea.delete("1.0", END)
        else:
            self.textArea.delete("1.0", END)

    def file_save(self):
        if self.fileOpen != "":
            fContent = self.file.read()
            self.file.close()
            if self.textArea.get("1.0", END+"-1c") != fContent:
                f = open(self.file, "w")
                data = self.textArea.get("1.0", END+"-1c")
                f.write(data)
                f.close()

    def file_saveAs(self):
        files =[("Text file", ".txt"),
                ("HTML File", ".html"),
                ("All Files", ".*")]
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=files)
        if file != None:
            data = self.textArea.get("1.0", END+"-1c")
            file.write(data)
            self.file = file
            file.close()
            self.fileOpen = file.name
            root.title(" Text Editor | {}".format(self.fileOpen))

    def file_open(self):
        def open_method(file):
            contents = file.read()
            self.textArea.delete("1.0", END)
            self.textArea.insert("1.0", contents)
            file.close()
            self.fileOpen = file.name
            root.title(" Text Editor | {}".format(self.fileOpen))
        file = filedialog.askopenfile(parent=root, mode="rb", title="Select a .txt file!")
        if file != None:
            if self.textArea.get("1.0", END+"-1c") != "":
                if self.fileOpen != "":
                    f = open(self.fileOpen)
                    fContent = f.read()
                    f.close()
                    print(fContent.rstrip('\n'))
                    print("--")
                    print(self.textArea.get("1.0", END+"-1c"))
                    if self.textArea.get("1.0", END+"-1c") != fContent:
                        result = messagebox.askyesno("Careful!", "It looks like you have some unsaved work, would you like to save it?")
                        if result:
                            self.file_saveAs()
                            open_method(file)
                        else:
                            open_method(file)
                    else:
                        open_method(file)
                else:
                    if self.textArea.get("1.0", END+"-1c") != "":
                        result = messagebox.askyesno("Careful!", "It looks like you have some unsaved work, would you like to save it?")
                        if result:
                            self.file_saveAs()
                            open_method(file)
                        else:
                            open_method(file)
            else:
                open_method(file)

    def editorHelp(self):
        pass

    def editorAbout(self):
        messagebox.showinfo("About Text Editor", "Text Editor \n\nVersion 1.0 \n© HaZDev. All rights reserved.")

def save(event):
    gui.file_save()

    # gui.checkChanged()
root = Tk()
gui = Text_Editor(root)

root.bind_all('<Control-s>', save)
mainloop()
