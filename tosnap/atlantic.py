from sectionate import (
    Section, join_sections
)

atlantic_sections = {
    "Western Europe": Section("Western Europe", [
        ( 009.0, 48.0),
        ( 015.0, 51.0),
        ( 022.0, 49.0),
        ( 035.0, 60.0),
    ]),
    "Bering Strait": Section("Bering Strait", [
        ( 055.0, 55.0),
        (-290.0, 55.0),
        (-225.0, 65.0),
        (-190.0, 65.5),
        (-185.0, 67.0),
        (-180.0, 67.5),
        (-175.0, 66.0),
        (-170.0, 66.0),
        (-165.0, 65.5),
        (-150.0, 65.5),
        (-130.0, 65.5),
        (-100.0, 50.0),
        (-090.0, 45.0),
    ]),
    "Fram Strait": Section("Fram Strait", [
        (-44.0, 69.0),
        (-30.0, 78.0),
        (-22.0, 79.0),
        ( 14.3, 79.0),
        ( 28.5, 70.0),
        ( 29.5, 66.0),
        ( 35.0, 60.0),
    ]),
    "Davis Strait": Section("Davis Strait", [
        (-65.0, 53.0),
        (-65.0, 57.5),
        (-62.0, 66.5),
        (-50.0, 66.5),
        (-47.5, 66.5),
        (-44.0, 69.0),
    ]),
    "Denmark Strait": Section("Denmark Strait", [
        (-44, 69),
        (-35, 69),
        (-25, 65),
        (-20, 65)
    ]),
    "Faroe Current": Section("Faroe Current", [
        (-14.00, 65.00),
        (- 6.25, 62.25)
    ]),
    "Faroe Bank": Section("Faroe Bank", [
        (-6.25, 62.25),
        (-8.00, 61.00),
        (-3.00, 58.50),
        (-5.00, 56.75),
    ]),
    "OSNAP West": Section("OSNAP West", [
        (-58, 52),
        (-51, 52.5),
        (-49, 54),
        (-48, 58.5),
        (-45, 60.5),
        (-44, 64.0),
    ]),
    "OSNAP East": Section("OSNAP East", [
        (-44, 64.0),
        (-42, 60.5),
        (-31, 59.0),
        (-28., 58.25),
        (-15, 58.0),
        (-12.5, 57.5),
        (-9.5, 57.25),
        (-5., 56.75)
    ]),
    "English Channel": Section("English Channel", [
        (0.0, 51.0),
        (0.0, 49.0),
        (2.5, 47.5)
    ]),
    "NOAC 47N": Section("NOAC 47N", [
        (-58.0, 52.0),
        (-56.5, 48.25),
        (-50.0, 47.00),
        (-12.0, 47.5),
        (  2.5, 47.5)
    ]),
    "Strait of Gibraltar": Section("Strait of Gibraltar", [
        (-4.00, 38.0),
        (-5.75, 36.5),
        (-5.75, 35.5),
        (-4.00, 34.0)
    ]),
    "RAPID 26N": Section("RAPID 26N", [
        (-90.0,  40.),
        (-80.0,  34.),
        (-80.0,  26.),
        (-72.0,  26.),
        (-49.0,  25.),
        (-41.0,  24.75),
        (-24.0,  24.5),
        (-21.5,  25.5),
        (-16.5,  27.0),
        (-10.0,  28.5),
        (- 5.0,  28.5),
        (- 4.0,  28.5),
    ]),
    "Quebec": Section("Quebec", [
        (-80.0,  47.5),
        (-75.0,  50.0),
        (-70.0,  53.0),
        (-65.0,  53.0)
    ]),
    "MOVE 16N": Section("MOVE 16N", [
        (-61.5, 0.),
        (-61.5, 8.),
        (-61.5, 16.75),
        (-51.5, 16.),
        (-12.,  16.),
        ( 20.,  16.),
    ]),
    "Isthmus of Panama": Section("Isthmus of Panama", [
        (-105.0,  40.0),
        (-105.0,  22.0),
        (- 98.0,  19.0),
        (- 95.0,  17.3),
        (- 92.0,  17.3),
        (- 91.0,  16.5),
        (- 90.0,  15.0),
        (- 87.0,  14.5),
        (- 85.0,  12.5),
        (- 84.8,  11.0),
        (- 83.8,  10.0),
        (- 83.0,   9.2),
        (- 82.0,   8.7),
        (- 81.0,   8.3),
        (- 80.0,   9.0),
        (- 79.4,   9.3),
        (- 78.8,   9.2),
        (- 78.0,   8.8),
        (- 77.0,   7.0),
        (- 71.0,   0.0)
    ]),
    "11S": Section("11S", [
        (-55., -9),
        (-37., -9),
        (-34., -11),
        ( 15., -11),
        ( 25., -11),
    ]),
    "SAMBA": Section("SAMBA", [
        (-55.0, -20.0),
        (-55.0, -34.5),
        ( 19.5, -34.5),
        ( 25.0, -20.0)
    ])
}

atlantic_region_boundaries = [
    join_sections(
        "South Atlantic",
        atlantic_sections["SAMBA"],
        atlantic_sections["11S"],
    ),
    join_sections(
        "Tropical Atlantic",
        atlantic_sections["11S"],
        atlantic_sections["MOVE 16N"],
    ),
    join_sections(
        "Gulf of Mexico",
        atlantic_sections["MOVE 16N"],
        atlantic_sections["Isthmus of Panama"],
        atlantic_sections["RAPID 26N"]
    ),
    join_sections(
        "Subtropical North Atlantic",
        atlantic_sections["RAPID 26N"],
        atlantic_sections["Quebec"],
        atlantic_sections["NOAC 47N"]
    ),
    join_sections(
        "Subpolar North Atlantic",
        atlantic_sections["NOAC 47N"],
        atlantic_sections["OSNAP West"],
        atlantic_sections["OSNAP East"],
        atlantic_sections["English Channel"]
    ),
    join_sections(
        "Labrador Sea",
        atlantic_sections["Davis Strait"],
        atlantic_sections["OSNAP West"],
    ),
    join_sections(
        "Irminger Sea",
        atlantic_sections["OSNAP East"],
        atlantic_sections["Denmark Strait"],
        atlantic_sections["Faroe Current"],
        atlantic_sections["Faroe Bank"],
    ),
    join_sections(
        "Greenland Sea",
        atlantic_sections["Fram Strait"],
        atlantic_sections["Western Europe"],
        atlantic_sections["English Channel"],
        atlantic_sections["Faroe Bank"],
        atlantic_sections["Faroe Current"],
        atlantic_sections["Denmark Strait"],
    ),
    join_sections(
        "High Arctic",
        atlantic_sections["Davis Strait"],
        atlantic_sections["Fram Strait"],
        atlantic_sections["Bering Strait"],
        atlantic_sections["Quebec"]
    )
]