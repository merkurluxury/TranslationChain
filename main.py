from google.cloud import translate_v2 as translate
import json

translate_client = translate.Client.from_service_account_json('C:/Users/serha/Desktop/PYTHON/dogaldi-fc2229d71142.json')

with open('C:/Users/serha/Desktop/PYTHON/dataset.json', 'r') as file:
    translation_chain = json.load(file)

new_examples = []

for i in range(len(translation_chain)):
    source_text = translation_chain[i]['source_text']
    target_text = translation_chain[i]['target_text']
    next_source_text = translation_chain[(i + 1) % len(translation_chain)]['source_text']

    # Türkçe'den İngilizce'ye çeviri
    translation1 = translate_client.translate(source_text, target_language='en')['translatedText']

    # İngilizce'den Türkçe'ye çeviri
    translation2 = translate_client.translate(translation1, target_language='tr')['translatedText']

    # Yeni çeviri örneğini oluştur
    new_example = {
        "source_text": next_source_text,
        "target_text": translation2
    }

    new_examples.append(new_example)

# Veri kümesine yeni örnekleri ekleyin
with open('C:/Users/serha/Desktop/PYTHON/dataset.json', 'r') as file:
    dataset = json.load(file)

dataset.extend(new_examples)

# Güncellenmiş veri kümesini farklı bir isimle kaydedin
output_file = 'C:/Users/serha/Desktop/PYTHON/updated_dataset.json'
with open(output_file, 'w') as file:
    json.dump(dataset, file, indent=4)

print(f"Güncellenmiş veri kümesi '{output_file}' dosyasına kaydedildi.")
