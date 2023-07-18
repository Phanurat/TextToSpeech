import speech_recognition as sr
from gtts import gTTS
import os

def speech_to_text():
    recog = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    with mic as source:
        miRe = 3
        print("กำลังบันทึกเสียง", miRe, "วินาที...")
        audio = recog.record(source, duration=miRe)

        try:
            text = '"' + recog.recognize_google(audio, language='th') + '"'
            print("ข้อความที่ได้:", text)
            return text
        except sr.UnknownValueError:
            print("ไม่สามารถรับรู้เสียง")
            return ""
        except sr.RequestError as e:
            print("การร้องขอแปลงเสียงเป็นข้อความล้มเหลว:", str(e))
            return ""

def text_to_speech(text):
    language = 'th'
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

def main():
    text = speech_to_text()
    if text:
        text_to_speech(text)

if __name__ == "__main__":
    main()
