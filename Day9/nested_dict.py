#nesting dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "stuttgart"], "total_visits": 5},
}

#nesting dictionary in a list
travel_log = [
    {
        "country" : "France",
        "cities_visited": ["paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country" : "Germany",
        "cities_visited": ["Berlin", "Hamburg", "stuttgart"],
        "total_visits": 5,
    },
]