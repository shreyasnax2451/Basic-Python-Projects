from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
import os

language = 'en'

# Initialize the gTTS object with the text and language
# for name in ['x','y','z']:
name = 'x'
text = f'Shoutout to {name}'
tts = gTTS(text=text, lang=language, slow=False)

speech_bytes = BytesIO()
tts.write_to_fp(speech_bytes)
speech_bytes.seek(0)

# Load audio data into PyDub
audio = AudioSegment.from_file(speech_bytes, format="mp3")

# Play the audio
play(audio)