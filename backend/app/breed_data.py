# ============================================================
# INDIAN CATTLE BREED AI
# BREED CHARACTERISTICS DATABASE
# ============================================================

from typing import Dict, Optional, List


# ============================================================
# BREED DATA
# ============================================================

BREED_DATA: Dict[str, Dict[str, str]] = {

    "Amritmahal": {
        "origin": "Karnataka, India",
        "type": "Cattle",
        "purpose": "Draft and agricultural work",
        "appearance": "Medium-sized, strong body with grey to white coat",
        "climate": "Adapted to warm and semi-dry conditions",
        "special_features": "Known for strength, endurance and working ability",
    },

    "Bachaur": {
        "origin": "Bihar, India",
        "type": "Cattle",
        "purpose": "Draft and agricultural work",
        "appearance": "Compact body with white to grey coat",
        "climate": "Well adapted to hot and dry conditions",
        "special_features": "Hardy breed suitable for farm work",
    },

    "Badri": {
        "origin": "Uttarakhand, India",
        "type": "Cattle",
        "purpose": "Milk and agricultural use",
        "appearance": "Small-sized hill cattle with varied coat colours",
        "climate": "Well adapted to Himalayan conditions",
        "special_features": "Hardy and adapted to mountainous terrain",
    },

    "Banni": {
        "origin": "Gujarat, India",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Medium to large body with dark or grey coat",
        "climate": "Highly adapted to hot and dry regions",
        "special_features": "Well suited to harsh desert-like environments",
    },

    "Bargur": {
        "origin": "Tamil Nadu, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Medium-sized cattle, commonly brown with white patches",
        "climate": "Adapted to hilly and dry conditions",
        "special_features": "Agile, strong and suitable for hill terrain",
    },

    "Bargur Buffalo": {
        "origin": "Tamil Nadu, India",
        "type": "Buffalo",
        "purpose": "Milk and agricultural use",
        "appearance": "Dark-coloured buffalo with strong body",
        "climate": "Adapted to warm conditions",
        "special_features": "Hardy local buffalo type",
    },

    "Belahi": {
        "origin": "Haryana and Punjab region, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Medium-sized cattle with white or grey coat",
        "climate": "Adapted to hot northern Indian climate",
        "special_features": "Hardy and suitable for local farming",
    },

    "Bhadawari": {
        "origin": "Uttar Pradesh and Madhya Pradesh, India",
        "type": "Buffalo",
        "purpose": "Milk production",
        "appearance": "Medium-sized buffalo, generally copper or brownish-black",
        "climate": "Adapted to hot climatic conditions",
        "special_features": "Known for relatively high milk fat content",
    },

    "Chhattisgarhi": {
        "origin": "Chhattisgarh, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Small to medium-sized cattle with varied coat colours",
        "climate": "Well adapted to tropical conditions",
        "special_features": "Hardy and suitable for agricultural work",
    },

    "Chilika": {
        "origin": "Odisha, India",
        "type": "Buffalo",
        "purpose": "Milk and agricultural use",
        "appearance": "Medium-sized dark-coloured buffalo",
        "climate": "Adapted to coastal and humid conditions",
        "special_features": "Well adapted to local coastal environments",
    },

    "Dagri": {
        "origin": "Gujarat, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Medium-sized cattle with light-coloured coat",
        "climate": "Adapted to warm and dry regions",
        "special_features": "Known for endurance and farm work",
    },

    "Dangi": {
        "origin": "Maharashtra and Gujarat, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Medium-sized cattle with white coat and dark markings",
        "climate": "Adapted to heavy rainfall areas",
        "special_features": "Known for tolerance to wet conditions",
    },

    "Deoni": {
        "origin": "Maharashtra, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Medium to large body, commonly white with black markings",
        "climate": "Adapted to semi-arid conditions",
        "special_features": "Dual-purpose breed",
    },

    "Gangatiri": {
        "origin": "Uttar Pradesh and Bihar, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "White to grey body with medium build",
        "climate": "Adapted to hot northern Indian climate",
        "special_features": "Hardy dual-purpose cattle",
    },

    "Gaolao": {
        "origin": "Maharashtra and Madhya Pradesh, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Medium-sized white or grey cattle",
        "climate": "Adapted to dry and semi-arid conditions",
        "special_features": "Fast and active draft animal",
    },

    "Ghumusari": {
        "origin": "Odisha, India",
        "type": "Cattle",
        "purpose": "Draft and agricultural work",
        "appearance": "Small to medium-sized cattle with varied coat",
        "climate": "Adapted to tropical conditions",
        "special_features": "Hardy local breed",
    },

    "Gir": {
        "origin": "Gujarat, India",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Distinctive domed forehead, long ears and red or white-speckled coat",
        "climate": "Highly adapted to hot and dry conditions",
        "special_features": "Excellent dairy breed with strong heat tolerance",
    },

    "Gojri": {
        "origin": "Jammu and Kashmir region, India",
        "type": "Cattle",
        "purpose": "Milk and agricultural use",
        "appearance": "Medium-sized cattle with varied coat colours",
        "climate": "Adapted to hilly conditions",
        "special_features": "Hardy breed suited to mountain regions",
    },

    "Hallikar": {
        "origin": "Karnataka, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Strong medium-sized body with grey coat",
        "climate": "Adapted to dry and warm conditions",
        "special_features": "Excellent endurance and working ability",
    },

    "Hariana": {
        "origin": "Haryana, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "White or light grey body with strong frame",
        "climate": "Adapted to hot northern plains",
        "special_features": "Popular dual-purpose breed",
    },

    "Himachali Pahari": {
        "origin": "Himachal Pradesh, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Small hill cattle with varied coat colours",
        "climate": "Adapted to cool mountainous conditions",
        "special_features": "Hardy and suitable for mountain terrain",
    },

    "Jaffarabadi": {
        "origin": "Gujarat, India",
        "type": "Buffalo",
        "purpose": "Milk production",
        "appearance": "Large black buffalo with heavy body and curved horns",
        "climate": "Adapted to warm climates",
        "special_features": "One of India's large dairy buffalo breeds",
    },

    "Kangayam": {
        "origin": "Tamil Nadu, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Strong compact body, generally grey or white",
        "climate": "Excellent adaptation to hot and dry conditions",
        "special_features": "Strong, hardy and famous for endurance",
    },

    "Kankrej": {
        "origin": "Gujarat and Rajasthan, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Large grey or silver-grey cattle with lyre-shaped horns",
        "climate": "Adapted to hot and dry regions",
        "special_features": "Strong dual-purpose breed",
    },

    "Khillar": {
        "origin": "Maharashtra and Karnataka, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Compact muscular body with grey or white coat",
        "climate": "Adapted to dry and semi-arid regions",
        "special_features": "Fast, strong and hardy draft breed",
    },

    "Krishna Valley": {
        "origin": "Karnataka and Maharashtra, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Large white or grey cattle with strong body",
        "climate": "Adapted to semi-arid regions",
        "special_features": "Good strength and dual-purpose characteristics",
    },

    "Malnad Gidda": {
        "origin": "Karnataka, India",
        "type": "Cattle",
        "purpose": "Milk and agricultural use",
        "appearance": "Small-sized cattle with compact body",
        "climate": "Adapted to humid and hilly regions",
        "special_features": "Hardy and disease-resistant local cattle",
    },

    "Mehsana": {
        "origin": "Gujarat, India",
        "type": "Buffalo",
        "purpose": "Milk production",
        "appearance": "Black buffalo with strong body and curved horns",
        "climate": "Adapted to hot and dry climate",
        "special_features": "Important dairy buffalo breed",
    },

    "Murrah": {
        "origin": "Haryana and Punjab, India",
        "type": "Buffalo",
        "purpose": "Milk production",
        "appearance": "Large black buffalo with tightly curled horns",
        "climate": "Adapted to warm conditions",
        "special_features": "One of India's most important dairy buffalo breeds",
    },

    "Nagori": {
        "origin": "Rajasthan, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "White or grey medium-sized cattle",
        "climate": "Excellent adaptation to hot and dry climate",
        "special_features": "Fast and strong draft breed",
    },

    "Nagpuri": {
        "origin": "Maharashtra, India",
        "type": "Buffalo",
        "purpose": "Milk and agricultural use",
        "appearance": "Medium-sized black buffalo with long horns",
        "climate": "Adapted to hot and dry conditions",
        "special_features": "Hardy buffalo suitable for dry regions",
    },

    "Nili Ravi": {
        "origin": "Punjab region",
        "type": "Buffalo",
        "purpose": "Milk production",
        "appearance": "Black buffalo, often with white markings on forehead and tail",
        "climate": "Adapted to warm conditions",
        "special_features": "High-quality dairy buffalo",
    },

    "Nimari": {
        "origin": "Madhya Pradesh, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Medium-sized cattle with red or white markings",
        "climate": "Adapted to hot and semi-arid conditions",
        "special_features": "Hardy dual-purpose breed",
    },

    "Ongole": {
        "origin": "Andhra Pradesh, India",
        "type": "Cattle",
        "purpose": "Draft and breeding",
        "appearance": "Large white or light-grey muscular cattle",
        "climate": "Highly adapted to hot conditions",
        "special_features": "Strong, hardy breed with international recognition",
    },

    "Pandharpuri": {
        "origin": "Maharashtra, India",
        "type": "Buffalo",
        "purpose": "Milk production",
        "appearance": "Black buffalo with very long, backward-curving horns",
        "climate": "Adapted to warm and dry conditions",
        "special_features": "Distinctive extremely long horns",
    },

    "Poda Thurpu": {
        "origin": "Andhra Pradesh and Telangana region, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Small to medium-sized cattle",
        "climate": "Adapted to hot conditions",
        "special_features": "Hardy working cattle",
    },

    "Ponwar": {
        "origin": "Uttar Pradesh, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Small-sized cattle with dark and white markings",
        "climate": "Adapted to northern Indian conditions",
        "special_features": "Hardy local breed",
    },

    "Pulikulam": {
        "origin": "Tamil Nadu, India",
        "type": "Cattle",
        "purpose": "Draft and traditional livestock activities",
        "appearance": "Medium-sized grey cattle with strong body",
        "climate": "Highly adapted to hot and dry conditions",
        "special_features": "Known for endurance and traditional Jallikattu association",
    },

    "Punganur": {
        "origin": "Andhra Pradesh, India",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Very small-sized cattle with short stature",
        "climate": "Adapted to dry and warm conditions",
        "special_features": "One of the smallest cattle breeds in the world",
    },

    "Rathi": {
        "origin": "Rajasthan, India",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Medium-sized cattle with white coat and reddish-brown patches",
        "climate": "Adapted to hot and dry climate",
        "special_features": "Good dairy breed with strong heat tolerance",
    },

    "Red Kandhari": {
        "origin": "Maharashtra, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Distinctive deep red coat",
        "climate": "Adapted to semi-arid conditions",
        "special_features": "Hardy dual-purpose breed",
    },

    "Red Sindhi": {
        "origin": "Sindh region, historically India",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Distinctive deep red coat",
        "climate": "Highly adapted to hot climates",
        "special_features": "Heat tolerant dairy breed",
    },

    "Sahiwal": {
        "origin": "Punjab region",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Reddish-brown coat with loose skin and strong body",
        "climate": "Highly adapted to hot climates",
        "special_features": "Important South Asian dairy breed",
    },

    "Shweta Kapila": {
        "origin": "Maharashtra, India",
        "type": "Cattle",
        "purpose": "Milk and agricultural use",
        "appearance": "Light or white-coated cattle",
        "climate": "Adapted to warm conditions",
        "special_features": "Hardy local cattle",
    },

    "Siri": {
        "origin": "Sikkim and West Bengal region, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "Small hill cattle with varied coat colours",
        "climate": "Adapted to cool mountainous environments",
        "special_features": "Suitable for hilly terrain",
    },

    "Surti": {
        "origin": "Gujarat, India",
        "type": "Buffalo",
        "purpose": "Milk production",
        "appearance": "Medium-sized black buffalo with sickle-shaped horns",
        "climate": "Adapted to warm conditions",
        "special_features": "Good dairy buffalo",
    },

    "Tharparkar": {
        "origin": "Rajasthan, India",
        "type": "Cattle",
        "purpose": "Milk and draft",
        "appearance": "White or light grey cattle with strong body",
        "climate": "Excellent adaptation to hot and arid conditions",
        "special_features": "Hardy dual-purpose breed with strong heat tolerance",
    },

    "Toda Buffalo": {
        "origin": "Nilgiri Hills, Tamil Nadu, India",
        "type": "Buffalo",
        "purpose": "Milk and traditional livestock use",
        "appearance": "Large dark buffalo with distinctive crescent-shaped horns",
        "climate": "Adapted to cool highland conditions",
        "special_features": "Associated with the Toda community and Nilgiri ecosystem",
    },

    "Umblachery": {
        "origin": "Tamil Nadu, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Small to medium-sized cattle, generally grey or white",
        "climate": "Adapted to hot and humid conditions",
        "special_features": "Well suited to agricultural work in coastal Tamil Nadu",
    },

    "Vechur": {
        "origin": "Kerala, India",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Very small-sized cattle with compact body",
        "climate": "Highly adapted to hot and humid conditions",
        "special_features": "Known as one of the world's smallest cattle breeds",
    },
}


# ============================================================
# ADDITIONAL BREED PROFILES
# Source: Indian_Cattle_Buffalo_77_State_Wise_Same_Format.xlsx
# ============================================================

BREED_DATA.update({
    "Luit (Swamp)": {"origin": "Assam; Manipur (India)", "type": "Buffalo", "purpose": "Milk + draught", "appearance": "Dark, compact", "climate": "Hot, humid", "special_features": "Swamp adapted"},
    "Manah": {"origin": "Assam (India)", "type": "Buffalo", "purpose": "Milk + draught", "appearance": "Black, compact", "climate": "Hot, humid", "special_features": "Swamp-region adapted"},
    "Lakhimi": {"origin": "Assam (India)", "type": "Cattle", "purpose": "Milk + draught", "appearance": "Grey/white, medium frame", "climate": "Hot, humid", "special_features": "Adapted to Assam"},
    "Purnea": {"origin": "Bihar (India)", "type": "Cattle", "purpose": "Draught", "appearance": "White/grey, medium frame", "climate": "Hot, humid", "special_features": "Hardy"},
    "Kosali": {"origin": "Chhattisgarh (India)", "type": "Cattle", "purpose": "Draught", "appearance": "White/grey, compact", "climate": "Hot, humid", "special_features": "Hardy"},
    "Medini": {"origin": "Jharkhand (India)", "type": "Cattle", "purpose": "Draught + milk", "appearance": "White/grey, sturdy", "climate": "Hot, humid", "special_features": "Hardy"},
    "Dharwadi": {"origin": "Karnataka (India)", "type": "Buffalo", "purpose": "Milk + draught", "appearance": "Black, medium horns", "climate": "Hot, humid", "special_features": "Hardy"},
    "Malvi": {"origin": "Madhya Pradesh (India)", "type": "Cattle", "purpose": "Draught", "appearance": "White/grey, sturdy", "climate": "Hot, dry", "special_features": "Hardy"},
    "Marathwadi": {"origin": "Maharashtra (India)", "type": "Buffalo", "purpose": "Milk + draught", "appearance": "Black, medium horns", "climate": "Hot, dry", "special_features": "Hardy"},
    "Melghati": {"origin": "Maharashtra (India)", "type": "Buffalo", "purpose": "Milk + draught", "appearance": "Black, sturdy", "climate": "Hot, dry", "special_features": "Hardy"},
    "Purnathadi": {"origin": "Maharashtra (India)", "type": "Buffalo", "purpose": "Milk + draught", "appearance": "Black, medium horns", "climate": "Hot, dry", "special_features": "Hardy"},
    "Kathani": {"origin": "Maharashtra (India)", "type": "Cattle", "purpose": "Draught", "appearance": "Grey/white, sturdy", "climate": "Hot, dry", "special_features": "Hardy"},
    "Konkan Kapila": {"origin": "Maharashtra; Goa (India)", "type": "Cattle", "purpose": "Milk + draught", "appearance": "Red/white, medium horns", "climate": "Hot, humid", "special_features": "Coastal adapted"},
    "Masilum": {"origin": "Meghalaya (India)", "type": "Cattle", "purpose": "Milk + draught", "appearance": "Dark/black, small frame", "climate": "Hilly, humid", "special_features": "Hill adapted"},
    "Thutho": {"origin": "Nagaland (India)", "type": "Cattle", "purpose": "Milk + draught", "appearance": "Brown/black, medium frame", "climate": "Hilly, humid", "special_features": "Hill adapted"},
    "Kalahandi": {"origin": "Odisha (India)", "type": "Buffalo", "purpose": "Milk + draught", "appearance": "Black, sturdy", "climate": "Hot, humid", "special_features": "Hardy"},
    "Manda": {"origin": "Odisha (India)", "type": "Buffalo", "purpose": "Milk + draught", "appearance": "Black, sturdy", "climate": "Hot, humid", "special_features": "Hardy"},
    "Binjharpuri": {"origin": "Odisha (India)", "type": "Cattle", "purpose": "Milk + draught", "appearance": "Grey/white, medium frame", "climate": "Hot, humid", "special_features": "Dual-purpose"},
    "Khariar": {"origin": "Odisha (India)", "type": "Cattle", "purpose": "Draught", "appearance": "Grey/white", "climate": "Hot, humid", "special_features": "Hardy"},
    "Motu": {"origin": "Odisha; Chhattisgarh; Andhra Pradesh (India)", "type": "Cattle", "purpose": "Draught", "appearance": "Grey/white, sturdy", "climate": "Hot, humid", "special_features": "Hardy"},
    "Mewati": {"origin": "Rajasthan; Haryana; Uttar Pradesh (India)", "type": "Cattle", "purpose": "Milk + draught", "appearance": "White/grey, dark neck", "climate": "Hot, dry", "special_features": "Dual-purpose"},
    "Nari": {"origin": "Rajasthan; Gujarat (India)", "type": "Cattle", "purpose": "Draught", "appearance": "Grey/white, medium horns", "climate": "Hot, arid", "special_features": "Arid adapted"},
    "Sanchori": {"origin": "Rajasthan (India)", "type": "Cattle", "purpose": "Draught", "appearance": "White/grey, medium frame", "climate": "Hot, arid", "special_features": "Arid adapted"},
    "Toda": {"origin": "Tamil Nadu (India)", "type": "Buffalo", "purpose": "Milk", "appearance": "Grey/black, large curved horns", "climate": "Hilly, humid", "special_features": "Nilgiri adapted"},
    "Kenkatha": {"origin": "Uttar Pradesh; Madhya Pradesh (India)", "type": "Cattle", "purpose": "Draught", "appearance": "Grey/white, compact", "climate": "Hot, dry", "special_features": "Hardy"},
    "Kherigarh": {"origin": "Uttar Pradesh (India)", "type": "Cattle", "purpose": "Draught", "appearance": "White/grey, medium horns", "climate": "Hot, dry", "special_features": "Hardy"},
    "Rohilkhandi": {"origin": "Uttar Pradesh (India)", "type": "Cattle", "purpose": "Draught + milk", "appearance": "White/grey, sturdy", "climate": "Hot, humid", "special_features": "Hardy"},
        "Alambadi": {
        "origin": "Tamil Nadu, India",
        "type": "Cattle",
        "purpose": "Draft work",
        "appearance": "Medium-sized cattle with grey to dark grey coat",
        "climate": "Adapted to hot and dry conditions",
        "special_features": "Hardy breed known for strength and endurance",
    },

    "Ayrshire": {
        "origin": "Scotland",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Medium-sized dairy cattle with red and white markings",
        "climate": "Adapted to cool and temperate conditions",
        "special_features": "Known for good milk production and adaptability",
    },

    "Brown_Swiss": {
        "origin": "Switzerland",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Large cattle with brown to grey-brown coat",
        "climate": "Adaptable to different climatic conditions",
        "special_features": "Known for milk production, strength and longevity",
    },

    "Guernsey": {
        "origin": "Guernsey, Channel Islands",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Medium-sized cattle with reddish-brown and white markings",
        "climate": "Adapted to temperate conditions",
        "special_features": "Dairy breed known for rich milk",
    },

    "Holstein_Friesian": {
        "origin": "Netherlands",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Large cattle with distinctive black-and-white markings",
        "climate": "Adaptable with appropriate management",
        "special_features": "Widely known for high milk production",
    },

    "Jersey": {
        "origin": "Jersey, Channel Islands",
        "type": "Cattle",
        "purpose": "Milk production",
        "appearance": "Small to medium-sized cattle with fawn to light-brown coat",
        "climate": "Adaptable to warm and temperate conditions",
        "special_features": "Known for milk with relatively high fat content",
    },

    "Kasargod": {
        "origin": "Kerala, India",
        "type": "Cattle",
        "purpose": "Milk and agricultural use",
        "appearance": "Small-sized cattle with compact body and varied coat colours",
        "climate": "Adapted to warm and humid conditions",
        "special_features": "Hardy cattle adapted to local Kerala conditions",
    },

    "Ladakhi": {
        "origin": "Ladakh, India",
        "type": "Cattle",
        "purpose": "Milk and agricultural use",
        "appearance": "Small-sized cattle adapted to high-altitude environments",
        "climate": "Adapted to cold and high-altitude conditions",
        "special_features": "Hardy breed adapted to the harsh Ladakh environment",
    },

    "Red_Dane": {
        "origin": "Denmark",
        "type": "Cattle",
        "purpose": "Milk and beef production",
        "appearance": "Medium to large cattle with red to reddish-brown coat",
        "climate": "Adapted to temperate conditions",
        "special_features": "Dual-purpose breed with good dairy characteristics",
    },
})


# ============================================================
# NORMALIZE BREED NAME
# ============================================================

def _normalize_breed_name(breed_name: str) -> str:
    """
    Convert different representations of a breed name
    into a common searchable format.

    Examples:
        Red_Sindhi     -> red sindhi
        red-sindhi     -> red sindhi
        RED SINDHI     -> red sindhi
        " Gir "        -> gir
    """

    if breed_name is None:
        return ""

    return (
        str(breed_name)
        .strip()
        .replace("_", " ")
        .replace("-", " ")
        .replace("  ", " ")
        .lower()
    )


# ============================================================
# GET BREED INFORMATION
# ============================================================

def get_breed_info(breed_name: str) -> Optional[Dict[str, str]]:
    """
    Return complete information for a breed.

    Supports:
        Gir
        gir
        GIR
        Gir
        Red_Sindhi
        Red-Sindhi
    """

    if not breed_name:
        return None

    requested = _normalize_breed_name(breed_name)

    for official_name, information in BREED_DATA.items():

        official_normalized = _normalize_breed_name(official_name)

        if official_normalized == requested:
            return information

    return None


# ============================================================
# GET CANONICAL BREED NAME
# ============================================================

def get_canonical_breed_name(breed_name: str) -> Optional[str]:
    """
    Return the official breed name stored in BREED_DATA.

    Also handles names used by the trained AI model.
    """

    if not breed_name:
        return None

    requested = _normalize_breed_name(breed_name)

    # --------------------------------------------------------
    # MODEL NAME ALIASES
    # --------------------------------------------------------

    aliases = {
        "khillari": "Khillar",
        "poda thirupu": "Poda Thurpu",
        "bhelai": "Belahi",
        "gangatari": "Gangatiri",
        "ghumsari": "Ghumusari",
        "luit": "Luit (Swamp)",
        "marathwada": "Marathwadi",
    }

    # --------------------------------------------------------
    # CHECK ALIAS
    # --------------------------------------------------------

    if requested in aliases:
        return aliases[requested]

    # --------------------------------------------------------
    # NORMAL DATABASE SEARCH
    # --------------------------------------------------------

    for official_name in BREED_DATA.keys():

        if _normalize_breed_name(
            official_name
        ) == requested:

            return official_name

    return None


# ============================================================
# CHECK WHETHER BREED EXISTS
# ============================================================

def breed_exists(breed_name: str) -> bool:
    """
    Check whether a breed exists in the database.
    """

    return get_breed_info(breed_name) is not None


# ============================================================
# GET ALL BREED NAMES
# ============================================================

def get_all_breed_names() -> List[str]:
    """
    Return all official breed names.
    """

    return list(BREED_DATA.keys())


# ============================================================
# GET BREEDS BY TYPE
# ============================================================

def get_breeds_by_type(breed_type: str) -> List[str]:
    """
    Return breeds filtered by type.

    Example:
        get_breeds_by_type("Cattle")
        get_breeds_by_type("Buffalo")
    """

    if not breed_type:
        return []

    requested_type = str(breed_type).strip().lower()

    return [
        breed_name
        for breed_name, information in BREED_DATA.items()
        if information["type"].lower() == requested_type
    ]


# ============================================================
# GET BREED COUNT
# ============================================================

def get_breed_count() -> int:
    """
    Return total number of breeds in the database.
    """

    return len(BREED_DATA)


# ============================================================
# SEARCH BREEDS
# ============================================================

def search_breeds(search_text: str) -> List[str]:
    """
    Search breed names.

    Example:
        search_breeds("gir")
        search_breeds("red")
        search_breeds("buffalo")
    """

    if not search_text:
        return []

    query = _normalize_breed_name(search_text)

    return [
        breed_name
        for breed_name in BREED_DATA
        if query in _normalize_breed_name(breed_name)
    ]


# ============================================================
# TEST DATABASE
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("INDIAN CATTLE BREED AI")
    print("BREED DATABASE TEST")
    print("=" * 60)

    # Total breeds
    print(f"\nTotal breeds: {get_breed_count()}")

    # Test Gir
    print("\nTesting Gir:")
    print(get_breed_info("Gir"))

    # Test lowercase
    print("\nTesting lowercase:")
    print(get_breed_info("gir"))

    # Test underscore
    print("\nTesting underscore:")
    print(get_breed_info("Red_Sindhi"))

    # Test hyphen
    print("\nTesting hyphen:")
    print(get_breed_info("Red-Sindhi"))

    # Canonical name
    print("\nCanonical name:")
    print(get_canonical_breed_name("red_sindhi"))

    # Check breed
    print("\nBreed exists:")
    print("Gir:", breed_exists("Gir"))
    print("Unknown:", breed_exists("Unknown Breed"))

    # Cattle count
    print("\nCattle breeds:")
    cattle_breeds = get_breeds_by_type("Cattle")
    print(f"Count: {len(cattle_breeds)}")

    # Buffalo count
    print("\nBuffalo breeds:")
    buffalo_breeds = get_breeds_by_type("Buffalo")
    print(f"Count: {len(buffalo_breeds)}")

    # Search
    print("\nSearch: 'red'")
    print(search_breeds("red"))

    print("\n" + "=" * 60)
    print("DATABASE TEST COMPLETED")
    print("=" * 60)
