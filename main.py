import win32clipboard 
import time #required to ask whether the content is changing or has changed & disable the script whenever you want.

# Checking if the new data is identical to the data that has been called before.
old = ""

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if old != data:
        with open("cclip_history.txt", 'a+') as f:
            f.write(data + "\n")
        old = data