SCENARII = {
    "quest-dokkan-story": [
        "assets/buttons/start.jpg",
        "assets/buttons/ok.jpg",
        "assets/buttons/close.jpg",
        "assets/buttons/rank-up.jpg",
        "assets/buttons/ds.jpg",
        "assets/buttons/act-super-2.jpg",
        "assets/buttons/act-super.jpg",
        "assets/buttons/new.jpg",        
        "assets/buttons/home-start.jpg",
        "assets/buttons/touch-start.jpg",
        "assets/buttons/warning.jpg",
    ],
    "event": {
        "awaken": {
            "le-malefique-empereur-de-l-univers": {
                "3-derniere-puissance-maximale-de-freezer": [
                    "assets/buttons/are-you-sure.jpg",
                    "assets/buttons/restart.jpg",
                    "assets/buttons/start.jpg",
                    "assets/buttons/ok.jpg",
                    "assets/buttons/close.jpg",
                    "assets/buttons/rank-up.jpg",
                    "assets/buttons/ds.jpg",            
                    "assets/buttons/act-super-2.jpg",           
                    "assets/buttons/act-super.jpg",
                    "assets/buttons/3-derniere-puissance-maximale-de-freezer.jpg",
                    "assets/buttons/event-le-malefique-empereur-de-l-univers.jpg",
                    "assets/buttons/awaken.jpg",
                    "assets/buttons/event.jpg",            
                    "assets/buttons/home-start.jpg",
                    "assets/buttons/touch-start.jpg",            
                    "assets/buttons/warning.jpg",                   
                ]
            }
        }
    }
}

def select_scenario(scenarios):
    if isinstance(scenarios, list):
        return scenarios

    print("Available options:")
    for i, key in enumerate(scenarios.keys(), 1):
        print(f"{i}. {key}")
    
    choice = int(input("Select an option by number: "))
    selected_key = list(scenarios.keys())[choice - 1]
    
    return select_scenario(scenarios[selected_key])
