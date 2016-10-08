#!/usr/bin/env python
"""Mailsack - dummy smtp server UI."""
import tkinter as tk

class Mailsack_UI(tk.Frame):

  def __init__(self, master=None):
    super().__init__(master)
    master.grid()
    self.show_main_interface()

  def show_main_interface(self):
    self.mail_list = tk.Listbox()
    self.mail_list.bind('<<ListboxSelect>>', self.onselect)
    self.mail_list['bd'] = 0
    self.mail_list['bg'] = '#DADADA'
    self.mail_list['highlightthickness'] = 0
    self.mail_list['height'] = 20
    self.mail_list['width'] = 30
    self.mail_list.grid(row=0, column=0)
    #self.scrollbar = tk.Scrollbar(self.mail_list, orient="vertical")
    #self.scrollbar.grid(row=0, column=1)
    #self.mail_list['yscrollcommand'] = self.scrollbar.set
    #self.scrollbar.config(command=self.mail_list.yview)
    for i in self.fetch_mails():
      self.mail_list.insert('end', i)

    self.mail_body = tk.Text()
    self.mail_body['bd'] = 0
    self.mail_body['highlightthickness'] = 0
    self.mail_body['padx'] = 20
    self.mail_body['pady'] = 20
    self.mail_body.grid(row=0, column=1)
    self.mail_body.insert('end',"\n\n\n\n\n\n\n\n\n\n\n\n \t\t\t\tClick on a mail")


  def fetch_mails(self):
    mails = []
    for i in range(100):
      mails.append("TEST " + str(i))
    return mails

  def onselect(self,evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    self.mail_body.delete("1.0", tk.END)
    self.mail_body.insert('end', value)


root = tk.Tk()
root['bg'] = '#DADADA'
root['padx'] = 10
root['padx'] = 10
app = Mailsack_UI(root)
root.mainloop()
