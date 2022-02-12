'''
Matthew Arras and Bjorn Soriano
CSE 163 Winter Quarter
Modules contains functions that test the quality
of the data scraping done in data_prep
'''
import data_prep
import math


def check_approx_equals(expected, received):
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    try:
        if type(expected) == dict:
            # first check that keys match, then check that the
            # values approximately match
            return expected.keys() == received.keys() and \
                all([check_approx_equals(expected[k], received[k])
                    for k in expected.keys()])
        elif type(expected) == list or type(expected) == set:
            # Checks both lists/sets contain the same values
            return len(expected) == len(received) and \
                all([check_approx_equals(v1, v2)
                    for v1, v2 in zip(expected, received)])
        elif type(expected) == float:
            return math.isclose(expected, received, abs_tol=0.001)
        else:
            return expected == received
    except Exception as e:
        print(f'EXCEPTION: Raised when checking check_approx_equals {e}')
        return False


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    assert check_approx_equals(expected, received), \
        f'Failed: Expected {expected}, but received {received}'


def test_rstats(r_stats18, r_stats19):
    '''
    Takes in dataframes that contain traditional statistics, and performs
    checks on their dimensions and values to ensure that their data has
    been properly scraped from the web
    '''
    # Row count check
    assert_equals(30, len(r_stats18['Team']))
    assert_equals(30, len(r_stats19['Team']))

    # Column count check
    assert_equals(24, len(r_stats19.columns))
    assert_equals(24, len(r_stats19.columns))

    # 18 data spot checks
    # should be OKC Thunders 3P Field Goals per game
    # Note original dataset wasn't 0 indexed so we add one
    # IE: Thunder were at 7, subtract one for 6
    assert_equals(11.4, r_stats18.loc[6, '3P'])

    # Should Be Boston Celtic total rebounds per game
    assert_equals(44.5, r_stats18.loc[13, 'TRB'])

    # 19 data spot checks
    # Should be Utah Jazz three point percentage per game
    assert_equals(.380, r_stats19.loc[17, '3P%'])

    # Should be Utah Jazz free throw attempts per game
    assert_equals(22.8, r_stats19.loc[17, 'FTA'])


def test_astats(a_stats18, a_stats19):
    '''
    Takes in dataframes that contain advanced statistics, and performs
    checks on their dimensions and values to ensure that their data has
    been properly scraped from the web
    '''
    # Num rows check
    assert_equals(30, len(a_stats18['Team']))
    assert_equals(30, len(a_stats19['Team']))

    # Num columns check
    assert_equals(14, len(a_stats18.columns))
    assert_equals(14, len(a_stats19.columns))

    # 18 spot checks
    # Bucks pace
    assert_equals(103.3, a_stats18.loc[0, 'Pace'])

    # Magic Effective FG%
    assert_equals(.518, a_stats18.loc[13, 'eFG%'])

    # 19 data spot checks

    # Bulls offensive rating
    assert_equals(106.7, a_stats19.loc[21, 'ORtg'])

    # Warriors Three point attempt rate
    assert_equals(.355, a_stats19.loc[29, '3PAr'])

    assert_equals(str, type(a_stats18.loc[16, 'Team']))
    assert_equals(str, type(a_stats19.loc[4, 'Team']))


def main():
    r18url = 'https://www.basketball-reference.com/leagues/NBA_2019.html'
    r19url = 'https://www.basketball-reference.com/leagues/NBA_2020.html'
    r_stats18 = data_prep.scrape_regular(r18url)
    r_stats19 = data_prep.scrape_regular(r19url)

    a18url = 'https://www.basketball-reference.com/leagues/NBA_2019.html'
    a19url = 'https://www.basketball-reference.com/leagues/NBA_2020.html'
    a_stats18 = data_prep.scrape_advanced(a18url)
    a_stats19 = data_prep.scrape_advanced(a19url)

    test_rstats(r_stats18, r_stats19)
    test_astats(a_stats18, a_stats19)


if __name__ == '__main__':
    main()
