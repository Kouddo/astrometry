from utility import average_fits, assert_similar, median_fits


def DarkGen(files):
    assert_similar(files)
    if integ == 'average':
        return average_fits(files)
    elif integ == 'median':
        return median_fits(files)
    else:
        raise Exception('Integration type must either be average or median')

