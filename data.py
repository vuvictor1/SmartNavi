"""********************************************************************************  
   Author Information:
   Kiara Guerra

   Other Authors: 

   Program Information:
   This File: data.py
   Description: Coordinates of each building used within the Graph Figure.
********************************************************************************"""  

# List of builiings and their names
buildings = ("Parking A", "Parking G", "Arboretum", "Children's Center", "Parking & Transportation Office",
             "A-South Parking", "Titan Sport Complex", "Housing Office", "Residence Halls", "Corporation Yard",
             "Titan House", "Ruby Gerontology Center", "Student Housing", "University Police", "State College Parking",
             "Student Rec Center", "Kinesiology/ Health Science", "Student Heath/ Counseling Center",
             "Engineering/ Computer Science", "Titan Student Union", "Parking E", "Becker Amphitheater",
             "Commons", "Pollak Library", "Education Classroom", "Parking I", "Visual Arts",
             "Clayes Performing Arts Center", "Quad", "Humanities/ Social Sciences", "Parking F", "Eastside Parking",
             "Greenhouse Complex", "McCarthy Hall", "University Hall", "Carl's Jr", "Langsdorf Hall", "Dan Black Hall",
             "Nutwood Parking", "Mihaylo Hall", "Parking C",

             # Added paths here

             "State 01", "State 02", "Corporate Drive 01", "WestCamp", "GymWest")

# Assign each building a coordinate with x and y values
coordinates = {

    # added path positions here
    "State 01": (7, 585),
    "State 02": (7, 435),
    "Corporate Drive 01":(70, 435),
    "WestCamp":(125, 435),
    "GymWest":(125, 360),



    "Parking A": (75, 585),
    "Parking G": (185, 650),
    "Arboretum": (350, 550),
    "Children's Center": (100, 490),
    "Parking & Transportation Office": (33, 470),
    "A-South Parking": (70, 470),
    "Titan Sport Complex": (215, 460),
    "Housing Office": (390, 500),
    "Residence Halls": (425, 500),
    "Corporation Yard": (60, 390),
    "Titan House": (295, 370),
    "Ruby Gerontology Center": (340, 360),
    "Student Housing": (390, 400),
    "University Police": (35, 320),
    "State College Parking": (75, 320),
    "Student Rec Center": (135, 320),
    "Kinesiology/ Health Science": (205, 320),
    "Student Heath/ Counseling Center": (300, 320),
    "Engineering/ Computer Science": (355, 280),
    "Titan Student Union": (80, 250),
    "Parking E": (420, 240),
    "Becker Amphitheater": (120, 205),
    "Commons": (180, 220),
    "Pollak Library": (230, 220),
    "Education Classroom": (290, 220),
    "Parking I": (350, 220),
    "Visual Arts": (60, 160),
    "Clayes Performing Arts Center": (175,160),
    "Quad": (230, 160),
    "Humanities/ Social Sciences": (290, 160),
    "Parking F": (360, 140),
    "Eastside Parking": (420, 140),
    "Greenhouse Complex": (175, 105),
    "McCarthy Hall": (225, 115),
    "University Hall": (290, 115),
    "Carl's Jr": (305, 90),
    "Langsdorf Hall": (280, 65),
    "Dan Black Hall": (225, 80),
    "Nutwood Parking": (70, 80),
    "Mihaylo Hall": (340, 50),
    "Parking C": (445, 50),
}