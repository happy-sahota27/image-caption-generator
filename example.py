"""
Example script demonstrating how to use the Image Caption Generator.
This script shows various ways to generate captions for images.
"""

from caption_generator import ImageCaptionGenerator
import os


def main():
    print("="*60)
    print("Image Caption Generator - Example Usage")
    print("="*60)
    
    # Initialize the caption generator
    print("\n[1/3] Initializing the caption generator...")
    generator = ImageCaptionGenerator()
    
    print("\n[2/3] Ready to generate captions!")
    print("\n" + "="*60)
    
    # Example 1: Generate caption for a specific image
    print("\n📸 Example 1: Single Image Caption Generation")
    print("-" * 60)
    
    # You can replace this with your own image path
    image_path = input("\nEnter the path to your image file (or press Enter to skip): ").strip()
    
    if image_path and os.path.exists(image_path):
        print(f"\nGenerating caption for: {image_path}")
        caption = generator.generate_caption(image_path)
        print(f"\n✨ Generated Caption: '{caption}'")
    elif image_path:
        print(f"\n❌ Error: File not found at '{image_path}'")
        print("Please make sure the path is correct and try again.")
    else:
        print("\n⏭️  Skipped - No image path provided")
    
    # Example 2: Generate captions for multiple images
    print("\n\n📸 Example 2: Batch Processing Multiple Images")
    print("-" * 60)
    
    # Example list of images (you can modify this)
    image_folder = input("\nEnter a folder path containing images (or press Enter to skip): ").strip()
    
    if image_folder and os.path.exists(image_folder):
        # Get all image files in the folder
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp']
        image_files = [
            os.path.join(image_folder, f) 
            for f in os.listdir(image_folder) 
            if os.path.isfile(os.path.join(image_folder, f)) and 
            os.path.splitext(f)[1].lower() in image_extensions
        ]
        
        if image_files:
            print(f"\nFound {len(image_files)} images. Generating captions...\n")
            
            for i, img_path in enumerate(image_files, 1):
                filename = os.path.basename(img_path)
                print(f"[{i}/{len(image_files)}] {filename}")
                caption = generator.generate_caption(img_path)
                print(f"    Caption: '{caption}'\n")
        else:
            print(f"\n❌ No image files found in '{image_folder}'")
    elif image_folder:
        print(f"\n❌ Error: Folder not found at '{image_folder}'")
    else:
        print("\n⏭️  Skipped - No folder path provided")
    
    # Example 3: Customizing generation parameters
    print("\n\n📸 Example 3: Custom Generation Parameters")
    print("-" * 60)
    print("\nYou can customize the caption generation with parameters:")
    print("  - max_length: Maximum length of the caption")
    print("  - num_beams: Number of beams for beam search (higher = better quality)")
    
    custom_image = input("\nEnter an image path to try custom parameters (or press Enter to skip): ").strip()
    
    if custom_image and os.path.exists(custom_image):
        print("\nGenerating with default parameters (max_length=50, num_beams=5):")
        caption1 = generator.generate_caption(custom_image, max_length=50, num_beams=5)
        print(f"  Caption: '{caption1}'")
        
        print("\nGenerating with custom parameters (max_length=30, num_beams=3):")
        caption2 = generator.generate_caption(custom_image, max_length=30, num_beams=3)
        print(f"  Caption: '{caption2}'")
    elif custom_image:
        print(f"\n❌ Error: File not found at '{custom_image}'")
    else:
        print("\n⏭️  Skipped - No image path provided")
    
    # Conclusion
    print("\n\n" + "="*60)
    print("[3/3] Example completed!")
    print("="*60)
    print("\n💡 Tips:")
    print("  - Use the web interface (app.py) for a more user-friendly experience")
    print("  - Import the ImageCaptionGenerator class in your own scripts")
    print("  - The model works best with clear, well-lit images")
    print("  - First run will be slower as the model loads into memory")
    print("\n🚀 To launch the web interface, run: python app.py")
    print("\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\n❌ An error occurred: {str(e)}")
        print("Please check your setup and try again.")
