import pytest
import main


class Test_Mean:
    @pytest.mark.parametrize(
        "input, expected, reason",
        [
            ((1, 2, -3), 0.0, "average of ints always results in float"),
            (("1,000,001", "999,999"), 1000000.0, "commas in input are ignored"),
            ((0, 2 / 3), 1 / 3, "numeric fractions"),
        ],
    )
    def test_success(self, input, expected, reason):
        assert main.mean(*input) == expected

    @pytest.mark.parametrize(
        "input, expected, reason",
        [
            ((-1, "Inf"), ValueError, "unexpected Inf"),
            (("NaN"), ValueError, "unexpected NaN"),
            ((), ValueError, "no input values, no mean"),
        ],
    )
    def test_exception(self, input, expected, reason):
        with pytest.raises(expected):
            main.mean(*input)
