import pytest
from unittest.mock import MagicMock, patch

from external_services.imagekit import get_file_urls_from_folder, get_random_photo_url


def test_get_file_urls_from_folder():
    mock_response = MagicMock()
    mock_response.list = [MagicMock(url="/file1.jpg"), MagicMock(url="/file2.jpg"), MagicMock(url="/file3.jpg")]

    with patch('external_services.imagekit.imagekit.list_files') as mock_list_files:
        mock_list_files.return_value = mock_response
        folder_name = "test_folder"
        file_urls = get_file_urls_from_folder(folder_name)
        assert file_urls == ["/file1.jpg", "/file2.jpg", "/file3.jpg"]


def test_get_random_photo_url():
    with patch('external_services.imagekit.get_file_urls_from_folder') as mock_get_file_urls_from_folder:
        mock_get_file_urls_from_folder.return_value = ["/file1.jpg", "/file2.jpg", "/file3.jpg"]
        folder_name = "test_folder"
        random_photo_url = get_random_photo_url(folder_name)
        assert random_photo_url in ["/file1.jpg", "/file2.jpg", "/file3.jpg"]
