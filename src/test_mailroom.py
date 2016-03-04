# coding=utf-8
import pytest

DIC_TABLE = [
    (['Nadia Bahrami:10000 5 2000\n',
        'Joe McClenahan:5000 2 2500\n',
        'Cris Ewing:1000 1 1000\n',
        'John McLain:55 11 5\n',
        'Bruce Wayne:20000000 1 20000000\n'], 'list',
        [('Nadia Bahrami', '10000', '5', '2000'),
            ('Joe McClenahan', '5000', '2', '2500'),
            ('Cris Ewing', '1000', '1', '1000'),
            ('John McLain', '55', '11', '5'),
            ('Bruce Wayne', '20000000', '1', '20000000')]),
    (['Nadia Bahrami:10000 5 2000\n',
        'Joe McClenahan:5000 2 2500\n',
        'Cris Ewing:1000 1 1000\n',
        'John McLain:55 11 5\n',
        'Bruce Wayne:20000000 1 20000000\n'], 'dictionary',
        {'Nadia Bahrami': ['10000', '5', '2000'],
         'John McLain': ['55', '11', '5'],
         'Joe McClenahan': ['5000', '2', '2500'],
         'Bruce Wayne': ['20000000', '1', '20000000'],
         'Cris Ewing': ['1000', '1', '1000']}),
]


SORT_TABLE = [
    ([('Nadia Bahrami', '10', '5', '2000'),
        ('Joe McClenahan', '5', '2', '2500'),
        ('Cris Ewing', '1000', '1', '1000'),
        ('John McLain', '55', '11', '5'),
        ('Bruce Wayne', '14', '1', '20000000')],
        [('Joe McClenahan', '5', '2', '2500'),
            ('Nadia Bahrami', '10', '5', '2000'),
            ('Bruce Wayne', '14', '1', '20000000'),
            ('John McLain', '55', '11', '5'),
            ('Cris Ewing', '1000', '1', '1000')]),
]


CALC_TABLE = [
    ([4, 1, 4], 2, [6, 2, 3]),
    ([9, 3, 3], 3, [12, 4, 3])
]


@pytest.mark.parametrize('lst, choice, result', DIC_TABLE)
def test_donor_list(lst, choice, result):
    from mailroom import donor_list
    assert donor_list(lst, choice) == result


@pytest.mark.parametrize('lst, result', SORT_TABLE)
def test_sorted_list(lst, result):
    from mailroom import sorted_list
    assert sorted_list(lst) == result


@pytest.mark.parametrize('donations, value, result', CALC_TABLE)
def test_calculation(donations, value, result):
    from mailroom import calculation
    assert calculation(donations, value) == result
