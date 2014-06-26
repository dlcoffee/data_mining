def manhattan(rating1, rating2):
    '''
    computes manhattan distance. both rating1 and rating2 are dictionaries of
    of the form
    {'The Strokes': 3.0, 'Slightly Stoopid': 2.5 ....}
    '''

    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])

    return distance



def computeNearestNeighbor(username, users):
    '''
    creates a sorted list of users based on their distance to username
    '''

    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))

    # sort based on distance -- closest first
    distances.sort()
    return distances



def recommend(username, users):
    '''
    gives a list of recommendations
    '''

    # first find the nearest neighbor
    nearest = computeNearestNeighbor(username, users)[0][1]
    recommendations = []

    # now find bands the neighbor rated that the user didn't
    neighborRatings = users[nearest]
    userRatings = users[username]

    for artist in neighborRatings:
        if artist not in userRatings:
            recommendations.append((artist, neighborRatings[artist]))

    # using the fn sorted for variety -- sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

