import webbrowser
import speech_recognition as sr
import win32com.client
import datetime
import os
import tkinter as tk

def say(txt):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(txt)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            if status_label.winfo_exists():
                status_label.config(text="Recognizing...", fg="blue")
                root.update()

            result = r.recognize_google(audio, language='en-IN', show_all=True)
            if isinstance(result, dict):
                query = result['alternative'][0]['transcript']
                if transcription_label.winfo_exists():
                    transcription_label.config(text=f"User said: {query}")
                    root.update()
                return query
            else:
                if transcription_label.winfo_exists():
                    transcription_label.config(text=f"User said: {result}")
                    root.update()
                return result
        except Exception:
            say("I'm sorry, I didn't catch that. Try again!")
            if transcription_label.winfo_exists():
                transcription_label.config(text="Error: Unable to recognize.")
                root.update()
            return None

def process_command():
    query = take_command()
    if query:
        query = query.lower()
        if transcription_label.winfo_exists():
            transcription_label.config(text=query)

        sites = [
            ["google", "https://www.google.com"],
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["instagram", "https://www.instagram.com"],
            ["facebook", "https://www.facebook.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["chat gpt", "https://www.chatgpt.com"],
            ["whatsapp", "https://web.whatsapp.com"]
        ]

        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                return

        if "open music" in query:
            say("Opening music")
            path = "C:/Users/Talha/Downloads/Pehle Bhi Main - Animal 128 Kbps.mp3"
            os.startfile(path)

        elif "stop" in query:
            say("Jarvis is going to shutdown.")
            if transcription_label.winfo_exists():
                transcription_label.config(text="Jarvis is shutting down...")
            root.quit()

        elif "shutdown" in query:
            say("System will shut down.")
            os.system("shutdown /s /t 1")

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {current_time}")
            if transcription_label.winfo_exists():
                transcription_label.config(text=f"Current time: {current_time}")

    if status_label.winfo_exists():
        status_label.config(text="Listening...", fg="white")

def start_jarvis():
    if status_label.winfo_exists():
        status_label.config(text="Listening...", fg="green")  
    continuous_listen()

def continuous_listen():
    process_command()
    root.after(1800, continuous_listen) 

root = tk.Tk()
root.title("Jarvis AI Voice Assistant")
root.geometry("500x400")
root.configure(bg="#333333")
root.iconbitmap("D:/Github pushed/Rhombix-Remote-Intern-tasks/22.ico")

status_label = tk.Label(root, text="Click 'Start' to begin", font=("Helvetica", 14), bg="#333333", fg="white")
status_label.pack(pady=10)

transcription_label = tk.Label(root, text="", font=("Helvetica", 12), fg="lightgrey", bg="#333333", wraplength=400, justify="left")
transcription_label.pack(pady=10)

start_button = tk.Button(root, text="Start", command=start_jarvis, font=("Helvetica", 12), width=15, bg="#4CAF50", fg="white")
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=root.quit, font=("Helvetica", 12), width=15, bg="#f44336", fg="white")
stop_button.pack(pady=10)

credits_label = tk.Label(root, text="Developed by xtHive, a project of Talhawkk", font=("Helvetica", 10), fg="lightgrey", bg="#333333")
credits_label.pack(side="bottom", pady=20)

root.mainloop()
