import pyaudio
import wave
import threading
from src.speech_to_command import speech_to_text


class RealTimeSpeechRecognition:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.keep_recording = True
        self.recognition_thread = None

    def start_recording(self, device_index=0):
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=16000,
                                      input=True,
                                      frames_per_buffer=1024,
                                      input_device_index=device_index)

        self.recognition_thread = threading.Thread(target=self.recognize_from_stream, args=())
        self.recognition_thread.start()

    def recognize_from_stream(self):
        while self.keep_recording:
            data = self.stream.read(1024)
            self.frames.append(data)

            # Continuously pass audio chunks to speech_to_text
            if len(self.frames) > 10:  # Adjust this value as needed
                sound_sample = b''.join(self.frames)
                recognized_text = speech_to_text(sound_sample)
                print(f"Recognized: {recognized_text}")
                self.frames = []

    def stop_recording(self):
        self.keep_recording = False
        self.recognition_thread.join()
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()


# Example usage
recorder = RealTimeSpeechRecognition()
recorder.start_recording()

# Do other stuff...

recorder.stop_recording()