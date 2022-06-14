from sample_202205 import __version__
from sample_202205 import sum

def test_version():
    assert __version__ == '0.1.0'

def test_sum():
    assert sum(1,2,3) == 1+2+3
    assert sum(1,2,3,4,5) == 1+2+3+4+5
    
def test_sum2():
    assert sum(1,2,3) == 1+2+3
    assert sum(1,2,3,4,5) == 1+2+3+4+5
    
