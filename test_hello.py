import hello

def test_hello():
    assert hello.hello("kasra") == "hello kasra"

def test_default_hello():
    assert hello.hello("") == "hello world"


