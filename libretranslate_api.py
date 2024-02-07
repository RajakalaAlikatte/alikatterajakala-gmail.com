from flask import Flask, jsonify, request
from libretranslate import LibreTranslate

app = Flask(__name__)

def translate_to_english(text, source_lang='auto', to_lang='en'):
    translator = LibreTranslate()

    # Translate to English
    translated_text = translator.translate(text, source_lang=source_lang, target_lang=to_lang)

    translated_info = {
        'input_text': text,
        'translated_text': translated_text
    }

    return translated_info

@app.route('/translate-language', methods=['POST'])
def translate_language_api():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Text not provided in the request'}), 400

    text_data = data['text']

    # Specify source language if known, or use 'auto' for automatic language detection
    source_language = 'auto'

    translated_text = translate_to_english(text_data, source_lang=source_language)

    return jsonify({'translation': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
