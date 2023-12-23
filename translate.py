from googletrans import Translator
import os





def split_text(text, max_length=4000):
    """
    Split text into parts with a maximum length of max_length.
    """
    parts = []
    while text:
        part = text[:max_length]
        if '\n' in part:
            # Try to split at the last newline character to avoid breaking words
            last_newline = part.rfind('\n')
            part = text[:last_newline]  # Take text up to the last complete line
            text = text[last_newline:]  # Remaining text becomes the new text
        else:
            text = text[max_length:]  # Just cut the text at the max length
        parts.append(part)
    return parts

def translate_text(text, source_language, destination_language):
    """
    Translate text using Google Translate and return the result.
    """
    translator = Translator()
    translated_parts = []
    for part in split_text(text):
        result = translator.translate(part, src=source_language, dest=destination_language)
        translated_parts.append(result.text)
    return '\n'.join(translated_parts)

# Define the input and output directories
input_directory = r'D:/text_az/'
output_directory = r'D:/text_en/'
source_language = 'az'
destination_language = 'en'

# Iterate over files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        with open(os.path.join(input_directory, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            translated_text = translate_text(text, source_language, destination_language)

        with open(os.path.join(output_directory, filename), 'w', encoding='utf-8') as outfile:
            outfile.write(translated_text)
