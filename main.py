"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
from google.oauth2 import service_account


def generate():
    content_name = '01_tarea_1.ssml'
    file_name = f'CCSE_2025/{content_name}.xml'
    ssml = ''
    with open(file_name, "r") as out:
        # Write the response to the output file.
        ssml = out.read()

    print(f'Got a ssml:{ssml}')

    # Load the service account key file
    credentials = service_account.Credentials.from_service_account_file("config/volmyr-test-c1ca48dc8ac7.json")

    # Instantiates a client with the credentials
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

    # Build the voice request, select the language code and the ssml voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-ES", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    audio_file_name = f'CCSE_2025/audio/{content_name}.mp3'
    with open(audio_file_name, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file {audio_file_name}')


if __name__ == '__main__':
    generate()
