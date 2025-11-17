def calc_aqi_level(concentration, intervals):
    concentration = float(concentration)

    for level, high in intervals:
        if concentration <= high:
            return level

    # if nothing matches return highest level
    return intervals[-1][0]
