import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TextToSpeech:
    """
    A class to convert text to speech using ElevenLabs API
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the TextToSpeech class
        
        Args:
            api_key (str): ElevenLabs API key. If not provided, will try to get from environment variable
        """
        self.api_key = api_key or os.getenv('ELEVENLABS_API_KEY')
        if not self.api_key:
            raise ValueError("ElevenLabs API key not provided. Set ELEVENLABS_API_KEY environment variable.")
        
        self.base_url = "https://api.elevenlabs.io/v1"
        self.headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
    
    def get_voices(self):
        """
        Get available voices from ElevenLabs
        
        Returns:
            list: List of available voices with their details
        """
        try:
            url = f"{self.base_url}/voices"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json().get('voices', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching voices: {e}")
            return []
    
    def text_to_speech(self, text, voice_id="21m00Tcm4TlvDq8ikWAM", output_file="output.mp3"):
        """
        Convert text to speech using ElevenLabs API
        
        Args:
            text (str): The text to convert to speech
            voice_id (str): The voice ID to use (default: Bella)
            output_file (str): Path where the audio file will be saved
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not text or not text.strip():
            print("Error: Text cannot be empty")
            return False
        
        try:
            url = f"{self.base_url}/text-to-speech/{voice_id}"
            
            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75
                }
            }
            
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            
            # Save the audio file
            with open(output_file, 'wb') as f:
                f.write(response.content)
            
            print(f"Speech generated successfully and saved to {output_file}")
            return True
        
        except requests.exceptions.RequestException as e:
            print(f"Error generating speech: {e}")
            return False
        except IOError as e:
            print(f"Error saving audio file: {e}")
            return False
    
    def text_to_speech_stream(self, text, voice_id="21m00Tcm4TlvDq8ikWAM"):
        """
        Convert text to speech and return audio data as bytes
        
        Args:
            text (str): The text to convert to speech
            voice_id (str): The voice ID to use
        
        Returns:
            bytes: Audio data if successful, None otherwise
        """
        if not text or not text.strip():
            print("Error: Text cannot be empty")
            return None
        
        try:
            url = f"{self.base_url}/text-to-speech/{voice_id}"
            
            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75
                }
            }
            
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            
            return response.content
        
        except requests.exceptions.RequestException as e:
            print(f"Error generating speech: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize the TextToSpeech class
    tts = TextToSpeech()
    
    # Example: Convert text to speech
    text = "Hello, this is a test message from ElevenLabs API."
    tts.text_to_speech(text, output_file="test_output.mp3")
    
    # Example: Get available voices
    voices = tts.get_voices()
    print(f"Available voices: {len(voices)}")
    for voice in voices[:5]:
        print(f"- {voice['name']} (ID: {voice['voice_id']})")
