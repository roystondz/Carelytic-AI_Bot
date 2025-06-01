import os
from gtts import gTTS
from dotenv import load_dotenv
import subprocess
import platform



def text_to_speech_with_gtts(text, output_file):
    language = 'en'
    audioobj=gTTS(text=text, lang=language, slow=False)
    audioobj.save(output_file)
    
    try:
        if platform.system() == "Windows":
            subprocess.run(["powershell", '-c',f'(New-object Media.Soundplayer "{output_filepath}").PlaySync();'])
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["afplay", output_file])
        else:  # Linux and other systems
            subprocess.run(["xdg-open", output_file])
    except Exception as e:
        print(f"Error opening audio file: {e}")

input_text = "Hello, this is a test of the text-to-speech conversion ,autoplay enabled"
output_filepath = "output.mp3"
text_to_speech_with_gtts(input_text, output_filepath)

# import elevenlabs
# from elevenlabs.client import ElevenLabs
# from elevenlabs import save

# load_dotenv()
# elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
# if not elevenlabs_api_key:
#     raise ValueError("ELEVENLABS_API_KEY environment variable is not set.")

# def text_to_speech_with_eleven_labs(input_text,output_filepath_elevenlabs="elevenlabs_output.mp3"):
#     client = ElevenLabs(api_key=elevenlabs_api_key)
#     audio = client.generate(
#         text=input_text,
#         voice="Elliot",
#         model="eleven_multilingual_v1",
#         output_format="mp3_22050_32"
#     )
#     elevenlabs.save(audio,output_filepath_elevenlabs)
#     pass

# text_to_speech_with_eleven_labs(input_text)

# elevenlabs = ElevenLabs(
#   api_key=os.getenv("ELEVENLABS_API_KEY"),
# )
# def text_to_speech_with_eleven_labs(input_text,output_filepath_elevenlabs="elevenlabs_output.mp3"):
#     audio = elevenlabs.text_to_speech.convert(
#         text="The first move is what sets everything in motion.",
#         voice_id="JBFqnCBsd6RMkjVDRZzb",
#         model_id="eleven_multilingual_v2",
#         output_format="mp3_44100_128",
#     )
#     save(audio, output_filepath_elevenlabs)
    
# text_to_speech_with_eleven_labs(input_text)


