from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Путь к файлу для записи действий
log_file_path = 'actions_log.txt'


def log_action(action):
    """Записывает действие в файл лога."""
    with open(log_file_path, 'a') as file:
        file.write(action)


@app.route('/set_info', methods=['POST'])
def set_info():
    global stored_text
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    stored_text = data['text']

    # Логируем действие
    log_action(f'{stored_text}')

    return jsonify({'message': 'Text stored successfully'}), 200


@app.route('/get_info', methods=['GET'])
def get_info():
    with open(log_file_path, "r") as data:
        return data.readlines()

@app.route('/clear', methods=['GET'])
def clear():
    os.remove("actions_log.txt")
    return "Clear comands"



if __name__ == '__main__':
    app.run(debug=True)