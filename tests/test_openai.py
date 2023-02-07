import openai
import pytest

from errors.error_messages import ERROR_MESSAGES_RU
from external_services.openai import get_openai_response


@pytest.fixture
def mock_response():
    return {'id': '123', 'choices': [{'text': 'Example response'}]}


def test_get_openai_response(mocker, mock_response):
    mocker.patch.object(openai.Completion, 'create', return_value=mock_response)
    response = get_openai_response('Test prompt')
    assert response == mock_response['choices'][0]['text']


def test_get_openai_response_error(mocker):
    mock_error = openai.OpenAIError('Mock error')
    mocker.patch.object(openai.Completion, 'create', side_effect=mock_error)
    response = get_openai_response('Test prompt')
    assert response == ERROR_MESSAGES_RU['openai_error']
