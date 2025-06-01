import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio_simple(file_path,timeout=20,phrase_time_limit=None):
    recognozer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting noise level...")
            recognozer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Recording audio...")
            audio_data = recognozer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Audio recorded successfully.")
        
            wave_data = audio_data.get_wav_data()
            audio_segement = AudioSegment.from_wav(BytesIO(wave_data))
            audio_segement.export(file_path, format="mp3",bitrate="128k")
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

audio_file_path = "patient_voice.mp3"
record_audio_simple(file_path=audio_file_path)

###
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

stt_model="whisper-large-v3-turbo"
def transcribe_audio_with_groq(audio_file_path,stt_model,GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    stt_model = stt_model

    audio_file=open(audio_file_path, "rb")

    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model=stt_model,
        language="en",
        response_format="text"
    )


    return(transcription)

