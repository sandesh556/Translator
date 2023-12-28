from googletrans import Translator
import os


def translate_file_for_all_languages(source_lang, file_name):
    translator = Translator()

    source_file_path = f"lang/{source_lang}/{file_name}.py"

    if not os.path.exists(source_file_path):
        print("Source language file not found.")
        return

    with open(source_file_path, 'r', encoding='utf-8') as source_file:
        data = eval(source_file.read())  # Assuming it contains a Python dictionary

        for target_lang in os.listdir("lang"):
            if target_lang == source_lang or not os.path.isdir(f"lang/{target_lang}"):
                continue

            target_dir_path = f"lang/{target_lang}"

            translated_data = {}
            for key, value in data.items():
                translation = translator.translate(value, src=source_lang, dest=target_lang)
                translated_data[key] = translation.text

            target_file_path = f"{target_dir_path}/{file_name}.php"
            formatted_string = "<?php\nreturn " + format_as_php_array(translated_data) + ";\n"

            with open(target_file_path, 'w', encoding='utf-8') as target_file:
                target_file.write(formatted_string)

            print(f"Translation for {target_lang} complete!")


def format_as_php_array(data):
    formatted_array = "array(\n"
    for key, value in data.items():
        formatted_array += f"    '{key}' => '{value}',\n"
    formatted_array += ")"
    return formatted_array


# User Input
source_lang = input("Enter the language code that you finish to translate from: ")
file_name = input("Enter file name (just the name): ")

# Usage example with user input
translate_file_for_all_languages(source_lang, file_name)
