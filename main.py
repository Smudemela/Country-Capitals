cc = {
    "afghanistan": "kabul",
    "albania": "tirana",
    "algeria": "algiers",
    "andorra": "andorra la vella",
    "angola": "luanda",
    "antigua and barbuda": "saint john's",
    "argentina": "buenos aires",
    "armenia": "yerevan",
    "australia": "canberra",
    "austria": "vienna",
    "azerbaijan": "baku",
    "bahamas": "nassau",
    "bahrain": "manama",
    "bangladesh": "dhaka",
    "barbados": "bridgetown",
    "belarus": "minsk",
    "belgium": "brussels",
    "belize": "belmopan",
    "benin": "porto-novo",
    "bhutan": "thimphu",
    "bolivia": "sucre",
    "bosnia and herzegovina": "sarajevo",
    "botswana": "gaborone",
    "brazil": "brasilia",
    "brunei": "bandar seri begawan",
    "bulgaria": "sofia",
    "burkina faso": "ouagadougou",
    "burundi": "gitega",
    "cabo verde": "praia",
    "cambodia": "phnom penh",
    "cameroon": "yaounde",
    "canada": "ottawa",
    "central african republic": "bangui",
    "chad": "n'djamena",
    "chile": "santiago",
    "china": "beijing",
    "colombia": "bogota",
    "comoros": "moroni",
    "congo (brazzaville)": "brazzaville",
    "congo (kinshasa)": "kinshasa",
    "costa rica": "san jose",
    "croatia": "zagreb",
    "cuba": "havana",
    "cyprus": "nicosia",
    "czech republic": "prague",
    "denmark": "copenhagen",
    "djibouti": "djibouti",
    "dominica": "roseau",
    "dominican republic": "santo domingo",
    "ecuador": "quito",
    "egypt": "cairo",
    "el salvador": "san salvador",
    "equatorial guinea": "malabo",
    "eritrea": "asmara",
    "estonia": "tallinn",
    "eswatini": "mbabane",
    "ethiopia": "addis ababa",
    "fiji": "suva",
    "finland": "helsinki",
    "france": "paris",
    "gabon": "libreville",
    "gambia": "banjul",
    "georgia": "tbilisi",
    "germany": "berlin",
    "ghana": "accra",
    "greece": "athens",
    "grenada": "st. george's",
    "guatemala": "guatemala city",
    "guinea": "conakry",
    "guinea-bissau": "bissau",
    "guyana": "georgetown",
    "haiti": "port-au-prince",
    "honduras": "tegucigalpa",
    "hungary": "budapest",
    "iceland": "reykjavik",
    "india": "new delhi",
    "indonesia": "jakarta",
    "iran": "tehran",
    "iraq": "baghdad",
    "ireland": "dublin",
    "israel": "jerusalem",
    "italy": "rome",
    "jamaica": "kingston",
    "japan": "tokyo",
    "jordan": "amman",
    "kazakhstan": "astana",
    "kenya": "nairobi",
    "kiribati": "tarawa",
    "korea, north": "pyongyang",
    "korea, south": "seoul",
    "kosovo": "pristina",
    "kuwait": "kuwait city",
    "kyrgyzstan": "bishkek",
    "laos": "vientiane",
    "latvia": "riga",
    "lebanon": "beirut",
    "lesotho": "maseru",
    "liberia": "monrovia",
    "libya": "tripoli",
    "liechtenstein": "vaduz",
    "lithuania": "vilnius",
    "luxembourg": "luxembourg",
    "madagascar": "antananarivo",
    "malawi": "lilongwe",
    "malaysia": "kuala lumpur",
    "maldives": "male",
    "mali": "bamako",
    "malta": "valletta",
    "marshall islands": "majuro",
    "mauritania": "nouakchott",
    "mauritius": "port louis",
    "mexico": "mexico city",
    "micronesia": "palikir",
    "moldova": "chisinau",
    "monaco": "monaco",
    "mongolia": "ulaanbaatar",
    "montenegro": "podgorica",
    "morocco": "rabat",
    "mozambique": "maputo",
    "myanmar": "naypyidaw",
    "namibia": "windhoek",
    "nauru": "yaren",
    "nepal": "kathmandu",
    "netherlands": "amsterdam",
    "new zealand": "wellington",
    "nicaragua": "managua",
    "niger": "niamey",
    "nigeria": "abuja",
    "north macedonia": "skopje",
    "norway": "oslo",
    "oman": "muscat",
    "pakistan": "islamabad",
    "palau": "ngerulmud",
    "panama": "panama city",
    "papua new guinea": "port moresby",
    "paraguay": "asuncion",
    "peru": "lima",
    "philippines": "manila",
    "poland": "warsaw",
    "portugal": "lisbon",
    "qatar": "doha",
    "romania": "bucharest",
    "russia": "moscow",
    "rwanda": "kigali",
    "saint kitts and nevis": "basseterre",
    "saint lucia": "castries",
    "saint vincent and the grenadines": "kingstown",
    "samoa": "apia",
    "san marino": "san marino",
    "sao tome and principe": "sao tome",
    "saudi arabia": "riyadh",
    "senegal": "dakar",
    "serbia": "belgrade",
    "seychelles": "victoria",
    "sierra leone": "freetown",
    "singapore": "singapore",
    "slovakia": "bratislava",
    "slovenia": "ljubljana",
    "solomon islands": "honiara",
    "somalia": "mogadishu",
    "south africa": "pretoria",
    "south sudan": "juba",
    "spain": "madrid",
    "sri lanka": "sri jayawardenepura kotte",
    "sudan": "khartoum",
    "suriname": "paramaribo",
    "sweden": "stockholm",
    "switzerland": "bern",
    "syria": "damascus",
    "taiwan": "taipei",
    "tajikistan": "dushanbe",
    "tanzania": "dodoma",
    "thailand": "bangkok",
    "timor-leste": "dili",
    "togo": "lome",
    "tonga": "nuku'alofa",
    "trinidad and tobago": "port of spain",
    "tunisia": "tunis",
    "turkey": "ankara",
    "turkmenistan": "ashgabat",
    "tuvalu": "funafuti",
    "uganda": "kampala",
    "ukraine": "kyiv",
    "united arab emirates": "abu dhabi",
    "united kingdom": "london",
    "united states": "washington, d.c.",
    "uruguay": "montevideo",
    "uzbekistan": "tashkent",
    "vanuatu": "port vila",
    "vatican city": "vatican city",
    "venezuela": "caracas",
    "vietnam": "hanoi",
    "yemen": "sana'a",
    "zambia": "lusaka",
    "zimbabwe": "harare"
}


c = input("Give me a country and I will tell the capitial city: ")

print(cc.get(c.lower(), "Country not found (maybe typo?)"))
