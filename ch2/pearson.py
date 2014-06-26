from math import sqrt

def pearson(rating1, rating2):
    '''
    calculates the pearson coefficient of two dictionaries of ratings
    '''

    sum_xy = 0
    sum_xx = 0
    sum_yy = 0
    sum_x = 0
    sum_y = 0
    n = 0 # number of co-rated items

    for key in rating1:
        if key in rating2:
            n += 1

            sum_xy += rating1[key] * rating2[key]
            sum_x += rating1[key]
            sum_y += rating2[key]
            sum_xx += rating1[key]**2
            sum_yy += rating2[key]**2

    denominator =  (sqrt(sum_xx - (sum_x**2)/n) * sqrt(sum_yy - (sum_y**2)/n))

    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y)/n) / denominator

