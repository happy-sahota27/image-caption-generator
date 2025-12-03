# 🖼️ AI Image Caption Generator

An intelligent image captioning system that uses deep learning to automatically generate descriptive captions for images. Simply upload an image, and the AI will describe what it sees!

## ✨ Features

- **Automatic Caption Generation**: Upload any image and get an AI-generated description
- **Pre-trained Model**: Uses BLIP (Bootstrapping Language-Image Pre-training) from Salesforce
- **Easy-to-Use Web Interface**: Interactive Gradio interface for seamless image upload
- **High Accuracy**: State-of-the-art vision-language model for accurate descriptions
- **GPU Support**: Automatically uses GPU if available for faster processing

## 🎯 What It Can Do

The model can identify and describe:
- People and their activities (e.g., "a man playing guitar")
- Animals and their behaviors (e.g., "a cat sitting next to a dog")
- Objects and scenes (e.g., "a red car parked on a street")
- Landscapes and environments (e.g., "a beach with palm trees at sunset")
- Complex scenarios with multiple elements

## 📋 Requirements

- Python 3.8 or higher
- Internet connection (for initial model download)
- At least 4GB RAM (8GB recommended)
- GPU is optional but recommended for faster processing

## 🚀 Installation

1. **Clone or download this project**

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: First-time installation will download the BLIP model (~2GB). This is a one-time download.

## 🎮 Usage

### Option 1: Web Interface (Recommended)

1. **Run the web application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   - The interface will automatically open at `http://127.0.0.1:7860`
   - If it doesn't open automatically, click the URL shown in the terminal

3. **Upload and generate**
   - Click the image upload area
   - Select an image from your computer
   - Wait a few seconds for the AI to generate the caption
   - View the generated description!

### Option 2: Python Script

1. **Use the caption generator directly in your code**
   ```python
   from caption_generator import ImageCaptionGenerator
   
   # Initialize the generator
   generator = ImageCaptionGenerator()
   
   # Generate caption for an image
   caption = generator.generate_caption("path/to/your/image.jpg")
   print(f"Caption: {caption}")
   ```

2. **Use the example script**
   ```bash
   python example.py
   ```

## 📁 Project Structure

```
imageCaptionGenerator/
├── caption_generator.py   # Core caption generation logic
├── app.py                 # Web interface using Gradio
├── example.py            # Example usage script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔧 Configuration

You can customize the caption generation in `caption_generator.py`:

- **max_length**: Maximum length of generated captions (default: 50)
- **num_beams**: Beam search parameter for quality (default: 5, higher = better but slower)
- **model_name**: Change the model variant (default: BLIP-large)

## 🐛 Troubleshooting

### Model Download Issues
If the model fails to download:
- Check your internet connection
- Ensure you have enough disk space (~2GB)
- Try running the script again

### Memory Issues
If you run out of memory:
- Use the base model instead: `"Salesforce/blip-image-captioning-base"`
- Close other applications
- Use a smaller image size

### GPU Not Detected
The model will automatically use CPU if GPU is not available. This is slower but works perfectly fine.

## 📚 Technical Details

**Model**: BLIP (Bootstrapping Language-Image Pre-training)
- **Developer**: Salesforce Research
- **Architecture**: Vision Transformer + Language Model
- **Training Data**: Large-scale image-text pairs
- **Capabilities**: Image understanding, caption generation, visual question answering

## 🎓 How It Works

1. **Image Processing**: The image is preprocessed and converted to a format the model understands
2. **Visual Encoding**: A vision transformer extracts visual features from the image
3. **Caption Generation**: A language model generates natural language descriptions based on visual features
4. **Beam Search**: Multiple caption candidates are generated and the best one is selected

## 🌟 Example Results

```
Input: Image of a golden retriever playing in a park
Output: "a dog running through a grassy field"

Input: Image of a person cooking in a kitchen
Output: "a person standing in front of a stove in a kitchen"

Input: Image of a sunset over mountains
Output: "a view of a mountain range at sunset"
```

## 📄 License

This project uses the BLIP model which is released under the BSD-3-Clause License by Salesforce.

## 🤝 Contributing

Feel free to fork this project and make improvements! Some ideas:
- Add support for multiple languages
- Implement batch processing
- Add more model options
- Create a mobile app interface

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the error messages carefully
3. Ensure all dependencies are installed correctly

## 🎉 Enjoy!

Start generating captions for your images and explore the power of AI vision-language models!
