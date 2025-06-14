# country_data.py

# Note: This list provides specific, officially defined or commonly accepted digital (HEX)
# representations of national flag colors. Accuracy has been verified against vexillological
# sources, but always check against official government standards if precision is paramount.
# The order of colors is generally from top-to-bottom or left-to-right of the flag,
# or based on prominence for gradient representation.

COUNTRY_COLORS = {
    # Europe
    "Albania": ["#DA291C", "#000000"],  # Red, Black (eagle)
    "Andorra": ["#1F4599", "#FFD100", "#D50032"], # Blue, Yellow, Red
    "Austria": ["#C8102E", "#FFFFFF", "#C8102E"], # Red, White, Red
    "Belarus": ["#D22730", "#009A44", "#FFFFFF"], # Red, Green, White (ornament background)
    "Belgium": ["#000000", "#FDDA24", "#EF3340"], # Black, Yellow, Red
    "Bosnia and Herzegovina": ["#002395", "#FFCD00", "#FFFFFF"], # Blue, Yellow, White (stars)
    "Bulgaria": ["#FFFFFF", "#00966E", "#D62612"], # White, Green, Red
    "Croatia": ["#FF0000", "#FFFFFF", "#0000FF"], # Red, White, Blue (officially defined by name, not code)
    "Cyprus": ["#FFFFFF", "#D47600", "#4E5B31"], # White, Copper (island), Green (olive branches)
    "Czech Republic": ["#FFFFFF", "#D7141A", "#11457E"], # White, Red, Blue (triangle)
    "Denmark": ["#C60C30", "#FFFFFF"], # Red (Dannebrog red), White (cross)
    "Estonia": ["#0072CE", "#000000", "#FFFFFF"], # Blue, Black, White
    "Finland": ["#FFFFFF", "#002F6C"], # White, Blue (cross)
    "France": ["#0055A4", "#FFFFFF", "#EF4135"], # Blue, White, Red
    "Germany": ["#000000", "#DD0000", "#FFCC00"], # Black, Red, Gold
    "Greece": ["#0D5EAF", "#FFFFFF"], # Blue, White
    "Hungary": ["#CE1126", "#FFFFFF", "#008751"], # Red, White, Green
    "Iceland": ["#02529C", "#FFFFFF", "#DC1E35"], # Blue, White (cross), Red (inner cross)
    "Ireland": ["#169B62", "#FFFFFF", "#FF883E"], # Green, White, Orange
    "Italy": ["#009246", "#FFFFFF", "#CE2B37"], # Green, White, Red

    "Latvia": ["#9E1B32", "#FFFFFF", "#9E1B32"], # Carmine (Latvian Red), White, Carmine
    "Liechtenstein": ["#002B7F", "#CE1126", "#F9E814"], # Blue, Red, Gold (crown)
    "Lithuania": ["#FDB913", "#006A44", "#C1272D"], # Yellow, Green, Red
    "Luxembourg": ["#EF3340", "#FFFFFF", "#00A3E0"], # Red, White, Light Blue
    "Malta": ["#FFFFFF", "#C8102E"], # White, Red (George Cross is complex)
    "Moldova": ["#0047AB", "#FFD100", "#CC092F"], # Blue, Yellow, Red (eagle is complex)
    "Monaco": ["#C8102E", "#FFFFFF"], # Red, White (same as Indonesia, different proportions)
    "Montenegro": ["#C40308", "#D4AF37"], # Red, Gold (border and eagle)
    "Netherlands": ["#AE1C28", "#FFFFFF", "#21468B"], # Red (Bright Vermilion), White, Blue (Cobalt Blue)
    "North Macedonia": ["#D20000", "#FFE600"], # Red, Yellow (sun)
    "Norway": ["#BA0C2F", "#FFFFFF", "#00205B"], # Red, White (cross), Blue (inner cross)
    "Poland": ["#FFFFFF", "#DC143C"], # White, Red (Crimson)
    "Portugal": ["#046A38", "#DA291C", "#FFD700"], # Green, Red, Yellow (coat of arms)
    "Romania": ["#002B7F", "#FCD116", "#CE1126"], # Blue, Yellow, Red
    "Russia": ["#FFFFFF", "#0039A6", "#D52B1E"], # White, Blue, Red
    "San Marino": ["#FFFFFF", "#68BBE3"], # White, Light Blue (coat of arms is complex)
    "Serbia": ["#C6363C", "#0C4076", "#FFFFFF"], # Red, Blue, White (coat of arms is complex)
    "Slovakia": ["#FFFFFF", "#0B4EA2", "#EE1C25"], # White, Blue, Red (coat of arms is complex)
    "Slovenia": ["#FFFFFF", "#005DAA", "#D21034"], # White, Blue, Red (coat of arms is complex)
    "Spain": ["#AA151B", "#F1BF00", "#AA151B"], # Red, Yellow (Gualda), Red (coat of arms complex)
    "Sweden": ["#006AA7", "#FECC02"], # Blue, Yellow (cross)
    "Switzerland": ["#DA291C", "#FFFFFF"], # Red, White (cross)
    "Ukraine": ["#0057B7", "#FFD700"], # Blue, Yellow
    "United Kingdom": ["#012169", "#FFFFFF", "#C8102E"], # Blue, White, Red (Union Jack is complex for linear)
    "Vatican City": ["#FFCC00", "#FFFFFF"], # Yellow, White (coat of arms is complex)

    # Americas
    "Antigua and Barbuda": ["#000000", "#005EB8", "#FFFFFF", "#FCD116", "#CE1126"], # Black, Blue, White, Yellow (sun), Red
    "Argentina": ["#75AADB", "#FFFFFF", "#F9B612"], # Light Blue, White, Light Blue, Yellow (Sun of May)
    "Bahamas": ["#00778B", "#FFC72C", "#000000"], # Aquamarine, Yellow, Black
    "Barbados": ["#00267F", "#FFC72C", "#000000"], # Ultramarine, Gold, Black (trident)
    "Belize": ["#003F87", "#D60000"], # Blue, Red (coat of arms is very complex)
    "Bolivia": ["#DA291C", "#F9E300", "#007A3D"], # Red, Yellow, Green
    "Brazil": ["#009B3A", "#FEDF00", "#002776"], # Green, Yellow (rhombus), Blue (circle with stars)
    "Canada": ["#FF0000", "#FFFFFF"], # Red, White (maple leaf)
    "Chile": ["#FFFFFF", "#DA291C", "#0032A0"], # White, Red, Blue (star is white)
    "Colombia": ["#FCD116", "#003893", "#CE1126"], # Yellow, Blue, Red
    "Costa Rica": ["#002B7F", "#FFFFFF", "#CE1126"], # Blue, White, Red, White, Blue
    "Cuba": ["#002A8F", "#FFFFFF", "#CF142B"], # Blue, White stripes, Red (triangle), White (star)
    "Dominica": ["#006341", "#FCD116", "#000000", "#FFFFFF", "#D41C30"], # Green, Yellow/Black/White cross, Red disk
    "Dominican Republic": ["#002D62", "#FFFFFF", "#CE1126"], # Blue, White (cross), Red

    "Ecuador": ["#FCD116", "#003893", "#CE1126"], # Yellow, Blue, Red (coat of arms complex)
    "El Salvador": ["#0047AB", "#FFFFFF"], # Blue, White, Blue (coat of arms complex)
    "Grenada": ["#007A5E", "#FCD116", "#CE1126"], # Green, Yellow (border/stars), Red (border/rectangle)
    "Guatemala": ["#4997D0", "#FFFFFF"], # Sky Blue, White, Sky Blue (coat of arms complex)
    "Guyana": ["#009E49", "#FCD116", "#000000", "#CE1126", "#FFFFFF"], # Green, Yellow, Black, Red, White
    "Haiti": ["#00209F", "#D21034"], # Blue, Red (coat of arms complex)
    "Honduras": ["#00BCE4", "#FFFFFF"], # Turquoise, White, Turquoise (stars are turquoise)
    "Jamaica": ["#009B3A", "#FED100", "#000000"], # Green, Gold (saltire), Black
    "Mexico": ["#006847", "#FFFFFF", "#CE1126"], # Green, White, Red (coat of arms complex)
    "Nicaragua": ["#0067C6", "#FFFFFF"], # Blue, White, Blue (coat of arms complex)
    "Panama": ["#FFFFFF", "#D21034", "#005293"], # White/Red quarters, Blue star, Red star
    "Paraguay": ["#D52B1E", "#FFFFFF", "#0038A8"], # Red, White, Blue
    "Peru": ["#D91023", "#FFFFFF"], # Red, White, Red
    "Saint Kitts and Nevis": ["#009E49", "#FCD116", "#000000", "#CE1126", "#FFFFFF"], # Green, Yellow, Black, Red, White (stars)
    "Saint Lucia": ["#66CCFF", "#FCD116", "#000000", "#FFFFFF"], # Cerulean Blue, Yellow, Black, White
    "Saint Vincent and the Grenadines": ["#002868", "#FCD116", "#009E60"], # Blue, Gold, Green
    "Suriname": ["#377E3F", "#FFFFFF", "#B40A2D", "#ECC81D"], # Green, White, Red, Yellow (star)
    "Trinidad and Tobago": ["#E00000", "#FFFFFF", "#000000"], # Red, White (stripe), Black (stripe)
    "USA": ["#B22234", "#FFFFFF", "#3C3B6E"], # Old Glory Red, White, Old Glory Blue
    "Uruguay": ["#0038A8", "#FFFFFF", "#FCD116"], # Blue/White stripes, Yellow (Sun of May)
    "Venezuela": ["#FCD116", "#003893", "#CE1126"], # Yellow, Blue, Red (stars are white)

    # Asia
    "Afghanistan": ["#000000", "#C8102E", "#008751", "#FFFFFF"], # Black, Red, Green, White (Emblem)
    "Armenia": ["#D90012", "#0033A0", "#F2A800"], # Red, Blue, Orange
    "Azerbaijan": ["#00B5E2", "#ED2939", "#00AF66", "#FFFFFF"], # Blue, Red, Green, White (crescent/star)
    "Bahrain": ["#FFFFFF", "#CE1126"], # White, Red (serrated edge)
    "Bangladesh": ["#006A4E", "#F42A41"], # Dark Green, Red (circle)
    "Bhutan": ["#FFC400", "#FF671F", "#FFFFFF"], # Yellow, Orange, White (dragon)
    "Brunei": ["#F7E500", "#FFFFFF", "#000000"], # Yellow, White/Black (diagonal stripes)
    "Cambodia": ["#032EA1", "#E00025", "#FFFFFF"], # Blue, Red, White (Angkor Wat)
    "China": ["#EE1C25", "#FFFF00"], # Red, Yellow (stars)
    "Georgia": ["#FFFFFF", "#FF0000"], # White, Red (crosses)
    "India": ["#FF9933", "#FFFFFF", "#138808", "#000080"], # Saffron, White, Green, Navy Blue (Ashoka Chakra)
    "Indonesia": ["#CE1126", "#FFFFFF"], # Red, White
    "Iran": ["#239F40", "#FFFFFF", "#DA0000"], # Green, White, Red (emblem/script complex)
    "Iraq": ["#CE1126", "#FFFFFF", "#000000", "#007A3D"], # Red, White, Black, Green (script)
    "Israel": ["#FFFFFF", "#0038B8"], # White, Blue (Star of David and stripes)
    "Japan": ["#FFFFFF", "#BC002D"], # White, Red (Hinomaru Red) (sun disc)
    "Jordan": ["#000000", "#FFFFFF", "#007A3D", "#CE1126"], # Black, White, Green, Red (triangle)
    "Kazakhstan": ["#00AFCA", "#FBE116"], # Light Blue, Gold (sun, eagle, ornament)
    "Kuwait": ["#007A3D", "#FFFFFF", "#CE1126", "#000000"], # Green, White, Red, Black (trapezoid)
    "Kyrgyzstan": ["#F00000", "#FFC700"], # Red, Yellow (sun/tunduk)
    "Laos": ["#CE1126", "#002868", "#FFFFFF"], # Red, Dark Blue, White (disc)
    "Lebanon": ["#ED1C24", "#FFFFFF", "#00A651"], # Red, White, Green (cedar tree)
    "Malaysia": ["#CC0000", "#FFFFFF", "#000066", "#FFCC00"], # Red/White stripes, Blue, Yellow (crescent/star)
    "Maldives": ["#C8102E", "#008751", "#FFFFFF"], # Red, Green (rectangle), White (crescent)
    "Mongolia": ["#C42129", "#0066B3", "#F2D900"], # Red, Blue, Red, Yellow (Soyombo symbol)
    "Myanmar": ["#FECB00", "#34B233", "#EA2839", "#FFFFFF"], # Yellow, Green, Red (stripes), White (star)
    "Nepal": ["#DC143C", "#003399", "#FFFFFF"], # Crimson, Blue (border), White (moon/sun)
    "North Korea": ["#024FA2", "#FFFFFF", "#ED1C27"], # Blue, White, Red (star in circle)
    "Oman": ["#DF1623", "#FFFFFF", "#00824C"], # Red, White, Green
    "Pakistan": ["#004225", "#FFFFFF"], # Green, White (crescent/star, vertical bar)
    "Palestine": ["#000000", "#FFFFFF", "#007A3D", "#CE1126"], # Black, White, Green, Red
    "Philippines": ["#0038A8", "#CE1126", "#FFFFFF", "#FCD116"], # Blue, Red, White (triangle), Gold (sun/stars)
    "Qatar": ["#FFFFFF", "#8A1538"], # White, Maroon (serrated edge)
    "Saudi Arabia": ["#006C35", "#FFFFFF"], # Green, White (Shahada and sword)
    "Singapore": ["#ED2939", "#FFFFFF"], # Red, White (crescent/stars are white)
    "South Korea": ["#FFFFFF", "#CD2E3A", "#0047A0", "#000000"], # White, Red/Blue (taegeuk), Black (trigrams)
    "Sri Lanka": ["#FFC400", "#8D1B3D", "#FF8200", "#00594F"], # Gold (border), Maroon, Orange/Green (Lion is gold)
    "Syria": ["#CE1126", "#FFFFFF", "#000000", "#007A3D"], # Red, White, Black (stripes), Green (stars)
    "Taiwan": ["#FE0000", "#000095", "#FFFFFF"], # Red, Blue (canton with white sun)
    "Tajikistan": ["#D72329", "#FFFFFF", "#006633", "#F8C300"], # Red, White, Green, Gold (crown/stars)
    "Thailand": ["#A51931", "#FFFFFF", "#2E428B"], # Red, White, Blue, White, Red
    "Timor-Leste": ["#DA291C", "#FFC72C", "#000000", "#FFFFFF"], # Red, Yellow (triangle), Black (triangle), White (star)
    "Turkey": ["#E30A17", "#FFFFFF"], # Red, White (crescent/star)
    "Turkmenistan": ["#009739", "#FFFFFF", "#D41E14"], # Green, White, Red (carpet band)
    "United Arab Emirates": ["#EF3340", "#009739", "#FFFFFF", "#000000"], # Red, Green, White, Black
    "Uzbekistan": ["#009DD6", "#FFFFFF", "#009A44", "#CE2029"], # Blue, White, Green, Red (fimbriations)
    "Vietnam": ["#DA251D", "#FFFF00"], # Red, Yellow (star)
    "Yemen": ["#CE1126", "#FFFFFF", "#000000"], # Red, White, Black

    # Africa
    "Algeria": ["#006233", "#FFFFFF", "#D21034"], # Green, White, Red (star/crescent)
    "Angola": ["#C8102E", "#000000", "#FFC907"], # Red, Black, Yellow (machete/gear/star)
    "Benin": ["#008751", "#FCD116", "#E8112D"], # Green, Yellow, Red
    "Botswana": ["#75AADB", "#FFFFFF", "#000000"], # Light Blue, White, Black
    "Burkina Faso": ["#EF2B2D", "#009E49", "#FCD116"], # Red, Green, Yellow (star)
    "Burundi": ["#CE1126", "#007A5E", "#FFFFFF"], # Red, Green, White (saltire)
    "Cabo Verde": ["#003893", "#FFFFFF", "#CF2027", "#F7D116"], # Blue, White/Red/White (stripes), Yellow (stars)
    "Cameroon": ["#007A5E", "#CE1126", "#FCD116"], # Green, Red, Yellow (star is yellow)
    "Central African Republic": ["#0038A8", "#FFFFFF", "#009A44", "#FCD116", "#CE1126"], # Blue, White, Green, Yellow, Red
    "Chad": ["#002664", "#FECB00", "#C60C30"], # Blue, Yellow, Red (very similar to Romania)
    "Comoros": ["#FCD116", "#FFFFFF", "#CE1126", "#3A75C4", "#00966E"], # Yellow, White, Red, Blue, Green (triangle)
    "Congo (Dem. Rep.)": ["#007FFF", "#CE1021", "#F7D518"], # Sky Blue, Red, Yellow (fimbriation/star)
    "Congo (Rep.)": ["#009A44", "#FCD116", "#DC241F"], # Green, Yellow (diagonal), Red
    "Cote d'Ivoire": ["#FF8F00", "#FFFFFF", "#009E60"], # Orange, White, Green
    "Djibouti": ["#7AB2E8", "#00A95C", "#FFFFFF", "#D7141A"], # Light Blue, Green, White (triangle), Red (star)
    "Egypt": ["#CE1126", "#FFFFFF", "#000000", "#C09300"], # Red, White, Black, Gold (Eagle of Saladin)
    "Equatorial Guinea": ["#3E9A00", "#FFFFFF", "#E32118", "#0073CE"], # Green, White, Red, Blue (triangle)
    "Eritrea": ["#009A44", "#EA2839", "#418FDE", "#FFC72C"], # Green/Blue (triangles), Red, Yellow (emblem)
    "Eswatini": ["#3E448B", "#FCD116", "#B10C0C", "#FFFFFF", "#000000"], # Blue, Yellow, Crimson, Black/White (shield)
    "Ethiopia": ["#078930", "#FCDD09", "#DA121A", "#0B63F3"], # Green, Yellow, Red, Blue (disc)
    "Gabon": ["#009E60", "#FCD116", "#3A75C4"], # Green, Yellow, Blue
    "Gambia": ["#CE1126", "#0C1C8C", "#3A7728", "#FFFFFF"], # Red, Blue, Green (sep. by white fimbriations)
    "Ghana": ["#CE1126", "#FCD116", "#006B3F", "#000000"], # Red, Yellow, Green, Black (star)
    "Guinea": ["#CE1126", "#FCD116", "#009460"], # Red, Yellow, Green
    "Guinea-Bissau": ["#CE1126", "#FCD116", "#009E49", "#000000"], # Red, Yellow, Green, Black (star)
    "Kenya": ["#000000", "#BB252A", "#008851", "#FFFFFF"], # Black, Red, Green, White (fimbriations/shield)
    "Lesotho": ["#00209F", "#FFFFFF", "#009A44", "#000000"], # Blue, White, Green, Black (Mokorotlo hat)
    "Liberia": ["#C8102E", "#FFFFFF", "#002868"], # Red/White stripes, Blue (canton/star)
    "Libya": ["#E70013", "#000000", "#239E46", "#FFFFFF"], # Red, Black, Green, White (crescent/star)
    "Madagascar": ["#FFFFFF", "#FC3D32", "#007E3A"], # White, Red, Green
    "Malawi": ["#000000", "#CE1126", "#3A7728"], # Black, Red, Green, Red (sun)

    "Mali": ["#14B53A", "#FCD116", "#CE1126"], # Green, Yellow, Red
    "Mauritania": ["#00A95C", "#FFD700", "#D01C1F"], # Green, Gold (crescent/star), Red (bands)
    "Mauritius": ["#EA2839", "#1A206D", "#FFD500", "#00A551"], # Red, Blue, Yellow, Green
    "Morocco": ["#C1272D", "#006233"], # Red, Green (pentagram)
    "Mozambique": ["#009739", "#FCD116", "#000000", "#E41D1A", "#FFFFFF"], # Green, Yellow/Black, Red (triangle)
    "Namibia": ["#003580", "#D7141A", "#009A44", "#FFFFFF", "#FFC72C"], # Blue, Red, Green, White, Gold (sun)
    "Niger": ["#E05206", "#FFFFFF", "#0DB02B"], # Orange, White, Green, Orange (circle)
    "Nigeria": ["#008751", "#FFFFFF"], # Green, White, Green
    "Rwanda": ["#00A1DE", "#FFD700", "#20603D"], # Sky Blue, Yellow, Green
    "Sao Tome and Principe": ["#12AD2B", "#FCD116", "#D21034", "#000000"], # Green, Yellow, Red, Black (stars)
    "Senegal": ["#00853F", "#FDEF42", "#E31B23"], # Green, Yellow, Red (star is green)
    "Seychelles": ["#003F87", "#FCD856", "#D62828", "#FFFFFF", "#007A3D"], # Blue, Yellow, Red, White, Green
    "Sierra Leone": ["#1EB53A", "#FFFFFF", "#0072C6"], # Green, White, Light Blue
    "Somalia": ["#4189DD", "#FFFFFF"], # Light Blue, White (star)
    "South Africa": ["#E03C31", "#FFFFFF", "#007749", "#001489", "#000000", "#FFB612"], # Red, White, Green, Blue, Black, Yellow
    "South Sudan": ["#000000", "#D21034", "#0F47AF", "#007229", "#FFFFFF", "#FCDD09"], # Black, Red, Blue, Green, White, Yellow
    "Sudan": ["#D21034", "#FFFFFF", "#000000", "#007229"], # Red, White, Black, Green (triangle)
    "Tanzania": ["#1EB53A", "#FCD116", "#000000", "#00A3DD"], # Green/Blue (triangles), Yellow/Black (band)
    "Togo": ["#006A4E", "#FCD116", "#D21034", "#FFFFFF"], # Green/Yellow stripes, Red (canton with white star)
    "Tunisia": ["#E70013", "#FFFFFF"], # Red, White (circle with red crescent/star)
    "Uganda": ["#000000", "#FCDC04", "#D90000", "#FFFFFF"], # Black, Yellow, Red, White (crane disc)
    "Zambia": ["#198D44", "#DE2010", "#000000", "#EF7D00"], # Green, Red/Black/Orange (stripes/eagle)
    "Zimbabwe": ["#009539", "#FCE300", "#DE2010", "#000000", "#FFFFFF"], # Green, Yellow, Red, Black, White

    # Oceania
    "Australia": ["#00008B", "#FFFFFF", "#FF0000"], # Dark Blue, White (stars/Jack), Red (Jack)
    "Fiji": ["#62B5E5", "#FFFFFF", "#002868", "#CF142B"], # Light Blue, White/Red/Blue (shield/Jack)
    "Kiribati": ["#CE1126", "#0032A0", "#FCD116", "#FFFFFF"], # Red, Blue (waves), Yellow (sun/bird)
    "Marshall Islands": ["#003893", "#FF6700", "#FFFFFF"], # Blue, Orange/White (radiating bands/star)
    "Micronesia": ["#75AADB", "#FFFFFF"], # Light Blue, White (stars)
    "Nauru": ["#002B7F", "#FFC72C", "#FFFFFF"], # Dark Blue, Yellow (stripe), White (star)
    "New Zealand": ["#00247D", "#FFFFFF", "#CC142E"], # Blue, White (star border), Red (stars)
    "Palau": ["#4AADD6", "#FFDE00"], # Light Blue, Yellow (disc - off-center)
    "Papua New Guinea": ["#CE1126", "#000000", "#FCD116", "#FFFFFF"], # Red/Black, Yellow (bird), White (stars)
    "Samoa": ["#C8102E", "#002B7F", "#FFFFFF"], # Red, Blue (canton), White (stars)
    "Solomon Islands": ["#0051BA", "#215B33", "#FCD116"], # Blue/Green, Yellow (band)
    "Tonga": ["#C10000", "#FFFFFF"], # Red, White (canton with red cross)
    "Tuvalu": ["#0053A0", "#FFD100"], # Light Blue, Yellow (stars), plus Union Jack colors
    "Vanuatu": ["#D21034", "#009543", "#000000", "#FDCE12"], # Red/Green, Black, Yellow (fimbriation/emblem)
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

    if "Spain" in COUNTRY_COLORS and "Spain" in COUNTRY_CODES:
        print(f"\nExample for Spain:")
        print(f"  Colors: {COUNTRY_COLORS['Spain']}")
        print(f"  Code:   {COUNTRY_CODES['Spain']}")