import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'AQAAAABeVj3BAADLW2ETxduOYUAxlX3ukwhnvnA'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path):
    """Создание папки. \n path: Путь к создаваемой папке."""
    response = requests.put(f'{URL}?path={path}', headers=headers)

    response.raise_for_status()
    return response.status_code








    #успешно
    # if response.status_code == 201:
    #     result = 'Success'
    #     return result

    #ресурс уже существует
    # if response.status_code == 409:
    #     result = 'Ресурс уже существует'
    #     return result


# create_folder('hello world')
# create_folder('hello world/api')
# create_folder('test_api')