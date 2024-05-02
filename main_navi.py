"""********************************************************************************  
   Author Information:
   Victor Vu (vuvictor@csu.fullerton.edu)

   Other Authors: 

   Program Information:
   This File: main_navi.py
   Description: Manager for the SmartNavi GPS system. Calls BFS, DFS and Dijkstra's 
   Algorithm for pathfinding. Also incorporates GUI, utilizing a graph model.
********************************************************************************"""  
import gui # Call the GUI file

# Main function for execution
def main():
    # Placeholder list (will need to rely on Robert's graph model) ---------------------------------------- important!!!!
    adjacency_list = {
    "Parking A": {"Parking G": 5, "Titan Sport Complex": 3, "Parking & Transportation Office": 2, "A-South Parking": 7, "Children's Center": 8},
    "Parking G": {"Parking A": 5, "Titan Sport Complex": 2, "Parking & Transportation Office": 9},
    "Arboretum": {"Housing Office": 3, "Residence Halls": 2, "Titan Sport Complex": 4, "Ruby Gerontology Center": 6, "Titan House": 2},
    "Children's Center": {"A-South Parking": 2, "Parking & Transportation Office": 6, "Parking A": 8},
    "Parking & Transportation Office": {"Parking A": 2, "Parking G": 9, "Children's Center": 6},
    "A-South Parking": {"Parking A": 7, "Children's Center": 2, "Parking & Transportation Office": 1},
    "Titan Sport Complex": {"Parking A": 3, "Parking G": 2, "Arboretum": 4},
    "Housing Office": {"Arboretum": 3, "Residence Halls": 2, "Ruby Gerontology Center": 6},
    "Residence Halls": {"Arboretum": 2, "Housing Office": 2, "Ruby Gerontology Center": 7},
    "Corporation Yard": {"Titan House": 8, "University Police": 3},
    "Titan House": {"Corporation Yard": 8, "University Police": 9, "Arboretum": 2},
    "Ruby Gerontology Center": {"Arboretum": 6, "Housing Office": 6, "Residence Halls": 7},
    "Student Housing": {"University Police": 1, "State College Parking": 3},
    "University Police": {"Student Housing": 1, "State College Parking": 1, "Corporation Yard": 3},
    "State College Parking": {"Student Housing": 3, "University Police": 1, "Student Rec Center": 5},
    "Student Rec Center": {"State College Parking": 5, "Kinesiology/ Health Science": 4},
    "Kinesiology/ Health Science": {"Student Rec Center": 4, "Student Heath/ Counseling Center": 5},
    "Student Heath/ Counseling Center": {"Kinesiology/ Health Science": 5, "Engineering/ Computer Science": 6},
    "Engineering/ Computer Science": {"Student Heath/ Counseling Center": 6, "Titan Student Union": 8},
    "Titan Student Union": {"Engineering/ Computer Science": 8, "Parking E": 2},
    "Parking E": {"Titan Student Union": 2, "Becker Amphitheater": 4},
    "Becker Amphitheater": {"Parking E": 4, "Commons": 1},
    "Commons": {"Becker Amphitheater": 1, "Pollak Library": 3},
    "Pollak Library": {"Commons": 3, "Education Classroom": 2},
    "Education Classroom": {"Pollak Library": 2, "Parking I": 1},
    "Parking I": {"Education Classroom": 1, "Visual Arts": 5},
    "Visual Arts": {"Parking I": 5, "Clayes Performing Arts Center": 2},
    "Clayes Performing Arts Center": {"Visual Arts": 2, "Quad": 3},
    "Quad": {"Clayes Performing Arts Center": 3, "Humanities/ Social Sciences": 2},
    "Humanities/ Social Sciences": {"Quad": 2, "Parking F": 3},
    "Parking F": {"Humanities/ Social Sciences": 3, "Eastside Parking": 4},
    "Eastside Parking": {"Parking F": 4, "Greenhouse Complex": 6},
    "Greenhouse Complex": {"Eastside Parking": 6, "McCarthy Hall": 7},
    "McCarthy Hall": {"Greenhouse Complex": 7, "University Hall": 2},
    "University Hall": {"McCarthy Hall": 2, "Carl's Jr": 8},
    "Carl's Jr": {"University Hall": 8, "Langsdorf Hall": 4},
    "Langsdorf Hall": {"Carl's Jr": 4, "Dan Black Hall": 3},
    "Dan Black Hall": {"Langsdorf Hall": 3, "Nutwood Parking": 2},
    "Nutwood Parking": {"Dan Black Hall": 2, "Mihaylo Hall": 5},
    "Mihaylo Hall": {"Nutwood Parking": 5, "Parking C": 4},
    "Parking C": {"Mihaylo Hall": 4},
}
    
    gui.show_gui(adjacency_list) # pass adjacency list to the GUI

# Call main
if __name__ == "__main__":
    main()