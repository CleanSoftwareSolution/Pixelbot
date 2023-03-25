import pyautogui
import time
import tkinter as tk
from threading import Thread

def find_target_pixel(target_pixel, tolerance=5):
    screenshot = pyautogui.screenshot()
    width, height = screenshot.size
    for x in range(width):
        for y in range(height):
            r, g, b = screenshot.getpixel((x, y))
            if (
                abs(r - target_pixel[0]) <= tolerance
                and abs(g - target_pixel[1]) <= tolerance
                and abs(b - target_pixel[2]) <= tolerance
            ):
                return x, y
    return None

def run_bot():
    global running
    target_pixel_color = (255, 0, 0)  # Replace with the color of the target pixel

    while running:
        target_pixel = find_target_pixel(target_pixel_color)

        if target_pixel:
            x, y = target_pixel
            # Perform desired action, such as clicking on the pixel
            pyautogui.click(x, y)
            output_text.insert(tk.END, f"Clicked at {x}, {y}\n")
            output_text.see(tk.END)
            time.sleep(1)  # Adjust the sleep time as needed

def start_bot():
    global running
    if not running:
        running = True
        bot_thread = Thread(target=run_bot)
        bot_thread.start()

def stop_bot():
    global running
    if running:
        running = False

root = tk.Tk()
root.title("Pixel Bot")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

output_text = tk.Text(frame, wrap=tk.WORD, width=50, height=10)
output_text.pack(padx=5, pady=5)

start_button = tk.Button(frame, text="Start Bot", command=start_bot)
start_button.pack(fill=tk.X, padx=5, pady=(10, 5))

stop_button = tk.Button(frame, text="Stop Bot", command=stop_bot)
stop_button.pack(fill=tk.X, padx=5, pady=(0, 5))

root.mainloop()
