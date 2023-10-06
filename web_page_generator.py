import tkinter as tk
from tkinter import *
import webbrowser
from tkinter import messagebox

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        '''self.master = master
        self.master.geometry("900x200")
        self.master.minsize(900,200)
        self.master.maxsize(900,200)'''

        self.master.title("Web Page Generator")

        self.btn = tk.Button(self.master, text = "Default HTML Page", width = 30, height = 2, command=self.defaultHTML)
        self.btn.grid(row=20, column=15)

        self.subbtn = tk.Button(self.master, text = "Submit Custom Text", width = 30, height = 2)
        self.subbtn.grid(row=20, column=20)
        
        self.entry = tk.Entry(self.master, text = '')
        self.entry.grid(row=15,column=1,rowspan=10,columnspan=1)

        self.label = tk.Label(self.master, text = 'Enter custom text or click the Default HTML page button')
        self.label.grid(row=10, column=0, padx=(10,10), pady=(10,10))
        
       

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
