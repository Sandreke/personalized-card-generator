from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from pathlib import Path

class CardGenerator:
    """
    A class to generate personalized greeting cards using a template and custom fonts.
    """
    def __init__(self, template_path: str, font_path: str):
        """
        Initialize the card generator with template and font paths.
        
        Args:
            template_path (str): Path to the template image
            font_path (str): Path to the font file (.ttf)
        """
        self.template_path = Path(template_path)
        self.font_path = Path(font_path)
        self._validate_paths()
        
    def _validate_paths(self):
        """Validate that all required files exist."""
        if not self.template_path.exists():
            raise FileNotFoundError(f"Template not found: {self.template_path}")
        if not self.font_path.exists():
            raise FileNotFoundError(f"Font file not found: {self.font_path}")
    
    def create_card(self, sender_name: str, recipient_name: str, output_path: str, 
                   font_size: int = 60):
        """
        Create a personalized card for a specific recipient.
        
        Args:
            sender_name (str): Name of the person sending the card
            recipient_name (str): Name of the recipient
            output_path (str): Where to save the generated card
            font_size (int): Size of the font (default: 60)
        """
        # Open and prepare template
        img = Image.open(self.template_path)
        draw = ImageDraw.Draw(img)
        
        # Load fonts
        try:
            font_regular = ImageFont.truetype(str(self.font_path), font_size)
            # Try to load bold and bold-italic variants
            bold_path = str(self.font_path).replace('-regular.ttf', '-bold.ttf')
            bold_italic_path = str(self.font_path).replace('-regular.ttf', '-bold-italic.ttf')
            
            font_bold = ImageFont.truetype(bold_path, font_size)
            font_bold_italic = ImageFont.truetype(bold_italic_path, font_size)
        except Exception as e:
            print(f"Warning: Font loading error: {e}")
            print("Using default font...")
            font_regular = font_bold = font_bold_italic = ImageFont.load_default()
        
        # Get image dimensions
        width, height = img.size
        
        # Prepare text
        greeting = "Con cariño, "
        
        # Calculate text dimensions
        greeting_bbox = draw.textbbox((0, 0), greeting, font=font_regular)
        name_bbox = draw.textbbox((0, 0), recipient_name, font=font_bold)
        
        # Calculate total width and maximum height
        total_width = (greeting_bbox[2] - greeting_bbox[0]) + (name_bbox[2] - name_bbox[0])
        max_height = max(greeting_bbox[3] - greeting_bbox[1], name_bbox[3] - name_bbox[1])
        
        # Position text (centered, slightly above middle)
        x = (width - total_width) / 2 + 350
        y = (height - max_height) / 2 - 150
        
        # Draw greeting and recipient name
        draw.text((x, y), greeting, font=font_regular, fill=(255, 255, 255))
        draw.text((x + (greeting_bbox[2] - greeting_bbox[0]), y), 
                 recipient_name, font=font_bold, fill=(255, 255, 255))
        
        # Add sender signature
        draw.text((1084, 1060), sender_name, font=font_bold_italic, fill=(235, 176, 110))
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save the card
        img.save(output_path)
        
    def generate_batch(self, sender_name: str, data_path: str, output_dir: str = "output"):
        """
        Generate cards for all recipients in an Excel file.
        
        Args:
            sender_name (str): Name of the person sending the cards
            data_path (str): Path to Excel file containing recipient names
            output_dir (str): Directory to save generated cards (default: 'output')
        """
        # Read recipient data
        df = pd.read_excel(data_path)
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate cards for each recipient
        for index, row in df.iterrows():
            recipient_name = row['name']
            output_path = os.path.join(output_dir, f"card_{recipient_name}.png")
            
            self.create_card(sender_name, recipient_name, output_path)
            print(f"Created card for: {recipient_name}")

def main():
    """Example usage of the CardGenerator class."""
    # Configuration
    TEMPLATE_PATH = "template.png"
    FONT_PATH = "fonts/cocomat-pro-regular.ttf"
    SENDER_NAME = "Sandreke"
    DATA_PATH = "friends.xlsx"
    
    # Initialize generator
    generator = CardGenerator(TEMPLATE_PATH, FONT_PATH)
    
    # Generate cards
    generator.generate_batch(SENDER_NAME, DATA_PATH)

if __name__ == "__main__":
    main()