import tkinter as tk
from defines import get_creds
from request_user_id import get_user_id

def get_new_creds():
    """ Reads input creds, validates, and saves to dictionary in defines
	"""
    global creds

    inputUser = inputUsername.get(1.0, "end-1c")
    inputAccessToken = inputAT.get(1.0, "end-1c")
    #get user ID
    userID = get_user_id(inputAccessToken, inputUser)

    #get dictionary of user credentials
    creds = get_creds()
    #create dictionary containing new user credentials using same key
    newCreds = {'ig_username':inputUser, 'access_token':inputAccessToken, 'instagram_account_id':userID}

    # update new credentials into the dictionary
    creds.update(newCreds)
    print(creds)

    # close the Tkinter frame if instagram_account_id has been successfully updated and verified
    if creds.get('instagram_account_id', '') != '':
        frame.destroy()
    #return creds

def input_creds_GUI():
    """ Creates GUI for user to input account details
    
	Returns:
		creds: the account credentials entered

	"""

    global frame
    global inputUsername
    global inputAT

    frame = tk.Tk() 
    frame.title("Input User Details") 
    frame.geometry('700x200') 

    # label for text box
    lbl = tk.Label(frame, text="Input username: ")
    lbl.grid(column=0, row=0)

    # TextBox Creation 
    inputUsername = tk.Text(frame,  height = 1,  width = 60) 
    inputUsername.grid(column=1, row=0) 

    # label for text box
    lblAT = tk.Label(frame, text="Input access token: ")
    lblAT.grid(column=0, row=1)

    # TextBox Creation 
    inputAT = tk.Text(frame,  height = 1,  width = 60) 
    inputAT.grid(column=1, row=1)

    #terms = tk.Label(text="By clicking Continue you agree to the terms and conditions available in the README file.")
    #terms.grid(column=0, rowspan=2)
    terms_text = "By clicking Continue you agree to the terms and conditions available in the README file."
    terms = tk.Label(frame, text=terms_text, wraplength=400)  # Adjust wraplength as needed
    terms.grid(column=0, row=2, columnspan=2, pady=10)
  
    # button Creation 
    printButton = tk.Button(frame, text = "Continue",   command = get_new_creds)
    printButton.grid(column=0, row=3, columnspan=2)

    # loop frame
    frame.mainloop()
    return creds