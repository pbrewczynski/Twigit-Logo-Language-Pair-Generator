# country_data.py

# Note: This list is extensive but not exhaustive, and color accuracy can vary.
# Always verify colors against official sources if precision is critical.
# The order of colors is generally from top-to-bottom or left-to-right of the flag,
# or based on prominence for gradient representation.

COUNTRY_COLORS = {
    # Europe
    "Albania": ["#FF0000", "#000000"],  # Red, Black (eagle)
    "Andorra": ["#0000FF", "#FFFF00", "#FF0000"], # Blue, Yellow, Red
    "Austria": ["#FF0000", "#FFFFFF", "#FF0000"], # Red, White, Red
    "Belarus": ["#FF0000", "#008000"], # Red, Green (ornament is complex)
    "Belgium": ["#000000", "#FFFF00", "#FF0000"], # Black, Yellow, Red
    "Bosnia and Herzegovina": ["#0000FF", "#FFFF00"], # Blue, Yellow (stars are white)
    "Bulgaria": ["#FFFFFF", "#008000", "#FF0000"], # White, Green, Red
    "Croatia": ["#FF0000", "#FFFFFF", "#0000FF"], # Red, White, Blue
    "Cyprus": ["#FFFFFF", "#FF8000"], # White, Copper (island), Green (olive branches)
    "Czech Republic": ["#FFFFFF", "#FF0000", "#0000FF"], # White, Red, Blue (triangle)
    "Denmark": ["#FF0000", "#FFFFFF"], # Red, White (cross)
    "Estonia": ["#0000FF", "#000000", "#FFFFFF"], # Blue, Black, White
    "Finland": ["#FFFFFF", "#0000FF"], # White, Blue (cross)
    "France": ["#000091", "#FFFFFF", "#E1000F"], # Blue, White, Red
    "Germany": ["#000000", "#DD0000", "#FFCC00"], # Black, Red, Gold
    "Greece": ["#0000FF", "#FFFFFF"], # Blue, White
    "Hungary": ["#FF0000", "#FFFFFF", "#008000"], # Red, White, Green
    "Iceland": ["#0000FF", "#FFFFFF", "#FF0000"], # Blue, White (cross), Red (inner cross)
    "Ireland": ["#008000", "#FFFFFF", "#FFA500"], # Green, White, Orange
    "Italy": ["#009246", "#FFFFFF", "#CE2B37"], # Green, White, Red
    "Latvia": ["#9E1B32", "#FFFFFF", "#9E1B32"], # Carmine, White, Carmine
    "Liechtenstein": ["#0000FF", "#FF0000"], # Blue, Red (crown is gold)
    "Lithuania": ["#FFFF00", "#008000", "#FF0000"], # Yellow, Green, Red
    "Luxembourg": ["#FF0000", "#FFFFFF", "#00A1DE"], # Red, White, Light Blue
    "Malta": ["#FFFFFF", "#FF0000"], # White, Red (George Cross is complex)
    "Moldova": ["#0000FF", "#FFFF00", "#FF0000"], # Blue, Yellow, Red (eagle is complex)
    "Monaco": ["#FF0000", "#FFFFFF"], # Red, White (same as Indonesia, but different proportions)
    "Montenegro": ["#FF0000", "#DAA520"], # Red, Gold (border and eagle)
    "Netherlands": ["#AE1C28", "#FFFFFF", "#21468B"], # Red, White, Blue
    "North Macedonia": ["#FF0000", "#FFFF00"], # Red, Yellow (sun)
    "Norway": ["#FF0000", "#FFFFFF", "#0000FF"], # Red, White (cross), Blue (inner cross)
    "Poland": ["#FFFFFF", "#FF0000"], # White, Red
    "Portugal": ["#008000", "#FF0000"], # Green, Red (coat of arms is complex)
    "Romania": ["#0000FF", "#FFFF00", "#FF0000"], # Blue, Yellow, Red
    "Russia": ["#FFFFFF", "#0000FF", "#FF0000"], # White, Blue, Red
    "San Marino": ["#FFFFFF", "#00A0E9"], # White, Light Blue (coat of arms is complex)
    "Serbia": ["#FF0000", "#0000FF", "#FFFFFF"], # Red, Blue, White (coat of arms is complex)
    "Slovakia": ["#FFFFFF", "#0000FF", "#FF0000"], # White, Blue, Red (coat of arms is complex)
    "Slovenia": ["#FFFFFF", "#0000FF", "#FF0000"], # White, Blue, Red (coat of arms is complex)
    "Spain": ["#FF0000", "#FFFF00", "#FF0000"], # Red, Yellow, Red (coat of arms is complex)
    "Sweden": ["#0000FF", "#FFFF00"], # Blue, Yellow (cross)
    "Switzerland": ["#FF0000", "#FFFFFF"], # Red, White (cross)
    "Ukraine": ["#0057B7", "#FFD700"], # Blue, Yellow
    "United Kingdom": ["#012169", "#FFFFFF", "#C8102E"], # Blue, White, Red (Union Jack is complex for linear)
    "Vatican City": ["#FFFF00", "#FFFFFF"], # Yellow, White (coat of arms is complex)

    # Americas
    "Antigua and Barbuda": ["#000000", "#0000FF", "#FFFFFF", "#FFFF00", "#FF0000"], # Black, Blue, White, Yellow (sun), Red (complex)
    "Argentina": ["#75AADB", "#FFFFFF", "#75AADB"], # Light Blue, White, Light Blue (sun is yellow)
    "Bahamas": ["#00A98F", "#FFFF00", "#000000"], # Aquamarine, Yellow, Black
    "Barbados": ["#0000FF", "#FFFF00", "#000000"], # Blue, Yellow, Black (trident)
    "Belize": ["#0000FF", "#FF0000"], # Blue, Red (coat of arms is very complex)
    "Bolivia": ["#FF0000", "#FFFF00", "#008000"], # Red, Yellow, Green
    "Brazil": ["#008000", "#FFFF00", "#0000FF"], # Green, Yellow (rhombus), Blue (circle with stars)
    "Canada": ["#FF0000", "#FFFFFF", "#FF0000"], # Red, White, Red (maple leaf)
    "Chile": ["#FFFFFF", "#FF0000", "#0000FF"], # White, Red, Blue (star is white)
    "Colombia": ["#FFFF00", "#0000FF", "#FF0000"], # Yellow, Blue, Red
    "Costa Rica": ["#0000FF", "#FFFFFF", "#FF0000", "#FFFFFF", "#0000FF"], # Blue, White, Red, White, Blue
    "Cuba": ["#0000FF", "#FFFFFF", "#FF0000"], # Blue, White stripes, Red (triangle), White (star)
    "Dominica": ["#008000", "#FFFF00", "#000000", "#FFFFFF"], # Green, Yellow/Black/White (cross), Red (disk), Purple (parrot - complex)
    "Dominican Republic": ["#0000FF", "#FFFFFF", "#FF0000"], # Blue, White (cross), Red
    "Ecuador": ["#FFFF00", "#0000FF", "#FF0000"], # Yellow, Blue, Red (coat of arms complex)
    "El Salvador": ["#0000FF", "#FFFFFF", "#0000FF"], # Blue, White, Blue (coat of arms complex)
    "Grenada": ["#008000", "#FFFF00", "#FF0000"], # Green, Yellow (border/stars), Red (border/rectangle) - (nutmeg complex)
    "Guatemala": ["#00A0E9", "#FFFFFF", "#00A0E9"], # Light Blue, White, Light Blue (coat of arms complex)
    "Guyana": ["#008000", "#FFFF00", "#000000", "#FF0000", "#FFFFFF"], # Green, Yellow (arrow), Black/Red/White (borders - complex)
    "Haiti": ["#0000FF", "#FF0000"], # Blue, Red (coat of arms complex)
    "Honduras": ["#0000FF", "#FFFFFF", "#0000FF"], # Blue, White, Blue (stars are blue)
    "Jamaica": ["#008000", "#FFFF00", "#000000"], # Green, Yellow (saltire), Black
    "Mexico": ["#008000", "#FFFFFF", "#FF0000"], # Green, White, Red (coat of arms complex)
    "Nicaragua": ["#0000FF", "#FFFFFF", "#0000FF"], # Blue, White, Blue (coat of arms complex)
    "Panama": ["#FFFFFF", "#FF0000", "#0000FF"], # White/Red quarters, Blue star, Red star
    "Paraguay": ["#FF0000", "#FFFFFF", "#0000FF"], # Red, White, Blue (different emblems on obverse/reverse - complex)
    "Peru": ["#FF0000", "#FFFFFF", "#FF0000"], # Red, White, Red
    "Saint Kitts and Nevis": ["#008000", "#FFFF00", "#000000", "#FF0000"], # Green, Yellow (stripes), Black (stripe with stars), Red (complex)
    "Saint Lucia": ["#00A0E9", "#FFFF00", "#000000", "#FFFFFF"], # Light Blue, Yellow (triangle), Black (triangle), White (border - complex)
    "Saint Vincent and the Grenadines": ["#0000FF", "#FFFF00", "#008000"], # Blue, Yellow, Green (diamonds are green - complex)
    "Suriname": ["#008000", "#FFFFFF", "#FF0000", "#FFFF00"], # Green, White, Red, White, Green, Yellow (star)
    "Trinidad and Tobago": ["#FF0000", "#FFFFFF", "#000000"], # Red, White (stripe), Black (stripe)
    "USA": ["#BF0A30", "#FFFFFF", "#002868"], # Old Glory Red, White, Old Glory Blue
    "Uruguay": ["#FFFFFF", "#0000FF", "#FFFF00"], # White/Blue stripes, Yellow (Sun of May)
    "Venezuela": ["#FFFF00", "#0000FF", "#FF0000"], # Yellow, Blue, Red (stars are white in an arc)

    # Asia
    "Afghanistan": ["#000000", "#FF0000", "#008000"], # Black, Red, Green (Emblem is white/gold - complex, current flag can vary)
    "Armenia": ["#FF0000", "#0000FF", "#FFA500"], # Red, Blue, Orange
    "Azerbaijan": ["#00A0E9", "#FF0000", "#008000"], # Light Blue, Red, Green (crescent/star are white)
    "Bahrain": ["#FFFFFF", "#FF0000"], # White, Red (serrated edge)
    "Bangladesh": ["#008000", "#FF0000"], # Dark Green, Red (circle)
    "Bhutan": ["#FFFF00", "#FFA500", "#FFFFFF"], # Yellow, Orange (dragon is white/black - complex)
    "Brunei": ["#FFFF00", "#FFFFFF", "#000000"], # Yellow, White/Black (diagonal stripes - complex emblem)
    "Cambodia": ["#0000FF", "#FF0000", "#FFFFFF"], # Blue, Red, White (Angkor Wat)
    "China": ["#FF0000", "#FFFF00"], # Red, Yellow (stars)
    "Georgia": ["#FFFFFF", "#FF0000"], # White, Red (crosses)
    "India": ["#FFA500", "#FFFFFF", "#008000", "#000080"], # Saffron, White, Green, Navy Blue (Ashoka Chakra)
    "Indonesia": ["#FF0000", "#FFFFFF"], # Red, White
    "Iran": ["#008000", "#FFFFFF", "#FF0000"], # Green, White, Red (emblem/script complex)
    "Iraq": ["#FF0000", "#FFFFFF", "#000000", "#008000"], # Red, White, Black, Green (script)
    "Israel": ["#FFFFFF", "#0000FF"], # White, Blue (Star of David and stripes)
    "Japan": ["#FFFFFF", "#BC002D"], # White, Red (sun disc)
    "Jordan": ["#000000", "#FFFFFF", "#008000", "#FF0000"], # Black, White, Green (stripes), Red (triangle with white star)
    "Kazakhstan": ["#00A0E9", "#FFFF00"], # Light Blue, Gold (sun and eagle, ornament)
    "Kuwait": ["#008000", "#FFFFFF", "#FF0000", "#000000"], # Green, White, Red (stripes), Black (trapezoid)
    "Kyrgyzstan": ["#FF0000", "#FFFF00"], # Red, Yellow (sun/tunduk)
    "Laos": ["#FF0000", "#0000FF", "#FFFFFF"], # Red, Dark Blue, White (disc)
    "Lebanon": ["#FF0000", "#FFFFFF", "#008000"], # Red, White, Green (cedar tree)
    "Malaysia": ["#FF0000", "#FFFFFF", "#0000FF", "#FFFF00"], # Red/White stripes, Blue (canton), Yellow (crescent/star) (complex)
    "Maldives": ["#FF0000", "#008000", "#FFFFFF"], # Red, Green (rectangle), White (crescent)
    "Mongolia": ["#FF0000", "#0000FF", "#FFFF00"], # Red, Blue, Red, Yellow (Soyombo symbol - complex)
    "Myanmar": ["#FFFF00", "#008000", "#FF0000", "#FFFFFF"], # Yellow, Green, Red (stripes), White (star)
    "Nepal": ["#DC143C", "#0000FF", "#FFFFFF"], # Crimson, Blue (border), White (moon/sun - unique shape, complex)
    "North Korea": ["#0000FF", "#FFFFFF", "#FF0000"], # Blue, White, Red (star in circle)
    "Oman": ["#FF0000", "#FFFFFF", "#008000"], # Red, White, Green (emblem is white - complex)
    "Pakistan": ["#008000", "#FFFFFF"], # Green, White (crescent/star, vertical bar)
    "Palestine": ["#000000", "#FFFFFF", "#008000", "#FF0000"], # Black, White, Green (stripes), Red (triangle)
    "Philippines": ["#0000FF", "#FF0000", "#FFFFFF", "#FFFF00"], # Blue, Red, White (triangle), Yellow (sun/stars)
    "Qatar": ["#FFFFFF", "#8A004F"], # White, Maroon (serrated edge)
    "Saudi Arabia": ["#008000", "#FFFFFF"], # Green, White (Shahada and sword - complex script)
    "Singapore": ["#FF0000", "#FFFFFF"], # Red, White (crescent/stars are white)
    "South Korea": ["#FFFFFF", "#FF0000", "#0000FF", "#000000"], # White, Red/Blue (taegeuk), Black (trigrams)
    "Sri Lanka": ["#FFD700", "#800000", "#FFA500", "#008000"], # Gold (border), Maroon, Orange/Green (stripes), (Lion is gold - complex)
    "Syria": ["#FF0000", "#FFFFFF", "#000000", "#008000"], # Red, White, Black (stripes), Green (stars)
    "Taiwan": ["#FF0000", "#0000FF", "#FFFFFF"], # Red, Blue (canton with white sun) (ROC flag)
    "Tajikistan": ["#FF0000", "#FFFFFF", "#008000", "#FFFF00"], # Red, White, Green (crown/stars are yellow - complex)
    "Thailand": ["#FF0000", "#FFFFFF", "#0000FF", "#FFFFFF", "#FF0000"], # Red, White, Blue, White, Red
    "Timor-Leste": ["#FF0000", "#FFFF00", "#000000", "#FFFFFF"], # Red, Yellow (triangle), Black (triangle), White (star)
    "Turkey": ["#FF0000", "#FFFFFF"], # Red, White (crescent/star)
    "Turkmenistan": ["#008000", "#FFFFFF", "#800000"], # Green, White (crescent/stars), Maroon (carpet band - very complex)
    "United Arab Emirates": ["#FF0000", "#008000", "#FFFFFF", "#000000"], # Red (vertical), Green, White, Black (horizontal)
    "Uzbekistan": ["#00A0E9", "#FFFFFF", "#008000", "#FF0000"], # Light Blue, White, Green (stripes separated by red fimbriations, crescent/stars are white)
    "Vietnam": ["#FF0000", "#FFFF00"], # Red, Yellow (star)
    "Yemen": ["#FF0000", "#FFFFFF", "#000000"], # Red, White, Black

    # Africa
    "Algeria": ["#008000", "#FFFFFF", "#FF0000"], # Green, White, Red (star/crescent)
    "Angola": ["#FF0000", "#000000", "#FFFF00"], # Red, Black, Yellow (machete/gear/star)
    "Benin": ["#008000", "#FFFF00", "#FF0000"], # Green (vertical), Yellow, Red (horizontal)
    "Botswana": ["#00A0E9", "#FFFFFF", "#000000"], # Light Blue, White (stripe), Black (stripe)
    "Burkina Faso": ["#FF0000", "#008000", "#FFFF00"], # Red, Green, Yellow (star)
    "Burundi": ["#FF0000", "#008000", "#FFFFFF"], # Red, Green (saltire is white, stars in circle - complex)
    "Cabo Verde": ["#0000FF", "#FFFFFF", "#FF0000", "#FFFF00"], # Blue, White/Red/White (stripes), Yellow (stars in circle)
    "Cameroon": ["#008000", "#FF0000", "#FFFF00"], # Green, Red, Yellow (star is yellow)
    "Central African Republic": ["#0000FF", "#FFFFFF", "#008000", "#FFFF00", "#FF0000"], # Blue, White, Green, Yellow (horiz. stripes), Red (vert. stripe), Yellow (star) (complex)
    "Chad": ["#0000FF", "#FFFF00", "#FF0000"], # Blue, Yellow, Red (same as Romania)
    "Comoros": ["#FFFF00", "#FFFFFF", "#FF0000", "#0000FF", "#008000"], # Yellow, White, Red, Blue (stripes), Green (triangle with crescent/stars) (complex)
    "Congo (Dem. Rep.)": ["#00A0E9", "#FF0000", "#FFFF00"], # Sky Blue, Red (stripe with yellow fimbriation), Yellow (star)
    "Congo (Rep.)": ["#008000", "#FFFF00", "#FF0000"], # Green, Yellow (diagonal band), Red
    "Cote d'Ivoire": ["#FFA500", "#FFFFFF", "#008000"], # Orange, White, Green (same as Ireland, reversed)
    "Djibouti": ["#00A0E9", "#008000", "#FFFFFF", "#FF0000"], # Light Blue, Green, White (triangle), Red (star)
    "Egypt": ["#FF0000", "#FFFFFF", "#000000", "#DAA520"], # Red, White, Black, Gold (Eagle of Saladin)
    "Equatorial Guinea": ["#008000", "#FFFFFF", "#FF0000", "#00A0E9"], # Green, White, Red, Light Blue (triangle - coat of arms complex)
    "Eritrea": ["#008000", "#FF0000", "#0000FF", "#FFFF00"], # Green/Blue (triangles), Red (triangle), Yellow (emblem - complex)
    "Eswatini": ["#0000FF", "#FFFF00", "#8B0000", "#FFFFFF", "#000000"], # Blue, Yellow, Crimson, Black/White (shield - complex)
    "Ethiopia": ["#008000", "#FFFF00", "#FF0000", "#0000FF"], # Green, Yellow, Red, Blue (disc with star emblem)
    "Gabon": ["#008000", "#FFFF00", "#0000FF"], # Green, Yellow, Blue
    "Gambia": ["#FF0000", "#0000FF", "#008000", "#FFFFFF"], # Red, Blue, Green (separated by white fimbriations)
    "Ghana": ["#FF0000", "#FFFF00", "#008000", "#000000"], # Red, Yellow, Green, Black (star)
    "Guinea": ["#FF0000", "#FFFF00", "#008000"], # Red, Yellow, Green
    "Guinea-Bissau": ["#FF0000", "#FFFF00", "#008000", "#000000"], # Red (vertical), Yellow, Green (horizontal), Black (star)
    "Kenya": ["#000000", "#FF0000", "#008000", "#FFFFFF"], # Black, Red, Green (separated by white fimbriations, shield/spears complex)
    "Lesotho": ["#0000FF", "#FFFFFF", "#008000", "#000000"], # Blue, White, Green, Black (Mokorotlo hat)
    "Liberia": ["#FF0000", "#FFFFFF", "#0000FF"], # Red/White stripes, Blue (canton with white star) (similar to US)
    "Libya": ["#FF0000", "#000000", "#008000", "#FFFFFF"], # Red, Black, Green (stripes), White (crescent/star)
    "Madagascar": ["#FFFFFF", "#FF0000", "#008000"], # White (vertical), Red, Green (horizontal)
    "Malawi": ["#000000", "#FF0000", "#008000", "#DC143C"], # Black, Red, Green (stripes), Red (rising sun)
    "Mali": ["#008000", "#FFFF00", "#FF0000"], # Green, Yellow, Red
    "Mauritania": ["#008000", "#FFFF00", "#FF0000"], # Green, Yellow (crescent/star), Red (top/bottom bands added 2017)
    "Mauritius": ["#FF0000", "#0000FF", "#FFFF00", "#008000"], # Red, Blue, Yellow, Green
    "Morocco": ["#FF0000", "#008000"], # Red, Green (pentagram)
    "Mozambique": ["#008000", "#000000", "#FFFF00", "#FF0000", "#FFFFFF"], # Green, Black/Yellow/Black (fimbriated stripes), Red (triangle), (AK47/book/hoe emblem complex)
    "Namibia": ["#0000FF", "#FF0000", "#008000", "#FFFFFF", "#FFFF00"], # Blue/Red/Green (diagonal bands separated by white, sun is yellow - complex)
    "Niger": ["#FFA500", "#FFFFFF", "#008000"], # Orange, White, Green, Orange (circle)
    "Nigeria": ["#008000", "#FFFFFF", "#008000"], # Green, White, Green
    "Rwanda": ["#00A0E9", "#FFFF00", "#008000"], # Light Blue, Yellow, Green, Yellow (sun)
    "Sao Tome and Principe": ["#008000", "#FFFF00", "#FF0000", "#000000"], # Green, Yellow (with black stars), Red (triangle)
    "Senegal": ["#008000", "#FFFF00", "#FF0000"], # Green, Yellow, Red (star is green)
    "Seychelles": ["#0000FF", "#FFFF00", "#FF0000", "#FFFFFF", "#008000"], # Blue, Yellow, Red, White, Green (oblique bands - complex for linear gradient)
    "Sierra Leone": ["#008000", "#FFFFFF", "#00A0E9"], # Green, White, Light Blue
    "Somalia": ["#00A0E9", "#FFFFFF"], # Light Blue, White (star)
    "South Africa": ["#FF0000", "#FFFFFF", "#0000FF", "#008000", "#000000", "#FFFF00"], # (Complex "Y" shape - very hard for simple linear) Red, White, Blue, Green, Black, Yellow
    "South Sudan": ["#000000", "#FF0000", "#008000", "#0000FF", "#FFFFFF", "#FFFF00"], # Black, Red, Green (sep by white), Blue (triangle), Yellow (star) (complex)
    "Sudan": ["#FF0000", "#FFFFFF", "#000000", "#008000"], # Red, White, Black (stripes), Green (triangle)
    "Tanzania": ["#008000", "#FFFF00", "#000000", "#00A0E9"], # Green/Blue (triangles), Yellow/Black/Yellow (diagonal band)
    "Togo": ["#008000", "#FFFF00", "#FF0000", "#FFFFFF"], # Green/Yellow stripes, Red (canton with white star)
    "Tunisia": ["#FF0000", "#FFFFFF"], # Red, White (circle with red crescent/star)
    "Uganda": ["#000000", "#FFFF00", "#FF0000"], # Black, Yellow, Red (stripes), White (circle with crane - complex)
    "Zambia": ["#008000", "#FF0000", "#000000", "#FFA500"], # Green, Red/Black/Orange (stripes in fly, eagle is orange - complex)
    "Zimbabwe": ["#008000", "#FFFF00", "#FF0000", "#000000", "#FFFFFF"], # Green/Yellow/Red/Black stripes, White (triangle), Red (star), Yellow (bird - complex)

    # Oceania
    "Australia": ["#00008B", "#FFFFFF", "#FF0000"], # Dark Blue, White (stars, Union Jack), Red (Union Jack) (complex)
    "Fiji": ["#00A0E9", "#FFFFFF", "#00008B", "#FF0000"], # Light Blue, White/Red/Blue (shield elements & Union Jack - complex)
    "Kiribati": ["#FF0000", "#0000FF", "#FFFF00", "#FFFFFF"], # Red, Blue (waves), Yellow (sun), White (frigatebird - complex)
    "Marshall Islands": ["#0000FF", "#FFA500", "#FFFFFF"], # Blue, Orange/White (radiating bands, star - complex)
    "Micronesia": ["#00A0E9", "#FFFFFF"], # Light Blue, White (stars)
    "Nauru": ["#000080", "#FFFF00", "#FFFFFF"], # Dark Blue, Yellow (stripe), White (star)
    "New Zealand": ["#00008B", "#FFFFFF", "#FF0000"], # Dark Blue, Red (stars with white border), (Union Jack - complex)
    "Palau": ["#00A0E9", "#FFFF00"], # Light Blue, Yellow (disc - off-center)
    "Papua New Guinea": ["#FF0000", "#000000", "#FFFF00", "#FFFFFF"], # Red/Black (triangles), Yellow (bird of paradise), White (Southern Cross stars) (complex)
    "Samoa": ["#FF0000", "#0000FF", "#FFFFFF"], # Red, Blue (canton with white Southern Cross stars)
    "Solomon Islands": ["#0000FF", "#008000", "#FFFF00"], # Blue/Green (triangles separated by yellow diagonal band, stars are white)
    "Tonga": ["#FF0000", "#FFFFFF"], # Red, White (canton with red cross)
    "Tuvalu": ["#00A0E9", "#FFFF00", "#FFFFFF"], # Light Blue, Yellow (stars), (Union Jack - complex)
    "Vanuatu": ["#FF0000", "#008000", "#000000", "#FFFF00"], # Red/Green (bands sep by yellow fimbriation), Black (triangle), (Boar's tusk/fern emblem - complex)
}

COUNTRY_CODES = {
    "Albania": "al", "Andorra": "ad", "Austria": "at", "Belarus": "by", "Belgium": "be",
    "Bosnia and Herzegovina": "ba", "Bulgaria": "bg", "Croatia": "hr", "Cyprus": "cy",
    "Czech Republic": "cz", "Denmark": "dk", "Estonia": "ee", "Finland": "fi", "France": "fr",
    "Germany": "de", "Greece": "gr", "Hungary": "hu", "Iceland": "is", "Ireland": "ie",
    "Italy": "it", "Latvia": "lv", "Liechtenstein": "li", "Lithuania": "lt", "Luxembourg": "lu",
    "Malta": "mt", "Moldova": "md", "Monaco": "mc", "Montenegro": "me", "Netherlands": "nl",
    "North Macedonia": "mk", "Norway": "no", "Poland": "pl", "Portugal": "pt", "Romania": "ro",
    "Russia": "ru", "San Marino": "sm", "Serbia": "rs", "Slovakia": "sk", "Slovenia": "si",
    "Spain": "es", "Sweden": "se", "Switzerland": "ch", "Ukraine": "ua", "United Kingdom": "gb",
    "Vatican City": "va",

    "Antigua and Barbuda": "ag", "Argentina": "ar", "Bahamas": "bs", "Barbados": "bb",
    "Belize": "bz", "Bolivia": "bo", "Brazil": "br", "Canada": "ca", "Chile": "cl",
    "Colombia": "co", "Costa Rica": "cr", "Cuba": "cu", "Dominica": "dm",
    "Dominican Republic": "do", "Ecuador": "ec", "El Salvador": "sv", "Grenada": "gd",
    "Guatemala": "gt", "Guyana": "gy", "Haiti": "ht", "Honduras": "hn", "Jamaica": "jm",
    "Mexico": "mx", "Nicaragua": "ni", "Panama": "pa", "Paraguay": "py", "Peru": "pe",
    "Saint Kitts and Nevis": "kn", "Saint Lucia": "lc",
    "Saint Vincent and the Grenadines": "vc", "Suriname": "sr",
    "Trinidad and Tobago": "tt", "USA": "us", "Uruguay": "uy", "Venezuela": "ve",

    "Afghanistan": "af", "Armenia": "am", "Azerbaijan": "az", "Bahrain": "bh",
    "Bangladesh": "bd", "Bhutan": "bt", "Brunei": "bn", "Cambodia": "kh", "China": "cn",
    "Georgia": "ge", "India": "in", "Indonesia": "id", "Iran": "ir", "Iraq": "iq",
    "Israel": "il", "Japan": "jp", "Jordan": "jo", "Kazakhstan": "kz", "Kuwait": "kw",
    "Kyrgyzstan": "kg", "Laos": "la", "Lebanon": "lb", "Malaysia": "my", "Maldives": "mv",
    "Mongolia": "mn", "Myanmar": "mm", "Nepal": "np", "North Korea": "kp", "Oman": "om",
    "Pakistan": "pk", "Palestine": "ps", "Philippines": "ph", "Qatar": "qa",
    "Saudi Arabia": "sa", "Singapore": "sg", "South Korea": "kr", "Sri Lanka": "lk",
    "Syria": "sy", "Taiwan": "tw", "Tajikistan": "tj", "Thailand": "th", "Timor-Leste": "tl",
    "Turkey": "tr", "Turkmenistan": "tm", "United Arab Emirates": "ae", "Uzbekistan": "uz",
    "Vietnam": "vn", "Yemen": "ye",

    "Algeria": "dz", "Angola": "ao", "Benin": "bj", "Botswana": "bw", "Burkina Faso": "bf",
    "Burundi": "bi", "Cabo Verde": "cv", "Cameroon": "cm", "Central African Republic": "cf",
    "Chad": "td", "Comoros": "km", "Congo (Dem. Rep.)": "cd", "Congo (Rep.)": "cg",
    "Cote d'Ivoire": "ci", "Djibouti": "dj", "Egypt": "eg", "Equatorial Guinea": "gq",
    "Eritrea": "er", "Eswatini": "sz", "Ethiopia": "et", "Gabon": "ga", "Gambia": "gm",
    "Ghana": "gh", "Guinea": "gn", "Guinea-Bissau": "gw", "Kenya": "ke", "Lesotho": "ls",
    "Liberia": "lr", "Libya": "ly", "Madagascar": "mg", "Malawi": "mw", "Mali": "ml",
    "Mauritania": "mr", "Mauritius": "mu", "Morocco": "ma", "Mozambique": "mz", "Namibia": "na",
    "Niger": "ne", "Nigeria": "ng", "Rwanda": "rw", "Sao Tome and Principe": "st",
    "Senegal": "sn", "Seychelles": "sc", "Sierra Leone": "sl", "Somalia": "so",
    "South Africa": "za", "South Sudan": "ss", "Sudan": "sd", "Tanzania": "tz", "Togo": "tg",
    "Tunisia": "tn", "Uganda": "ug", "Zambia": "zm", "Zimbabwe": "zw",

    "Australia": "au", "Fiji": "fj", "Kiribati": "ki", "Marshall Islands": "mh",
    "Micronesia": "fm", "Nauru": "nr", "New Zealand": "nz", "Palau": "pw",
    "Papua New Guinea": "pg", "Samoa": "ws", "Solomon Islands": "sb", "Tonga": "to",
    "Tuvalu": "tv", "Vanuatu": "vu"
}

if __name__ == "__main__":
    print("Country Data Module")
    print("-------------------")
    print(f"Loaded colors for {len(COUNTRY_COLORS)} countries.")
    print(f"Loaded codes for {len(COUNTRY_CODES)} countries.")

    # Basic check for consistency
    missing_codes = [name for name in COUNTRY_COLORS if name not in COUNTRY_CODES]
    missing_colors = [name for name in COUNTRY_CODES if name not in COUNTRY_COLORS]

    if missing_codes:
        print(f"\nWarning: Countries in COUNTRY_COLORS but missing from COUNTRY_CODES: {missing_codes}")
    if missing_colors:
        print(f"\nWarning: Countries in COUNTRY_CODES but missing from COUNTRY_COLORS: {missing_colors}")

    if not missing_codes and not missing_colors and len(COUNTRY_COLORS) == len(COUNTRY_CODES):
        print("\nCOUNTRY_COLORS and COUNTRY_CODES seem consistent in terms of entries.")
    else:
        print("\nThere are inconsistencies between COUNTRY_COLORS and COUNTRY_CODES entries.")

    if "France" in COUNTRY_COLORS and "France" in COUNTRY_CODES:
        print(f"\nExample for France:")
        print(f"  Colors: {COUNTRY_COLORS['France']}")
        print(f"  Code:   {COUNTRY_CODES['France']}")