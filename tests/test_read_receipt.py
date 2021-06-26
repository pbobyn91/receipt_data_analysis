from read_receipt import get_image, read_img


def test_gets_text():
    receipt = get_image(test=True)
    data = read_img(receipt)
    assert data, "This should have text"
