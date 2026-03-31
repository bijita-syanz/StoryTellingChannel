from text_to_speech import TextToSpeech

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
