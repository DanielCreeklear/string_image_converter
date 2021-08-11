from PIL.JpegImagePlugin import JpegImageFile
from PIL.Image import Image
from pytest import mark


@mark.usefixtures('image_processing')
def test_should_return_jpeg_image_object(image_processing):
    image_processing.open_image('./example.jpg')
    assert type(image_processing.image) is JpegImageFile


@mark.usefixtures('image_processing')
def test_should_return_image_with_new_size(image_processing):
    image_processing.open_image('./example.jpg')
    assert image_processing.resize_image(100) == (100, 56)


@mark.usefixtures('image_processing')
def test_should_return_image_gray_scale(image_processing):
    image_processing.open_image('./example.jpg')
    assert type(image_processing.grayify()) is Image


@mark.usefixtures('image_processing')
def test_should_return_image_string(image_processing):
    image_processing.open_image('./example.jpg')
    assert type(image_processing.pixels_to_ascii()) is str
