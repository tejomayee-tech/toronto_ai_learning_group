import ttkbootstrap as ttk


window = ttk.Window(themename="minty")
window.title("MyApp")
window.geometry("600x400")

WelcomeText = ttk.Label(window, text="Welcome to MyApp", font=("Arial", 15,"bold"))
# WelcomeText.pack() #display
WelcomeText.grid(row=0,column=0, padx=10, pady=10)


button = ttk.Button(window,text="Submit")
button.grid(row=1,column=0, padx=10, pady=10)

testText = ttk.Label(window, text="MyApp")
# WelcomeText.pack() #display
testText.grid(row=2,column=1, padx=10, pady=10)

window.mainloop()
