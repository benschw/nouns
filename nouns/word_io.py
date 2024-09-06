def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as myfile:
        content = myfile.read().splitlines()
    return content


def save_data(file_path, data):
    with open(file_path, 'w') as f:
        for word in data:
            f.write(word + '\n')
