import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        
    def customHTML(self):
        text = self.entry.get()
        htmlText = text
        htmlFile = open("custom.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("custom.html")
        

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.label = tk.Label(self.master, text="Enter custom text or click Default HMTL page button")
        self.label.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky=W)
        self.entry = tk.Entry(self.master, text="", width=100)
        self.entry.grid(padx=(10,10), pady=(10,10))
        self.btn = tk.Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0,padx=(400,0), pady=(10,10))
        self.subbtn = tk.Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.subbtn.grid(row=2, column=1, padx=(10,10), pady=(10,10))
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
