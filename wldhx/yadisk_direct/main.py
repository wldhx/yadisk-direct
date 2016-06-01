import argparse
import requests

API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'


def get_real_direct_link(sharing_link: str) -> str:
    pk_request = requests.get(API_ENDPOINT.format(sharing_link))

    return pk_request.json()['href']


def main():
    parser = argparse.ArgumentParser(description='Get real direct links usable with tools like curl or wget for files stored in Yandex.Disk.')
    parser.add_argument('sharing_links', type=str, nargs='+',
            help='YaDisk sharing links (like https://yadi.sk/i/LKkWupFjr5WzR)')
    args = parser.parse_args()

    print(*[get_real_direct_link(x) for x in args.sharing_links], sep=' ')


if __name__ == '__main__':
    main()
