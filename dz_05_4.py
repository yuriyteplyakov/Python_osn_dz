translate = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}
with open("text_4.txt") as file, open("translate.txt", 'w') as new_file:
    content = file.readlines()
    for line in content:
        english_dict = line.split()
        rus_translate = translate.get(english_dict[0])
        new_file.write(f'{line.replace(english_dict[0], rus_translate)}')