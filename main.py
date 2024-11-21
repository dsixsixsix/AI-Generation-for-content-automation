# Import the required module for text to speech conversion
from gtts import gTTS

# This module is imported so that we can play the converted audio
import os

# اسم الملف النصي الذي يحتوي على النص
file_name = "text_input.txt"

# فتح الملف وقراءة محتوياته
# فتح الملف وقراءة محتوياته
with open(file_name, "r", encoding="utf-8") as file:
    mytext = file.read().strip()  # استخدم strip() لإزالة المسافات البيضاء الزائدة

# تحقق من أن النص ليس فارغًا
if not mytext:
    raise ValueError("The text file is empty or only contains whitespace.")

print("Text read from file ")  # التأكد من استقبال النص بنجاح من الملف
# Language in which you want to convert
language = input("Enter (en) for English, or (ru) for Russian: ")

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")
