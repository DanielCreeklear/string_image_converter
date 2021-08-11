from PIL.JpegImagePlugin import JpegImageFile
from pytest import mark


@mark.usefixtures('image_processing')
def test_should_return_jpeg_image_object(image_processing):
    assert type(image_processing.open_image('./example.jpg')) is JpegImageFile


@mark.usefixtures('image_processing')
def test_should_return_image_with_new_size(image_processing):
    assert image_processing.resize(100) == (10, 10)


@mark.usefixtures('image_processing')
def test_should_return_image_gray_scale(image_processing):
    assert type(image_processing.grayify()) is JpegImageFile


@mark.usefixtures('example_image')
def test_should_return_image_string(image_processing):
    assert type(image_processing.pixels_to_ascii()) is str
