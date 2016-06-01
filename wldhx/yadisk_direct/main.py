import defopt
import requests

API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'


def get_real_direct_link(sharing_link: str) -> str:
    pk_request = requests.get(API_ENDPOINT.format(sharing_link))

    return pk_request.json()['href']


def main(*sharing_link: str, separator: str = ' '):
    """Get real direct links usable with tools like curl or wget for files stored in Yandex.Disk.

    :param  sharing_link: YaDisk sharing link (like https://yadi.sk/i/LKkWupFjr5WzR)
    :param  separator:    A string to separate output links with
    """

    print(*[get_real_direct_link(x) for x in sharing_link], sep=separator)


if __name__ == '__main__':
    defopt.run(main)
