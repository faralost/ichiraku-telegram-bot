import random

from imagekitio import ImageKit
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions

from config_data import config

imagekit = ImageKit(
    private_key=config.IMAGEKIT_PRIVATE_KEY,
    public_key=config.IMAGEKIT_PUBLIC_KEY,
    url_endpoint='https://ik.imagekit.io/faralost'
)


def get_file_urls_from_folder(folder_name: str) -> list[str]:
    list_files = imagekit.list_files(options=ListAndSearchFileRequestOptions(path=folder_name))
    return [file.url for file in list_files.list]


def get_random_photo_url(folder_name: str) -> str:
    return random.choice(get_file_urls_from_folder(folder_name))
