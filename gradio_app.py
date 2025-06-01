from brain_of_the_doctor import encode_image_to_base64, analyze_image_with_query
from voice_of_the_patient import record_audio_simple , transcribe_audio_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

import gradio as gr
import os

system_prompt = """
    You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please
"""

def process(audio_file, image_file):
    speech_to_text_output = transcribe_audio_with_groq(audio_file, stt_model="whisper-large-v3-turbo",GROQ_API_KEY= os.getenv("GROQ_API_KEY"))
    if image_file:
        encoded_image = encode_image_to_base64(image_file)
        analysis_result = analyze_image_with_query(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            query=system_prompt+speech_to_text_output,
            encoded_image=encoded_image
        )
    else:
        analysis_result = "No image provided for analysis."
        
    doctor_response = text_to_speech_with_gtts(analysis_result, output_file="doctor_response.mp3")
    return speech_to_text_output, analysis_result, doctor_response
    pass

iface = gr.Interface(
    fn=process,
    inputs=[
        gr.Audio(sources=['microphone'],type="filepath", ),
        gr.Image(type="filepath", label="Upload Image"),
    ],
    outputs=[
        gr.Textbox(label="Transcription"),
        gr.Textbox(label="Analysis Result"),
        gr.Audio(label="Doctor's Response", autoplay=True),
    ],
    title="Voice of the Doctor - Carelytic",
    
)

iface.launch(debug=True,share=True)