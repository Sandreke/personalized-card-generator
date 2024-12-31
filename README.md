# Personalized Card Generator

A Python tool to generate personalized greeting cards for any occasion using custom templates and fonts. Perfect for creating bulk personalized cards for birthdays, holidays, special events, or any celebration.

## Features

- Generate personalized cards from Excel data
- Support for custom templates and fonts
- Batch processing capability
- Flexible text positioning and styling
- Support for regular, bold, and bold-italic font variants

## Requirements

- Python 3.6+
- Pillow (PIL)
- pandas
- openpyxl
- Excel file with recipient names

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Sandreke/personalized-card-generator.git
cd personalized-card-generator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Prepare your data:
   - Create an Excel file with a column named 'name' containing recipient names
   - Place your template image (PNG format) in the project directory
   - Add your fonts to the `fonts` directory

2. Update the configuration in `main()`:
```python
TEMPLATE_PATH = "path/to/your/template.png"
FONT_PATH = "path/to/your/font.ttf"
SENDER_NAME = "Your Name"
DATA_PATH = "path/to/your/data.xlsx"
```

3. Run the script:
```bash
python card_generator.py
```

Generated cards will be saved in the `output` directory.

## File Structure
```
personalized-card-generator/
├── card_generator.py
├── template.png
├── friends.xlsx
├── fonts/
│   ├── your-font-regular.ttf
│   ├── your-font-bold.ttf
│   └── your-font-bold-italic.ttf
├── output/
│   └── (generated cards)
└── requirements.txt
```

## Template Requirements

- Image format: PNG
- Recommended resolution: 1920x1080 or higher
- Areas for text should have good contrast

## Font Requirements

- TTF format
- Font family should include regular, bold, and bold-italic variants
- File naming convention: `fontname-regular.ttf`, `fontname-bold.ttf`, `fontname-bold-italic.ttf`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
