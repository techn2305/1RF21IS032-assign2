# app6/utils.py
import datetime

def encode_message(message):
    # Determine if the current day is odd or even
    current_day = datetime.datetime.now().day
    is_odd_day = current_day % 2 != 0
    
    # Define encoding dictionaries
    odd_day_encoding = {chr(i + 64): f'{i:02}' for i in range(1, 27)}
    even_day_encoding = {chr(i + 64): f'5{i:02}' for i in range(1, 27)}
    
    encoded_message = []
    
    for char in message.upper():
        if char.isalpha():
            if is_odd_day:
                encoded_message.append(odd_day_encoding[char])
            else:
                encoded_message.append(even_day_encoding[char])
        else:
            encoded_message.append(char)
    
    return ' '.join(encoded_message)
