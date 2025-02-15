from PIL import Image, ImageDraw, ImageFont

def add_text_to_panel(text, panel_image):
    # Generate an image containing the text
    text_image = generate_text_image(text)

    # Create a new image large enough to contain the panel image and the text image
    result_image = Image.new('RGB', (panel_image.width, panel_image.height + text_image.height))

    # Paste the panel image at the top of the result image
    result_image.paste(panel_image, (0, 0))

    # Paste the text image below the panel image
    result_image.paste(text_image, (0, panel_image.height))

    return result_image

def generate_text_image(text):
    # Define image dimensions
    width = 1024
    height = 128

    # Create a white background image
    image = Image.new('RGB', (width, height), color='white')

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Choose a font (Pillow's default font or fallback)
    try:
        font = ImageFont.truetype(font="manga-temple.ttf", size=30)
    except IOError:
        print("Font not found. Using default font.")
        font = ImageFont.load_default()

    # Calculate text size using textbbox (returns a bounding box around the text)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate the position to center the text horizontally and vertically
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Define text color (black in this example)
    text_color = (0, 0, 0)

    # Add text to the image
    draw.text((x, y), text, fill=text_color, font=font)

    return image
