from django.shortcuts import render
from django.http import HttpResponse
from num2words import num2words # type: ignore
from PIL import Image, ImageDraw, ImageFont # type: ignore
import os

def index(request):
    words = None
    cheque_url = None
    if request.method == 'POST':
        amount = int(request.POST.get('amount'))
        words = num2words(amount, lang='en_IN').replace(',', '').replace('-', ' ').title() + ' Only'
        
        # Generate Cheque Image
        cheque_image_path = generate_cheque_image(amount, words)
        cheque_url = f'/media/{cheque_image_path}'

    return render(request, 'converter/index.html', {'words': words, 'cheque_url': cheque_url})

def generate_cheque_image(amount, words):
    # Create a blank cheque image
    cheque_img = Image.new('RGB', (800, 300), color=(255, 255, 255))
    d = ImageDraw.Draw(cheque_img)

    # Use default font
    font = ImageFont.load_default()

    # Draw text on the cheque
    d.text((10, 50), f'Amount: Rs {amount}', fill=(0, 0, 0), font=font)
    d.text((10, 100), f'In Words: {words}', fill=(0, 0, 0), font=font)

    # Save the image
    media_root = 'media'
    if not os.path.exists(media_root):
        os.makedirs(media_root)
    cheque_image_path = os.path.join(media_root, 'cheque.png')
    cheque_img.save(cheque_image_path)

    return 'cheque.png'
