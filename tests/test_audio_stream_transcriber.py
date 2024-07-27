import unittest
from unittest.mock import Mock, patch
import pyaudio

class TestAudioStreamTranscriber(unittest.TestCase):
    def setUp(self):
        self.transcriber = Mock()
        self.transcriber.stream = Mock()
        self.transcriber.audio = Mock()

    @patch('pyaudio.PyAudio')
    def test_stop_recording(self, mock_pyaudio):
        self.transcriber.keep_recording = True
        self.transcriber.recognition_thread = Mock()

        self.transcriber.stop_recording()

        self.assertFalse(self.transcriber.keep_recording)
        self.transcriber.recognition_thread.join.assert_called_once()
        self.transcriber.stream.stop_stream.assert_called_once()
        self.transcriber.stream.close.assert_called_once()
        self.transcriber.audio.terminate.assert_called_once()

    def test_stop_recording_when_not_recording(self):
        self.transcriber.keep_recording = False
        self.transcriber.recognition_thread = None

        self.transcriber.stop_recording()

        self.transcriber.stream.stop_stream.assert_not_called()
        self.transcriber.stream.close.assert_not_called()
        self.transcriber.audio.terminate.assert_not_called()
