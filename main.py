import math

# canonicalize() takes an imput and returns a canonicalized numerical value
# if the input is a string, it tries to be friendly and accept US-formatting
#
# Periods are assumed as the "decimal separator"
# Commas can optionally be used as "thousands separator" and are merely ignored
# So we can pasrse US-style 10,000.45 as 10000.45
# but not German-style 10.000,45 which will be misinterpreted as 10.00045
#
# anything that fails coercion into a float will raise
#
# I broke this out because:
# 1) if there are additional numerical list functions, they'll want to use this, too,
# 2) if we wanted to generalize it to handle non-USian formats, it should be broken out,
# 3) this is get-to-know-me code and writing just one function seemed like too little
def canonicalize(input):
    if isinstance(input, str):
        return float(input.replace(",", ""))
    return float(input)


# mean() takes variable-length inputs
# and returns their mean
#
# it calls canoonicalize() to turn inputs to a floats
# and also throws on nan, inf, and -inf
def mean(*inputs):
    if len(inputs) < 1:
        raise ValueError("at least one input value required")
    result = 0
    for input in inputs:
        value = canonicalize(input)
        if math.isnan(value) or math.isinf(value):
            raise ValueError(f"unhandled value: {input}")
        result += value / len(inputs)
    return result
