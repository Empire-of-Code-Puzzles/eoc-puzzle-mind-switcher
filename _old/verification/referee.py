from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS


cover = """
def cover(f, data):
    fdata = tuple(set(s) for s in data)
    result = f(fdata)
    if not isinstance(result, (list, tuple)) or not all(isinstance(p, set) for p in result):
        raise TypeError("The result should be a list/tuple of sets.")
    return [list(p) for p in result], str(result)
"""


def checker(data, from_cover):
    result, str_result = from_cover
    robots = {"nikola": "nikola", "sophia": "sophia"}
    switched = []
    for pair in data:
        switched.append(set(pair))
        r1, r2 = pair
        robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)

    for pair in result:
        if len(pair) != 2:
            return False, (1, "Each pair should contain exactly two names.", str_result)
        r1, r2 = pair
        if not isinstance(r1, str) or not isinstance(r2, str):
            return False, (2, "Names must be strings.", str_result)
        if r1 not in robots.keys():
            return False, (3, "I don't know '{}'.".format(r1), str_result)
        if r2 not in robots.keys():
            return False, (3, "I don't know '{}'.".format(r2), str_result)
        if set(pair) in switched:
            return False, (4, "'{}' and '{}' already were switched.".format(r1, r2), str_result)
        switched.append(set(pair))
        robots[r1], robots[r2] = robots[r2], robots[r1]
    for body, mind in robots.items():
        if body != mind:
            return False, (10, "'{}' has '{}' mind.".format(body, mind), str_result)
    return True, (100, "Great!", str_result)


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': cover,  # or None
            'python-3': cover
        },
        checker=checker,
        function_name="mind_switcher"
    ).on_ready)
