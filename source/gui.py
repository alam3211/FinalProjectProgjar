import Tkinter as tkinter


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    window.quit()

window = tkinter.Tk()

window.title("Progjar Chat Apps")

messages_frame = tkinter.Frame(window)
messages_frame.pack()

message_box_frame = tkinter.Frame(window)
message_box_frame.pack(side = tkinter.BOTTOM)

my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(window)  # To navigate through past messages.

# Following will contain the messages.
msg_list = tkinter.Listbox(window, height=30, width=90, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
msg_list.pack()
entry_field = tkinter.Entry(message_box_frame, textvariable=my_msg)
entry_field.bind("<Return>")
entry_field.pack(side=tkinter.LEFT)
send_button = tkinter.Button(message_box_frame, text="Send")
send_button.pack(side=tkinter.LEFT)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()