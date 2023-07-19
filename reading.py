from gtts import gTTS
import os
import time

# อ่านข้อความจากไฟล์ word.txt
with open('word.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# เลือกภาษาให้กับ TTS
language = 'th'  # ภาษาไทย

# สร้างเสียงจากข้อความ
start_time = time.time()  # เวลาเริ่มต้นการสร้างเสียง
tts = gTTS(text=text, lang=language, slow=False)
end_time = time.time()  # เวลาสิ้นสุดการสร้างเสียง

# คำนวณและแสดงเวลาที่ใช้ในการสร้างเสียง
time_taken = end_time - start_time
print(f"เวลาที่ใช้ในการสร้างเสียง: {time_taken:.3f} วินาที")

# บันทึกไฟล์เสียงเป็น MP3
tts.save("output.mp3")

# เล่นไฟล์เสียงที่สร้างขึ้น
os.system("start output.mp3")
