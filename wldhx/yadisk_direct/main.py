import click
import requests

API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'


def get_real_direct_link(sharing_link: str) -> str:
    pk_request = requests.get(API_ENDPOINT.format(sharing_link))

    return pk_request.json()['href']


@click.command()
@click.argument('sharing_link', type=str, nargs=-1)
@click.option('-s', '--separator', type=str, default=' ', help='A string to separate output links with')
def main(sharing_link, separator):
    """Get real direct links usable with tools like curl or wget for files stored in Yandex.Disk."""

    print(*[get_real_direct_link(x) for x in sharing_link], sep=separator)


if __name__ == '__main__':
    main()
