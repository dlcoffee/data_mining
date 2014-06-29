import math

users3 = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Matt":  {"Imagine Dragons": 3, "Daft Punk": 4,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Ben":   {"Kacey Musgraves": 4, "Imagine Dragons": 3,
                    "Lorde": 3, "Fall Out Boy": 1},
          "Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
                    "Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
          "Tori":  {"Kacey Musgraves": 5, "Imagine Dragons": 4,
                    "Daft Punk": 5, "Fall Out Boy": 3}}    



def computeSimilarity(band1, band2, userRatings):
    '''
    calculates adjusted cosine similiarity. we compensate for grade inflation
    by subtracting the user's average rating from each rating

    adjusted cosine similarity is a model-based collaborative filtering method
    an advantage is that these methods scale better. for large data sets
    they tend to be fast and require less memory

    userRatings is a dictionary of the form: {'User': {'band1': rating, ...}}
    '''

    averages = {} # dictionary, where key is user and value is average rating
    for (key, ratings) in userRatings.items():
        averages[key] = (float(sum(ratings.values()))
                        / len(ratings.values()))

    num = 0
    den1 = 0
    den2 = 0

    for (user, ratings) in userRatings.items():
        if band1 in ratings and band2 in ratings:
            avg = averages[user]
            num += (ratings[band1] - avg) * (ratings[band2] - avg)
            den1 += (ratings[band1] - avg) ** 2
            den2 += (ratings[band2] - avg) ** 2

    den = (math.sqrt(den1) * math.sqrt(den2))
    
    if den != 0:
        return num / den
    else:
        return 0 



def normalize(rating)
    '''
    helper method to normalize a rating from a scale of 1 to 5 to
    a scale of -1 to 1
    '''
    min_r = 1
    max_r = 5

    return (2*(rating - min_r) - (max_r - min_r))/(max_r - min_r)


def denormalize(rating)
    '''
    helper method tode normalize a rating from a scale of -1 to 1 to
    a scale of 1 to 5
    '''
    min_r = 1
    max_r = 5

    return .5*((rating + 1)*(max_r - min_r)) + min_r


def predictRating(user, band, userRatings):
   '''
    predicts what rating a user might gave a band

    we normalize ratings from an initial scale of 1 to 5 to -1 to 1 

    userRatings is a dictionary of the form: {'User': {'band1': rating, ...}}
    '''

    num = 0
    den = 0   
 
    for (user, ratings) in userRatings.items():
        num += 


