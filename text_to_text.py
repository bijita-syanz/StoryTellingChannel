import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class TextToText:
    """
    A class to generate and process text using Google Gemini API
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the TextToText class
        
        Args:
            api_key (str): Google Gemini API key. If not provided, will try to get from environment variable
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key not provided. Set GEMINI_API_KEY environment variable.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_story(self, prompt, temperature=0.7, max_tokens=500):
        """
        Generate a story based on the given prompt
        
        Args:
            prompt (str): The prompt to generate story from
            temperature (float): Controls randomness (0.0 - 1.0). Default is 0.7
            max_tokens (int): Maximum tokens in the response
        
        Returns:
            str: Generated story text if successful, None otherwise
        """
        if not prompt or not prompt.strip():
            print("Error: Prompt cannot be empty")
            return None
        
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens,
                )
            )
            return response.text
        except Exception as e:
            print(f"Error generating story: {e}")
            return None
    
    def enhance_text(self, text, style="formal"):
        """
        Enhance or rewrite text in a specific style
        
        Args:
            text (str): The text to enhance
            style (str): The style to apply (formal, casual, poetic, technical, etc.)
        
        Returns:
            str: Enhanced text if successful, None otherwise
        """
        if not text or not text.strip():
            print("Error: Text cannot be empty")
            return None
        
        try:
            prompt = f"Please rewrite the following text in a {style} style:\n\n{text}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error enhancing text: {e}")
            return None
    
    def summarize_text(self, text, length="medium"):
        """
        Summarize the given text
        
        Args:
            text (str): The text to summarize
            length (str): Length of summary (short, medium, long)
        
        Returns:
            str: Summarized text if successful, None otherwise
        """
        if not text or not text.strip():
            print("Error: Text cannot be empty")
            return None
        
        try:
            length_instructions = {
                "short": "in 1-2 sentences",
                "medium": "in 3-5 sentences",
                "long": "in a paragraph"
            }
            
            instruction = length_instructions.get(length, "in 3-5 sentences")
            prompt = f"Please summarize the following text {instruction}:\n\n{text}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error summarizing text: {e}")
            return None
    
    def translate_text(self, text, target_language):
        """
        Translate text to a target language
        
        Args:
            text (str): The text to translate
            target_language (str): The target language (e.g., 'Arabic', 'Spanish', 'French')
        
        Returns:
            str: Translated text if successful, None otherwise
        """
        if not text or not text.strip():
            print("Error: Text cannot be empty")
            return None
        
        try:
            prompt = f"Please translate the following text to {target_language}:\n\n{text}\n\nProvide only the translation, nothing else."
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error translating text: {e}")
            return None
    
    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the given text
        
        Args:
            text (str): The text to analyze
        
        Returns:
            dict: Sentiment analysis with sentiment type and explanation
        """
        if not text or not text.strip():
            print("Error: Text cannot be empty")
            return None
        
        try:
            prompt = f"Analyze the sentiment of the following text. Respond with JSON format: {{'sentiment': 'positive/negative/neutral', 'confidence': 0.0-1.0, 'explanation': 'brief explanation'}}:\n\n{text}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return None
    
    def creative_write(self, topic, genre="general"):
        """
        Generate creative writing based on topic and genre
        
        Args:
            topic (str): The topic to write about
            genre (str): The genre (story, poem, script, etc.)
        
        Returns:
            str: Creative writing if successful, None otherwise
        """
        if not topic or not topic.strip():
            print("Error: Topic cannot be empty")
            return None
        
        try:
            prompt = f"Write a creative {genre} about the following topic:\n\n{topic}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating creative content: {e}")
            return None
