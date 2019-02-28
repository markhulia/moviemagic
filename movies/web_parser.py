import requests
"""
/search/title?title=The+Godfather&title_type=feature,tv_movie,tv_series,short&release_date=1985-01-01,2019-12-31&user_rating=1.0,10.0&num_votes=1,10000000&genres=action,adventure,animation,biography,comedy,crime,documentary,drama,family,fantasy,film-noir,game-show,history,horror,music,musical,mystery,news,reality-tv,romance,sci-fi,sport,talk-show,thriller,war,western
"""

BASE_URL = ""

r = requests.get(BASE_URL)


"""
User Stories:

1. User hits "Find" without any filters
    - System selects a random amount of filters (e.g. range(1, amount(filters))) 
    - System assigns a random value for each filter (e.g. range(min_val, max_val))
    - System retrieves all results and stores tha number of results from html tag
    - Number of results is divided by number of results per page to determine number of pages
    - Random page is selected and system redirects to the specific page
    - Random movie is retrieved from the page and displayed to user
    
2. User hits "Find" with specified filters
    - System retrieves all results with specified filter and stores the number of results from html tag
    == Sub-flow from user-story 1 ==  

"""
