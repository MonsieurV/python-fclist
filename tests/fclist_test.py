import types
from fclist import fclist, Font

def test_list_fonts():
    """
    The fclist() function list system fonts.
    """
    fonts = fclist()
    assert isinstance(fonts, types.GeneratorType) is True
    nb_fonts = 1
    for font in fonts:
        nb_fonts += 1
        assert isinstance(font, Font) is True
        assert 'family' in dir(font)
        assert 'fullname' in dir(font)
        assert 'style' in dir(font)
        assert 'file' in dir(font)
        assert 'fontformat' in dir(font)
        assert 'foundry' in dir(font)
    assert nb_fonts > 2
