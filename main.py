import tkinter as tk


window = tk.Tk()
window.title("AutoWipeNote")
window.geometry("700x600")

class DelayedDeleteTextWidget(tk.Text):
    def __init__(self, master=None, delete_delay=3000, **kwargs):
        tk.Text.__init__(self, master, **kwargs)
        self.delete_delay = delete_delay
        self.typing_timer_id = None
        self.bind("<Key>", self.reset_typing_timer)

    def reset_typing_timer(self, event=None):
        # Reset the typing timer when there is user typing
        if self.typing_timer_id:
            self.after_cancel(self.typing_timer_id)
        self.typing_timer_id = self.after(self.delete_delay, self.delete_text)

    def delete_text(self):
        # Delete the text in the Text widget when the typing delay is reached
        self.delete(1.0, tk.END)

heading = tk.Label(text='Welcome to AutoWipeNote', font=('Roboto', 25, 'bold'))
heading.grid(row=0,column=0)



inputs = DelayedDeleteTextWidget(window,delete_delay=3000)
inputs.grid(row=1,column=0)





window.mainloop()