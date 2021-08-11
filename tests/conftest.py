from converter_ascii import ImageProcessing
from pytest import fixture
from PIL.Image import open


@fixture
def image_processing():
    return ImageProcessing()
