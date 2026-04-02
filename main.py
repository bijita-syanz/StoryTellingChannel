from text_to_speech import TextToSpeech
from text_to_text import TextToText

MAIN_PROMPT = "You are a creative storytelling assistant. Help users create engaging, imaginative stories in both English and Arabic. Enhance their prompts and generate compelling narratives that captivate readers."

def enhance_prompt(user_prompt: str, prompt_type: str = "creative") -> str:
    """
    Enhance a user prompt using the Gemini API.
    
    Args:
        user_prompt (str): The original user prompt
        prompt_type (str): Type of enhancement - 'creative', 'detailed', 'technical', 'formal'
    
    Returns:
        str: Enhanced prompt
    """
    ttt = TextToText()
    
    enhancement_instructions = {
        "creative": "Make this prompt more creative, imaginative, and engaging for storytelling.",
        "detailed": "Expand this prompt with more specific details and context.",
        "technical": "Make this prompt more technical and precise with clear specifications.",
        "formal": "Rewrite this prompt in a formal, professional tone."
    }
    
    instruction = enhancement_instructions.get(prompt_type, enhancement_instructions["creative"])
    
    enhanced = ttt.enhance_text(user_prompt, instruction)
    return enhanced

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
    
    # Example: Enhance a prompt
    print("\n--- Testing Enhance Prompt Function ---")
    original = "Write a story about a robot"
    
    for ptype in ["creative", "detailed", "technical", "formal"]:
        enhanced = enhance_prompt(original, ptype)
        print(f"\n{ptype.upper()} Enhancement:")
        print(f"Original: {original}")
        print(f"Enhanced: {enhanced}")
