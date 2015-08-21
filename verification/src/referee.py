from checkio_referee import RefereeBase
from checkio_referee import covercodes, validators, representations, ENV_NAME


import settings_env
from tests import TESTS

Result = validators.ValidatorResult


class MindSwitcherValidator(validators.BaseValidator):

    def validate(self, result):
        if (not isinstance(result, list) or
                any(not isinstance(x, list) or len(x) != 2 for x in result)):
            return Result(False, "TypeError. Please, read Input-Output format")
        data = self._test.get("input", [])
        robots = {"a1": "a1", "t2": "t2"}
        switched = []
        for pair in data:
            switched.append(set(pair))
            r1, r2 = pair
            robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)

        for pair in result:
            if len(pair) != 2:
                return Result(False, "Each pair should contain exactly two names.")
            r1, r2 = pair
            if not isinstance(r1, str) or not isinstance(r2, str):
                return Result(False, "Names must be strings.")
            if r1 not in robots.keys():
                return Result(False, "I don't know '{}'.".format(r1))
            if r2 not in robots.keys():
                return Result(False, "I don't know '{}'.".format(r2))
            if set(pair) in switched:
                return Result(False, "'{}' and '{}' already were switched.".format(r1, r2))
            switched.append(set(pair))
            robots[r1], robots[r2] = robots[r2], robots[r1]
        for body, mind in robots.items():
            if body != mind:
                return Result(False, "'{}' has '{}' mind.".format(body, mind))
        return Result(True,  "Great!")


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    VALIDATOR = MindSwitcherValidator
    DEFAULT_FUNCTION_NAME = "mind_switcher"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "mindSwitcher"
    }
