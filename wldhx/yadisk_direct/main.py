from sys import argv
import requests

API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'


def get_real_direct_link(sharing_link: str) -> str:
    pk_request = requests.get(API_ENDPOINT.format(sharing_link))

    return pk_request.json()['href']


def main():
    yad_url = argv[1]

    print(get_real_direct_link(yad_url))


if __name__ == '__main__':
    main()
