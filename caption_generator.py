"""
Image Caption Generator using Pre-trained BLIP Model
This module provides functionality to generate captions for images using
the BLIP (Bootstrapping Language-Image Pre-training) model from Hugging Face.
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch


class ImageCaptionGenerator:
    """
    A class to generate captions for images using the BLIP model.
    
    The BLIP model is a state-of-the-art vision-language model that can
    generate descriptive captions for images by understanding the visual
    content and converting it to natural language.
    """
    
    def __init__(self, model_name="Salesforce/blip-image-captioning-large"):
        """
        Initialize the caption generator with a pre-trained model.
        
        Args:
            model_name (str): The name of the pre-trained model to use.
                            Default is BLIP large model for better accuracy.
        """
        print(f"Loading model: {model_name}...")
        
        # Determine device (GPU if available, otherwise CPU)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        
        # Load the processor and model
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name).to(self.device)
        
        print("Model loaded successfully!")
    
    def generate_caption(self, image_path, max_length=50, num_beams=5):
        """
        Generate a caption for a given image.
        
        Args:
            image_path (str): Path to the image file
            max_length (int): Maximum length of the generated caption
            num_beams (int): Number of beams for beam search (higher = better quality but slower)
        
        Returns:
            str: Generated caption describing the image
        """
        try:
            # Load and process the image
            image = Image.open(image_path).convert('RGB')
            
            # Prepare inputs
            inputs = self.processor(image, return_tensors="pt").to(self.device)
            
            # Generate caption
            output = self.model.generate(
                **inputs,
                max_length=max_length,
                num_beams=num_beams,
                early_stopping=True
            )
            
            # Decode the generated caption
            caption = self.processor.decode(output[0], skip_special_tokens=True)
            
            return caption
            
        except Exception as e:
            return f"Error generating caption: {str(e)}"
    
    def generate_caption_from_pil(self, pil_image, max_length=50, num_beams=5):
        """
        Generate a caption for a PIL Image object.
        
        Args:
            pil_image (PIL.Image): PIL Image object
            max_length (int): Maximum length of the generated caption
            num_beams (int): Number of beams for beam search
        
        Returns:
            str: Generated caption describing the image
        """
        try:
            # Convert to RGB if necessary
            image = pil_image.convert('RGB')
            
            # Prepare inputs
            inputs = self.processor(image, return_tensors="pt").to(self.device)
            
            # Generate caption
            output = self.model.generate(
                **inputs,
                max_length=max_length,
                num_beams=num_beams,
                early_stopping=True
            )
            
            # Decode the generated caption
            caption = self.processor.decode(output[0], skip_special_tokens=True)
            
            return caption
            
        except Exception as e:
            return f"Error generating caption: {str(e)}"


def main():
    """
    Example usage of the ImageCaptionGenerator class.
    """
    # Initialize the generator
    generator = ImageCaptionGenerator()
    
    # Example: Generate caption for an image
    # Replace 'test_image.jpg' with your actual image path
    image_path = "test_image.jpg"
    
    print(f"\nGenerating caption for: {image_path}")
    caption = generator.generate_caption(image_path)
    print(f"Caption: {caption}")


if __name__ == "__main__":
    main()
