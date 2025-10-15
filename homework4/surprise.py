# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(targets):
	for star in targets:
		print(star)
	print()

# 2) Write a function that uses a loop to print the name of each star with its spectral type.

def print_star_spectral_types(targets):
    for star_name, info in targets.items():
        print(f"{star_name}: {info['Spectral Type']}")


# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_fainter_stars(targets):
    """Finds and prints stars with a magnitude greater than 0.1."""
    print("\nStars with magnitude > 0.1:")
    for star_name, info in targets.items():
        if info["Magnitude"] > 0.1:
            print(f"{star_name}: Magnitude {info['Magnitude']}")




# 4) Look up another target, add all the necessary information to the targets list. 

targets["Proxima Centauri"] = {
    "RA": "14hr 29m 42.9s",
    "Dec": "-62° 40' 46¨",
    "Magnitude": 11.13,
    "Spectral Type": "M5.5V"
}
 
#5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_brightest_near_dec_20(targets):
    """
    Finds the brightest star whose declination is closest to 20°.
    Note: A lower magnitude value means a brighter star.
    """
    min_dec_difference = float('inf') 
    target_name = None
    target_magnitude = float('inf')

    for star_name, info in targets.items():
        
        dec_str = info["Dec"].replace("°", "").replace("−", "-").strip()
        dec_degrees = float(dec_str.split()[0])

        dec_difference = abs(dec_degrees - 20)

        if dec_difference < min_dec_difference:
            min_dec_difference = dec_difference
            target_name = star_name
            target_magnitude = info["Magnitude"]
        elif dec_difference == min_dec_difference:
            
            if info["Magnitude"] < target_magnitude:
                target_name = star_name
                target_magnitude = info["Magnitude"]

    print(f"\nThe brightest star with a declination closest to 20° is: {target_name}")



# 6) What is your favorite constellation?
def fav_constellation():
    constellation = "Big Dipper"
    print(constellation)



print_star_names(targets)

print_star_spectral_types(targets)

find_fainter_stars(targets)


find_brightest_near_dec_20(targets)

fav_constellation()