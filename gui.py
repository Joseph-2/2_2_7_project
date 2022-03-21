# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename


def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()


def do_command(command):
  global command_textbox, url_entry
  # If url_entry is blank, use localhost IP address 
  url_val = url_entry.get()
  if (len(url_val) == 0):
    # url_val = "127.0.0.1"
    url_val = "192.168.1.222"
    
  command_textbox.delete(1.0, tk.END)
  command_textbox.insert(tk.END, command + " working....\n")
  command_textbox.update()

  p = subprocess.Popen(command + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

  cmd_results, cmd_errors = p.communicate()
  command_textbox.insert(tk.END, cmd_results)
  command_textbox.insert(tk.END, cmd_errors)

root = tk.Tk()
frame = tk.Frame(root,bg='antique white')
frame.pack(fill='x')

# set up button to run the do_command function
save_btn = tk.Button(frame,
 text="save",
 fg= 'blue',
 bg= 'linen',
 command=mSave)
save_btn.pack(side='right')

ping_btn = tk.Button(frame, 
text="ping", 
fg='blue',
bg='linen',
command=lambda:do_command("ping "))
ping_btn.pack(side='left')

tracert_btn = tk.Button(frame,
text="tracert", 
fg='blue',
bg='linen',
command=lambda:do_command("tracert "))
tracert_btn.pack(side='left')

nslookup_btn = tk.Button(frame,
text="nslookup",
fg='blue',
bg='linen',
command=lambda:do_command("nslookup "))
nslookup_btn.pack(side='left')

# creates the frame with label for the text box
frame_URL = tk.Frame(root,bg="antique white") # change frame color
frame_URL.pack(side='left',fill='both')

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    font=("Arial", 14),
    fg="blue",
    bg="white")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root) # change frame color
frame.pack(fill='both')

command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack(fill='both')

root.mainloop()