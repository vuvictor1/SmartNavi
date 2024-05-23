"""********************************************************************************  
   Author Information:
   Kiara Guerra

   Other Authors: Victor Vu and Robert Petersen

   Program Information:
   This File: data.py
   Description: Hold coordinates of each building used within the Graph Figure.
   
   Copyright (C) 2024 Victor V. Vu, Kirara Guerra and Robert Petersen
   This program is free software: you can redistribute it and/or modify it under
   the terms of the GNU General Public License version 3 as published by the
   Free Software Foundation. This program is distributed in the hope that it
   will be useful, but WITHOUT ANY WARRANTY without even the implied Warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
   Public License for more details. A copy of the GNU General Public License v3
   is available here: <https://www.gnu.org/licenses/>.
********************************************************************************"""

# List of builiings and their names
buildings = (
    # All buildings
    "A-South Parking",
    "Arboretum",
    "Becker Amphitheater",
    "Carl's Jr",
    "Children's Center",
    "Clayes Performing Arts Center",
    "Commons",
    "Corporation Yard",
    "Dan Black Hall",
    "Eastside Parking",
    "Education Classroom",
    "Engineering/ Computer Science",
    "Golleher Alumni House",
    "Greenhouse Complex",
    "Housing Office",
    "Humanities/ Social Sciences",
    "Kinesiology/ Health Science",
    "Langsdorf Hall",
    "McCarthy Hall",
    "Mihaylo Hall",
    "Nutwood Parking Structure",
    "Parking A",
    "Parking C",
    "Parking E",
    "Parking F",
    "Parking G",
    "Parking I",
    "Parking & Transportation Office",
    "Pollak Library",
    "Quad",
    "Residence Halls",
    "State College Parking",
    "Student Heath/ Counseling Center",
    "Student Housing",
    "Titan House",
    "Titan Sport Complex",
    "University Police",
    "Ruby Gerontology Center",
    "Student Rec Center",
    "Titan Student Union",
    "University Hall",
    "Visual Arts",

    # Added paths here, to have hidden
    "-----------Paths---------",
    "Art 01",
    "Corporate Drive 01",
    "Gym Drive 01",
    "GymState",
    "GymWest",
    "NutWood 01",
    "NutWood 02",
    "State 01",
    "State 02",
    "State 03",
    "State 04",
    "StateArt",
    "StateNut",
    "WestCamp",
    "Yorba 00",
    "Yorba 01",
    "Yorba 02",
)

# Assign each building a coordinate with x and y values
coordinates = {
    "Arboretum": (350, 550),
    "A-South Parking": (70, 470),
    "Becker Amphitheater": (120, 205),
    "Carl's Jr": (305, 90),
    "Children's Center": (100, 490),
    "Clayes Performing Arts Center": (175, 160),
    "Commons": (180, 220),
    "Corporation Yard": (70, 390),
    "Dan Black Hall": (225, 80),
    "Eastside Parking": (420, 140),
    "Education Classroom": (290, 220),
    "Engineering/ Computer Science": (355, 280),
    "Golleher Alumni House": (35, 280),
    "Greenhouse Complex": (175, 105),
    "Housing Office": (390, 500),
    "Humanities/ Social Sciences": (290, 160),
    "Kinesiology/ Health Science": (205, 320),
    "Langsdorf Hall": (280, 65),
    "McCarthy Hall": (225, 115),
    "Mihaylo Hall": (340, 50),
    "Nutwood Parking Structure": (70, 80),
    "Parking & Transportation Office": (33, 470),
    "Parking A": (75, 585),
    "Parking C": (125, 35),
    "Parking E": (420, 240),
    "Parking F": (375, 140),
    "Parking G": (185, 650),
    "Parking I": (350, 220),
    "Pollak Library": (230, 220),
    "Quad": (230, 160),
    "Residence Halls": (425, 500),
    "Ruby Gerontology Center": (340, 360),
    "State College Parking": (75, 320),
    "Student Heath/ Counseling Center": (300, 320),
    "Student Housing": (390, 400),
    "Student Rec Center": (135, 320),
    "Titan House": (295, 370),
    "Titan Sport Complex": (215, 460),
    "Titan Student Union": (80, 250),
    "University Hall": (290, 115),
    "University Police": (35, 320),
    "Visual Arts": (60, 160),

    # Added path positions here
    "-----------Paths---------": (75, 110),
    "Art 01": (75, 110),
    "NutWood 01": (125, 15),
    "NutWood 02": (375, 15),
    "State 01": (7, 585),
    "State 02": (7, 435),
    "State 03": (7, 280),
    "State 04": (7, 250),
    "StateArt": (7, 110),
    "StateNut": (7, 15),
    "Corporate Drive 01": (70, 435),
    "GymWest": (125, 360),
    "Gym Drive 01": (70, 360),
    "GymState": (7, 360),
    "WestCamp": (125, 435),
    "Yorba 00": (140, 690),
    "Yorba 01": (140, 650),
    "Yorba 02": (140, 620),

}

# Accessibility list
alt_buildings = (
    # All buildings
    "A-South Parking",
    "Arboretum",
    "Becker Amphitheater",
    "Carl's Jr",
    "Children's Center",
    "Clayes Performing Arts Center",
    "Commons",
    "Corporation Yard",
    "Dan Black Hall",
    "Eastside Parking",
    "Education Classroom",
    "Engineering/ Computer Science",
    "Golleher Alumni House",
    "Greenhouse Complex",
    "Housing Office",
    "Humanities/ Social Sciences",
    "Kinesiology/ Health Science",
    "Langsdorf Hall",
    "McCarthy Hall",
    "Mihaylo Hall",
    "Nutwood Parking Structure",
    "Parking C",
    "Parking E",
    "Parking F",
    "Parking I",
    "Pollak Library",
    "Quad",
    "Residence Halls",
    "State College Parking",
    "Student Heath/ Counseling Center",
    "Student Housing",
    "Titan House",
    "Titan Sport Complex",
    "University Police",
    "Ruby Gerontology Center",
    "Student Rec Center",
    "Titan Student Union",
    "University Hall",
    "Visual Arts",

    # Added paths here, to have hidden
    "-----------Paths---------",
    "Art 01",
    "Corporate Drive 01",
    "Gym Drive 01",
    "GymState",
    "GymWest",
    "NutWood 01",
    "NutWood 02",
    "State 02",
    "State 03",
    "State 04",
    "StateArt",
    "StateNut",
    "WestCamp",
)

# Coordinates for the alt list buildings
alt_coordinates = {
    "Arboretum": (350, 550),
    "A-South Parking": (70, 470),
    "Becker Amphitheater": (120, 205),
    "Carl's Jr": (305, 90),
    "Children's Center": (100, 490),
    "Clayes Performing Arts Center": (175, 160),
    "Commons": (180, 220),
    "Corporation Yard": (70, 390),
    "Dan Black Hall": (225, 80),
    "Eastside Parking": (420, 140),
    "Education Classroom": (290, 220),
    "Engineering/ Computer Science": (355, 280),
    "Golleher Alumni House": (35, 280),
    "Greenhouse Complex": (175, 105),
    "Housing Office": (390, 500),
    "Humanities/ Social Sciences": (290, 160),
    "Kinesiology/ Health Science": (205, 320),
    "Langsdorf Hall": (280, 65),
    "McCarthy Hall": (225, 115),
    "Mihaylo Hall": (340, 50),
    "Nutwood Parking Structure": (70, 80),
    "Parking C": (125, 35),
    "Parking E": (420, 240),
    "Parking F": (375, 140),
    "Parking I": (350, 220),
    "Pollak Library": (230, 220),
    "Quad": (230, 160),
    "Residence Halls": (425, 500),
    "Ruby Gerontology Center": (340, 360),
    "State College Parking": (75, 320),
    "Student Heath/ Counseling Center": (300, 320),
    "Student Housing": (390, 400),
    "Student Rec Center": (135, 320),
    "Titan House": (295, 370),
    "Titan Sport Complex": (215, 460),
    "Titan Student Union": (80, 250),
    "University Hall": (290, 115),
    "University Police": (35, 320),
    "Visual Arts": (60, 160),

    # Added path positions here
    "-----------Paths---------": (75, 110),
    "Art 01": (75, 110),
    "NutWood 01": (125, 15),
    "NutWood 02": (375, 15),
    "State 02": (7, 435),
    "State 03": (7, 280),
    "State 04": (7, 250),
    "StateArt": (7, 110),
    "StateNut": (7, 15),
    "Corporate Drive 01": (70, 435),
    "GymWest": (125, 360),
    "Gym Drive 01": (70, 360),
    "GymState": (7, 360),
    "WestCamp": (125, 435),
}