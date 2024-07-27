import whisper
from Levenshtein import ratio
import re

model = whisper.load_model("base.en")
whisper.DecodingOptions(language="en")


def speech_to_text(sound_sample):
    result = model.transcribe(sound_sample)
    recognized = re.sub(r'[^\w]', ' ', result['text']).lower()

    return recognized


# target = 'double fault'
#
# dist = ratio(recognized, target)
# print(f'Recognized text: {recognized}')
# print(f'The Levenshtein distance is {dist}.')

if __name__ == '__main__':
    speech_to_text("/home/paprycy/PycharmProjects/TennisAnalyzer/resources/recordings_samples/double_fault3.mp3")
