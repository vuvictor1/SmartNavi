"""********************************************************************************  
   Author Information:
   Victor Vu (vuvictor@csu.fullerton.edu)

   Other Authors: 

   Program Information:
   This File: main_navi.py
   Description: Manager for the SmartNavi GPS system. Calls BFS, DFS and Dijkstra's 
   Algorithm for pathfinding. Also incorporates GUI, utilizing a graph model.
********************************************************************************"""  
import gui  # Call the GUI file

# Main function for execution


def main():
    # Paths and Nodes
    adjacency_list = {

    # to edit with testing
        "Arboretum": {"Housing Office": 3, "Residence Halls": 2, "Titan Sport Complex": 4, "Ruby Gerontology Center": 6, "Titan House": 2},
        "A-South Parking": {"Parking A": 7, "Children's Center": 2, "Parking & Transportation Office": 1, "Corporate Drive 01": 1},
        "Becker Amphitheater": {"Visual Arts": 1.5, "Commons": 1, "Titan Student Union": 1,
                                "Clayes Performing Arts Center": 2, },
        "Carl's Jr": {"University Hall": 8, "Langsdorf Hall": 4},
        "Commons": {"Becker Amphitheater": 1, "Pollak Library": 3, "Student Rec Center": 2.5,
                    "Kinesiology/ Health Science": 2.5, "Clayes Performing Arts Center": 1.5},
        "Children's Center": {"A-South Parking": 1, "Parking A": 2},
        "Clayes Performing Arts Center": {"Visual Arts": 2, "Quad": 3, "Becker Amphitheater": 2, "Commons": 1.5},
        "Corporation Yard": {"Corporate Drive 01": 1,},
        "Dan Black Hall": {"Langsdorf Hall": 3, "Nutwood Parking Structure": 2},
        "Eastside Parking": {"Parking F": 1, "Parking E": 1, },
        "Education Classroom": {"Pollak Library": 2, "Parking I": 1, "Student Heath/ Counseling Center": 3,
                                "Kinesiology/ Health Science":2.5 },
        "Engineering/ Computer Science": {"Student Heath/ Counseling Center": 6, "Titan Student Union": 8,
                                          "Student Housing":2.5},
        "Golleher Alumni House": {"University Police": 1, "Titan Student Union": 1, "State College Parking":1,},
        "Greenhouse Complex": {"McCarthy Hall": 7},
        "Housing Office": {"Arboretum": 3, "Residence Halls": 2, "Ruby Gerontology Center": 6, "Student Housing": 2},
        "Humanities/ Social Sciences": {"Quad": 2, "Parking F": 3},
        "Kinesiology/ Health Science": {"Student Rec Center": 1, "Student Heath/ Counseling Center": 1.5,
                                        "Titan Student Union":2, "Pollak Library":1.5, "Commons":2.5,
                                        "Titan Sport Complex": 3, "Education Classroom": 2.5},
        "Langsdorf Hall": {"Carl's Jr": 4, "Dan Black Hall": 3},
        "McCarthy Hall": {"Greenhouse Complex": 7, "University Hall": 2},
        "Mihaylo Hall": {"Nutwood Parking Structure": 5, "Parking C": 4},
        "Nutwood Parking Structure": {"Dan Black Hall": 2, "Art 01": 1, "Parking C":1},
        "Parking A": {"A-South Parking": 1.5, "Parking & Transportation Office": 1.5, "Children's Center": 1.25},
        "Parking C": {"Mihaylo Hall": 3, "NutWood 01": .5, "Nutwood Parking Structure": 1},
        "Parking E": {"Eastside Parking": 1, "Parking I": 1},
        "Parking F": {"Humanities/ Social Sciences": 3, "Eastside Parking": 4,  "NutWood 02": 2, "Parking I":1},
        "Parking G": {"Yorba 01": 1,},
        "Parking I": {"Education Classroom": 1, "Visual Arts": 5, "Parking E": 1, "Parking F":1},
        "Parking & Transportation Office": {"Parking A": 2},
        "Pollak Library": {"Commons": 3, "Education Classroom": 2, "Kinesiology/ Health Science":1.5,
                           "Student Heath/ Counseling Center": 3.5,},
        "Quad": {"Clayes Performing Arts Center": 3, "Humanities/ Social Sciences": 2},
        "Residence Halls": {"Arboretum": 2, "Housing Office": 2, "Ruby Gerontology Center": 7},
        "Ruby Gerontology Center": {"Arboretum": 6, "Housing Office": 6, "Residence Halls": 7,
                                    "Titan Sport Complex": 5, "Student Housing": 1.5, },
        "State College Parking": {"University Police": 1,   "Student Rec Center": 1, "Golleher Alumni House":1, },
        "Student Heath/ Counseling Center": {"Kinesiology/ Health Science": 1.5, "Engineering/ Computer Science": 1.5,
                                             "Pollak Library": 3.5, "Education Classroom": 3},
        "Student Housing": {"Engineering/ Computer Science": 2.5, "Ruby Gerontology Center": 1.5, "Housing Office": 2,},
        "Student Rec Center": { "Kinesiology/ Health Science": 1, "State College Parking": 1, "Titan Student Union": 1.5,
                                "Commons":2.5},
        "Titan House": { "Arboretum": 2},
        "Titan Sport Complex": {"Parking A": 3, "Arboretum": 4, "Kinesiology/ Health Science": 3},
        "Titan Student Union": { "Golleher Alumni House": 1, "State College Parking": 1.5, "Student Rec Center": 1.5,
                                 "Visual Arts": 1, "Becker Amphitheater":1, "Kinesiology/ Health Science": 2, },
        "University Hall": {"McCarthy Hall": 2, "Carl's Jr": 8},
        "University Police": {"State College Parking": 1, "Golleher Alumni House": 1, },
        "Visual Arts": {"Parking I": 5, "Clayes Performing Arts Center": 2, "Art 01": 1, "Titan Student Union" :1,  "Becker Amphitheater":1.5,},


    # Additional Paths for traversals
    "Art 01": {"StateArt": 1, "Visual Arts": 1, "Nutwood Parking Structure": 1 },
    "Corporate Drive 01": {"State 02": 1, "Corporation Yard": 1,},
    "GymWest": {"WestCamp": 1, "Titan Sport Complex": 3, "Ruby Gerontology Center": 6},
    "Gym Drive 01": {"GymWest": 1, "State College Parking": 1, "Corporation Yard": 1},
    "GymState" : {"Gym Drive 01": 1, "State 02": 1},
    "NutWood 01": {"StateNut": 1, "Parking C":.5,},
    "NutWood 02": {"NutWood 01": 3, "Parking F":2},
    "State 01": {"Parking A": 1},
    "State 02": {"State 01": 1, "Corporate Drive 01": 1, "State 03": 1,},
    "State 03": {"Golleher Alumni House": 1, "State 02": 1, "State 04": 1,},
    "State 04": {"State 03": 1, "Titan Student Union": 2, "StateArt":2},
    "StateArt": {"State 04": 2,},
    "StateNut": {"StateArt": 1, "NutWood 01": 1,},
    "WestCamp": {"Corporate Drive 01": 1, "Titan Sport Complex": 3,},
    "Yorba 00" : {"Yorba 01": 1,},
    "Yorba 01" : {"Parking G": 1, "Yorba 02": .5},
    "Yorba 02" : {"Parking A": 2, "Yorba 01" :1,},
}
    # Accessibility list
    alt_list = {
    "Quad": {"Humanities/ Social Sciences": 2},  
    "Langsdorf Hall": {"Carl's Jr": 5},  
    "McCarthy Hall": {"University Hall": 3},  
    "Titan Student Union": {"Visual Arts": 1.5},
    }

    gui.show_gui(adjacency_list, alt_list) # pass adjacency list to the GUI

# Call main
if __name__ == "__main__":
    main()