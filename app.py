"""
Web Interface for Image Caption Generator using Gradio
This script creates an interactive web interface where users can upload images
and get AI-generated captions describing the content.
"""

import gradio as gr
from caption_generator import ImageCaptionGenerator


# Initialize the caption generator (load model once)
print("Initializing Image Caption Generator...")
generator = ImageCaptionGenerator()


def generate_caption_interface(image):
    """
    Interface function for Gradio to generate captions.
    
    Args:
        image: PIL Image object from Gradio interface
    
    Returns:
        str: Generated caption
    """
    if image is None:
        return "Please upload an image first."
    
    caption = generator.generate_caption_from_pil(image)
    return caption


# Create Gradio interface
demo = gr.Interface(
    fn=generate_caption_interface,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=gr.Textbox(label="Generated Caption", lines=3),
    title="🖼️ AI Image Caption Generator",
    description="""
    Upload any image and let AI generate a descriptive caption!
    
    This tool uses the BLIP (Bootstrapping Language-Image Pre-training) model 
    to understand image content and generate natural language descriptions.
    
    **Examples to try:**
    - Photos of people and their activities
    - Animals in different settings
    - Landscapes and cityscapes
    - Objects and scenes
    """
)


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Starting Image Caption Generator Web Interface")
    print("="*50)
    print("\nThe interface will open in your browser automatically.")
    print("You can also access it at the URL shown below.\n")
    
    # Launch the interface
    demo.launch(
        share=True,  # Set to True to create a public link
        show_error=True
    )
