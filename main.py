import tkinter
from tkinter import Text
import requests
import json
from tkinter import ttk
import sv_ttk

# ~~~~~~~ Support Functionss ~~~~~~~ # 

def send_request():
    method_dict = {
        "Get": requests.get,
        "Post": requests.post,
        "Put": requests.put,
        "Delete": requests.delete,
    }
    http_verb = request_verb_combo.get()
    client_func = method_dict[http_verb]
    
    # Make request 
    uri = ent_url.get()
    response = client_func(uri)

    try:
        response_body_text = json.dumps(response.json(), indent=1)
    except Exception:
        response_body_text = response.text

    # Update UI
    response_status_code.config(text=f"Status Code: {response.status_code}")
    response_body.config(text=response_body_text)
    elapsed.config(text=f"Time Elapsed: {response.elapsed} Seconds")

# ~~~~~~~ Window Setup ~~~~~~~ # 
window = tkinter.Tk()
window.title("Mailman")
frm_body = ttk.Frame(master=window, padding=10)
frm_body.pack(fill='both', expand=True)
sv_ttk.set_theme("dark")

# ~~~~~~~ Request Information ~~~~~~~ # 

# Create frame for request form
frm_request_info = ttk.LabelFrame(
    master=frm_body, 
    padding=10, 
    relief='raised', 
    borderwidth=1,
    text="Request"
)
frm_request_info.pack(fill='both',side='top', expand=True)

# Combobox for request type
request_verb_combo = ttk.Combobox(
    master=frm_request_info,
    values=[
        "Get",
        "Post",
        "Put",
        "Delete",
    ],
    width=5
)
request_verb_combo.current(0)
request_verb_combo.pack(side='left')

# Entry for URL Info
ent_url = ttk.Entry(master=frm_request_info, width=100)
ent_url.pack(side='left')

# Button for sending request
btn_send = ttk.Button(
    master=frm_request_info, 
    text="Send",
    command=send_request
)
btn_send.pack(side='left')

# ~~~~~~~ Response Information ~~~~~~~ # 
frm_response_info = ttk.LabelFrame(
    master=frm_body, 
    padding=10, 
    relief='raised', 
    borderwidth=1,
    text="Response"
    )
frm_response_info.pack(fill='both',side='top', expand=True)

# Meta Data Frame
frm_response_meta_data = ttk.LabelFrame(
    master=frm_response_info, 
    padding=10, 
    relief='raised', 
    borderwidth=1,
    text ="Meta Data"
)
frm_response_meta_data.pack(fill='both',side='left')

# Status Code Label
response_status_code = ttk.Label(frm_response_meta_data, text="", )
response_status_code.grid(row=0, column=0, sticky='w')

# Time Elapsed Label
elapsed = ttk.Label(frm_response_meta_data, text="")
elapsed.grid(row=1, column=0, sticky='w')

# Padding to separate frames
frm_padding = ttk.Frame(
    master=frm_response_info, 
    width=10, 
)
frm_padding.pack(fill='both',side='left')

# Response Body Frame
frm_response_body_data = ttk.LabelFrame(
    master=frm_response_info, 
    padding=10, 
    relief='raised', 
    borderwidth=1, 
    text="Response Body",
)
frm_response_body_data.pack(fill='both',side='right', expand=True)

response_body = ttk.Label(frm_response_body_data, text="")
response_body.grid(row=0, column=0, sticky='w')


# Start App
window.mainloop()