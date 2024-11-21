import os
from gtts import gTTS
import tkinter as tk
from tkinter import filedialog, messagebox


def select_file():
    # Open a file dialog to select a text file
    # Открыть диалоговое окно для выбора текстового файла
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        # Read the contents of the file
        # Прочитать содержимое файла
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().strip()
        # Check if the text is empty
        # Проверить, пуст ли текст
        if not text:
            messagebox.showerror(
                "Error", "The text file is empty or only contains whitespace."
            )
            # Показать сообщение об ошибке, если файл пуст
            return
        # Get the selected language
        # Получить выбранный язык
        language = language_var.get()
        # Validate the language input
        # Проверить правильность ввода языка
        if language not in ["en", "ru"]:
            messagebox.showerror(
                "Error", "Invalid language code. Please select a valid language."
            )
            # Показать сообщение об ошибке, если код языка неверен
            return
        try:
            # Convert text to speech
            # Преобразовать текст в речь
            tts = gTTS(text=text, lang=language, slow=False)
            # Save the audio file
            # Сохранить аудиофайл
            tts.save("output.mp3")
            # Play the audio file
            # Воспроизвести аудиофайл
            os.system(
                "start output.mp3"
            )  # Use 'open' for macOS or 'xdg-open' for Linux
            # Используйте 'open' для macOS или 'xdg-open' для Linux
            messagebox.showinfo(
                "Success", "Audio file created and played successfully."
            )
            # Показать сообщение об успешном создании и воспроизведении аудиофайла
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            # Показать сообщение об ошибке, если что-то пошло не так


# Create a simple GUI
# Создать простой графический интерфейс
root = tk.Tk()
root.title("Text to Speech Converter")

# Variable to store the selected language
# Переменная для хранения выбранного языка
language_var = tk.StringVar(value="en")

# Create radio buttons for language selection
# Создать переключатели для выбора языка
tk.Label(root, text="Select Language:").pack()
tk.Radiobutton(root, text="English", variable=language_var, value="en").pack()
tk.Radiobutton(root, text="Russian", variable=language_var, value="ru").pack()

# Create a button to select the text file
# Создать кнопку для выбора текстового файла
tk.Button(root, text="Select Text File", command=select_file).pack()

# Run the GUI event loop
# Запустить цикл обработки событий графического интерфейса
root.mainloop()
