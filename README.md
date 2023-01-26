# itential-take-home

## dev code
For lack of a better idea, the dev code is in main.py.

`mean()` takes a variable number of number args and returns their average.

Note: this also works on one arg, even though the assignment was 2 or more. I raise on 0 args.

### input: accepted
It handles numeric types and the helper function `canonicalize()` also handles strings (optionally with commas), converting to numerical.

It also handles anything coerced into a number (truthy values). I didn't bother filtering those out.

### input: raise ValueError
It raises on "spelled out" numbers ("forty-seven thousand six and thirty-two hundredths") because that seems hard and I am lazy. Likewise, no Roman numerals. But those were potentially in scope, too.

It raises on string fractions, either words ("one third") or numeric strings ("1/3").

It raises on no input. There's nothing to average.

It raises on NaN and -Inf and Inf, even when only given one argument.

## tests
First install, then run pytest:

    pipenv install
    pipenv run pytest

If you don't use pipenv, you can:

    pip install -r requirements.txt
    pytest

It outputs to the CLI and also drops result.xml, a JUnit-style XML results file suitable for CI tools.

I don't entirely like the way the results look, but it's the most RSpec-like I've been able to manage with Pytest parameterized tests, passing a partial test description string as one of the parameters so that it shows up in the pspec results. Well . . . without putting [something like this](https://stackoverflow.com/a/69107395) in a conftest.py, I mean, and that seemed too much for this exercise.

It also outputs coverage, including [htmlcov/index.html](htmlcov/index.html) (live link on local machine after running tests) if you'd like to check that.

## out of scope
I didn't run tests or gate merges on coverage percent on GitHub with GH Actions.