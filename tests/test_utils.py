import pytest

def test_loading_utils():
    import myutils

def test_utils_make_movie_file_does_not_exist():
    from myutils.movie import make_movie
    print(make_movie(figures='./does_not_exist_%03d.png', filename='./does_not_exist.mp4'))

