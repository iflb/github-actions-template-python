from github_actions_template_python import __version__
from github_actions_template_python import calc_sum


def test_version():
    assert __version__ == '0.1.0'

def test_calc_sum():
    assert calc_sum(1,2,3) == 1+2+3
    assert calc_sum(1,2,3,4,5) == 1+2+3+4+5
    
def test_calc_sum2():
    assert calc_sum(1,2,3) == 1+2+3
    assert calc_sum(1,2,3,4,5) == 1+2+3+4+5
    
