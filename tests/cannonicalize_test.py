import pytest
import main
import math


class Test_Canonicalize:
    @pytest.mark.parametrize(
        "input, expected, reason",
        [
            (1000, 1000.00, "no commas"),
            ("1000.500", 1000.5, "trailing decimal zeroes dropped"),
            ("1,000,000", 1000000.0, "handles commas"),
            ("1,0,,,00,000,,,.,,", 1000000.0, "very permissive about commas"),
            ("-InF", float("-inf"), "accepts negative Inf for non-mean uses"),
            ("iNf", float("inf"), "accepts Inf for non-mean uses"),
            (2 / 4, 0.5, "numeric fractions"),
        ],
    )
    def test_success(self, input, expected, reason):
        assert main.canonicalize(input) == expected

    def test_success_NaN_for_non_mean_uses(self):
        assert math.isnan(main.canonicalize("NAN"))

    @pytest.mark.parametrize(
        "input, expected, reason",
        [
            ("fffff", ValueError, "not numeric"),
        ],
    )
    def test_exception(self, input, expected, reason):
        with pytest.raises(expected):
            main.mean(input)
