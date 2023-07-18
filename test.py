from gtts import gTTS
import os

# ข้อความที่ต้องการแปลงเป็นเสียง
text = "ไอ้ ควายเอ่ย เต็ม คาราเบล"

# เลือกภาษาให้กับ TTS
language = 'th'  # ภาษาไทย

# สร้างเสียงจากข้อความ
tts = gTTS(text=text, lang=language, slow=False)

# บันทึกไฟล์เสียงเป็น MP3
tts.save("output.mp3")

# เล่นไฟล์เสียงที่สร้างขึ้น
os.system("start output.mp3")
