import google.generativeai as genai
import os
import tkinter as tk
frame = tk.Tk() 
frame.title("Dungeon Game") 
frame.geometry('400x200') 
a = """
I am at the entrance of a dungeon, known in leengds as Un Dak Oh, and home to majestic creatures and untold treasures. I can take various actions in this fantasy world. The character is Xana, a mischecious fox spirit, and I am at the entrance of the dungeon. I have a spellbook, some potions, and other magical doohickies, but the entire story and map is up to you!
"""
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat()
def printInput(): 
    inp = inputtxt.get(1.0, "end-1c")
    response = chat.send_message(inp)
    lbl.config(text = response.text) 

# while True:
#     f = open("instructions.txt", "r").read()
#     response = chat.send_message(f)
#     print(response.text)
#     time.sleep(8)

inputtxt = tk.Text(frame,
                   height = 5, 
                   width = 20) 
inputtxt.insert(tk.INSERT, a)
  
inputtxt.pack() 
  
# Button Creation 
printButton = tk.Button(frame, 
                        text = "Print",  
                        command = printInput) 
printButton.pack() 
  
# Label Creation 
lbl = tk.Label(frame, text = "Press Print to get started!") 
lbl.pack() 
frame.mainloop()
