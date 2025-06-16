from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json
import requests 

# Colors
cor0 = "#FFFFFF"  # white
cor1 = "#333333"  # black
cor2 = "#EB5D51"  # red

# Window setup
window = Tk()
window.geometry('300x320')
window.title('Currency Converter')
window.configure(bg=cor0)
window.resizable(False, False)

# Top and Main Frames
top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

# --- Function to Convert Currency ---
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get().strip()
    currency_2 = combo2.get().strip()
    amount = value.get()

    if not currency_1 or not currency_2 or not amount:
        result['text'] = "Fill all fields"
        return

    try:
        float(amount)
    except ValueError:
        result['text'] = "Enter valid number"
        return

    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    headers = {
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com",
        "x-rapidapi-key": "YOUR_API_KEY"  # Replace with your real API key
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = json.loads(response.text)
        converted_amount = data["result"]["convertedAmount"]

        symbol = {
            "USD": "$", "INR": "₹", "EUR": "€", "BRL": "R$", "CAD": "CA$"
        }.get(currency_2.upper(), "")

        formatted = symbol + "{:,.2f}".format(converted_amount)
        result["text"] = formatted
    else:
        result["text"] = "API Error"

# --- Load Icon ---
icon2 = Image.open("icon2.png")
icon2 = icon2.resize((40, 40))
icon = ImageTk.PhotoImage(icon2)

app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter",
                 height=50, padx=13, pady=10, anchor=CENTER,
                 font=("Arial", 16, "bold"), bg=cor2, fg=cor0)
app_name.place(x=0, y=0)

# --- Main Frame Widgets ---
result = Label(main, text="", width=16, height=2, pady=7, relief="solid",
               anchor=CENTER, font=("Ivy", 15, "bold"), bg=cor0, fg=cor1)
result.place(x=50, y=10)

currency = ["INR", "CAD", "USD", "EUR"]

# From currency
from_label = Label(main, text="From", width=8, relief="flat", anchor=NW,
                   font=("Ivy", 10, "bold"), bg=cor0, fg=cor1)
from_label.place(x=40, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy", 12, "bold"))
combo1['values'] = currency
combo1.place(x=50, y=115)

# To currency
to_label = Label(main, text="To", width=8, relief="flat", anchor=NW,
                 font=("Ivy", 10, "bold"), bg=cor0, fg=cor1)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy", 12, "bold"))
combo2['values'] = currency
combo2.place(x=160, y=115)

# Amount input
value = Entry(main, width=22, justify=CENTER,
              font=("Ivy", 12, "bold"), relief=SOLID)
value.place(x=50, y=150)

# Convert button
button = Button(main, text="Convert", width=19, height=1,
                bg=cor2, fg=cor0, font=("Ivy", 12, "bold"), command=convert)
button.place(x=50, y=210)

# Start application
window.mainloop()
