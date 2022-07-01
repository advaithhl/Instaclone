import logging
from random import randint

import pytest
import requests
from django.core.files.uploadedfile import SimpleUploadedFile

from utils import random_string

logger = logging.getLogger(__name__)
disabled_loggers = [
    'PIL.Image',
    'PIL.TiffImagePlugin',
    'faker.factory',
]


def pytest_configure():
    for logger_name in disabled_loggers:
        logger = logging.getLogger(logger_name)
        logger.disabled = True


@pytest.fixture
def random_file_name():
    str_length = randint(1, 200)
    logger.debug(f'Total string length is {str_length + 4}')
    return f'{random_string(str_length)}.jpg'


@pytest.fixture
def horizontal_image():
    random_value = randint(100, 500) * 2
    height = random_value // 2
    width = random_value * 2
    logger.debug(f'Random value is {random_value}')
    logger.debug(f'Height is {height}')
    logger.debug(f'Width is {width}')
    url = f'https://picsum.photos/{width}/{height}'
    response = requests.get(url)
    logger.debug(f'Response code from picsum is {response.status_code}')
    logger.debug(f'Response content size is {len(response.content)}')
    img = SimpleUploadedFile(
        'horizontal_image.jpg',
        content=response.content,
        content_type='image/jpeg',
    )
    logger.debug(f'Generated image size if {img.size}')
    return img


@pytest.fixture
def vertical_image():
    random_value = randint(100, 500) * 2
    height = random_value * 2
    width = random_value // 2
    logger.debug(f'Random value is {random_value}')
    logger.debug(f'Height is {height}')
    logger.debug(f'Width is {width}')
    url = f'https://picsum.photos/{width}/{height}'
    response = requests.get(url)
    logger.debug(f'Response code from picsum is {response.status_code}')
    logger.debug(f'Response content size is {len(response.content)}')
    img = SimpleUploadedFile(
        'vertical_image.jpg',
        content=response.content,
        content_type='image/jpeg',
    )
    logger.debug(f'Generated image size if {img.size}')
    return img


@pytest.fixture
def default_image(random_file_name):
    logger.debug(f'Random file name is {random_file_name}')
    img = SimpleUploadedFile(
        random_file_name,
        content=open('feed/tests/assets/test_view__1.jpg', 'rb').read(),
        content_type='image/jpeg',
    )
    return img
