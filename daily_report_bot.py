import pyautogui
import time
from datetime import datetime
import re
import os
import pyperclip
from openpyxl import Workbook


pyautogui.FAILSAFE = True
pyautogui.PAUSE - 0.5 # waits for 0.5s between each operation

website = "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE"

#wait for loading
time.sleep(1)

print('Step 1 - Open a Chrome browser')
time.sleep(2)

pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)


print('Step 2 - Open the Finance website')
time.sleep(2)

pyautogui.hotkey("ctrl", "l") # focus on the address bar

# writes the text letter by letter - so wont be identified as Bot
pyautogui.typewrite(website, interval=0.05)
pyautogui.press('enter')
print("Loading page...")
time.sleep(8)


print('Step 3 - Copy the data of the webiste')
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)


# Close Chrome
print('Close Chrome Window')
pyautogui.hotkey("ctrl", "w")
time.sleep(1)


print('Step 4 - Open a notepad, Paste the copied data')
time.sleep(1)
pyautogui.hotkey('win','r')
time.sleep(1)
pyautogui.write('notepad', interval=0.5)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'n') #open a new tab in Notepad

time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

print('Step 5 - Paste the copied data')
page_text = pyperclip.paste()

print('Step 6: Search for NIFTY 50')
pyautogui.hotkey("ctrl", "f")
time.sleep(1)
pyautogui.write("NIFTY 50", interval=0.05)
time.sleep(1)
pyautogui.press("enter")


print('Step 7: Extract and Determine Change value')
match = re.search(
    r'NIFTY\s*50.*?([\d,]+\.\d+)',
    page_text,
    re.DOTALL
)

if match:
    nifty_value = match.group(1)
    change_match = re.search(
        r'([+-]?\d+\.\d+%)\s*\(([+-]?\d+\.\d+)\)',
        page_text,
        re.DOTALL
    )

    if change_match:

        percentage = change_match.group(1)
        points = change_match.group(2)

        if points.startswith("-"):
            comment = (
                f"Market is DOWN by {abs(float(points)):.2f} points "
                f"({percentage}) compared to the previous close."
            )
        else:
            comment = (
                f"Market is UP by {float(points):.2f} points "
                f"({percentage}) compared to the previous close."
            )
    else:
        comment = "Daily market movement unavailable."
else:
    nifty_value = "Not Found"
    comment = "Daily market snapshot not available"

print("NIFTY 50:", nifty_value)
print("Comment:", comment)

print('Step 8: Close Notepad')
pyautogui.hotkey("alt", "f4")
time.sleep(1)


print('If prompted to save changes, choose - Dont Save')
pyautogui.press("right")   # Highlights "Don't Save" on many Windows versions
pyautogui.press("enter")

print('Step 9 - Create the Excel file')
wb = Workbook()
ws = wb.active
ws.append([
    "Date & Time",
    "NIFTY 50",
    "Comment"
])

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ws.append([
    current_time,
    nifty_value,
    comment
])

# Get the current project directory
project_dir = os.getcwd()

# Create an output folder
output_dir = os.path.join(project_dir, "output")

os.makedirs(output_dir, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")

excel_filename = f"daily_report_{today}.xlsx"

excel_path = os.path.join(output_dir, excel_filename)

wb.save(excel_path)

print(f"Excel saved at: {excel_path}")


print('Step 10 - Open the Excel file')
os.startfile(excel_path)


print('Step 11 - Save the Screenshot in the Same Folder and close the file')

screenshot_filename = f"report_snapshot_{today}.png"
screenshot_path = os.path.join(output_dir, screenshot_filename)
time.sleep(2)
pyautogui.screenshot(screenshot_path)
print(f"Screenshot saved at: {screenshot_path}")

# Close Excel file
pyautogui.hotkey("alt", "f4")
time.sleep(1)