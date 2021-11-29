import re
from unidecode import unidecode



#province/territory abbreviations from https://www150.statcan.gc.ca/n1/pub/92-195-x/2011001/geo/prov/tbl/tbl8-eng.htm
#things like newfoundland and labrador reduced to newfoundland
#this list of approx 1500 tweets will need to be checked manually afterwards for validity of can locations
#ie. just open tsv/csv in excel/pycharm and delete rows out of can
#also for report, mention english can speakers aren't the best sample of can. you need both
def get_canadian_locations_exact():
    country = ['ca', 'can']
    p1 = ['nl', 'tnl']
    p2 = ['pei', 'ipe', 'pe']
    p3 = ['ns', 'ne', 'né']
    p4 = ['nb']
    p5 = ['que', 'qc']
    p6 = ['ont', 'on']
    p7 = ['man' 'mb']
    p8 = ['sask', 'sk']
    p9 = ['alta', 'alb', 'ab']
    p10 = ['bc', 'cb']
    t1 = ['yt', 'yn']
    t2 = ['nwt', 'tno', 'nt']
    t3 = ['nvt', 'nt', 'nu']
    #notice nt both in t2 and t3, not important unless we weight sample by provinces, which is a bit too fancy

    all_canadian_geo_list = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
    all_canadian_geo_list += t1 + t2 + t3 + country
    all_canadian_geo = set(all_canadian_geo_list)
    return all_canadian_geo

def get_californian_cities_exact():
    cali_cities_list = ['san', 'santa', 'rio']
    cali_cities = set(cali_cities_list)
    return cali_cities

def all_wrong_locations_sub():
    bad_loc = get_bad_locations_sub()
    neb_loc = get_nebraska_cities_sub()
    cali_loc = get_californian_cities_sub()
    all_wrong_sub = set.union(bad_loc, neb_loc, cali_loc)
    return all_wrong_sub


def get_bad_locations_sub():
    popular_list = ['on earth', 'on the couch', 'yt channel', 'notifications on', 'on both sides', 'ca usa', 'ca uk', 'us canada', 'and canada']
    popular_list += ['on my', 'on a', 'on an', 'on the', 'on your', 'tweets on', 'can travel', 'lawse angelees', 'earth between mexico', 'northern ireland']
    popular_list += ['walton on thames', 'ochten', 'you can', 'qc ncr', 'canada   us', 'freedom bunker', 'can dm me']
    popular_list += ['on koo as', 'we can do', 'on yo mama', 'nu zillun', 'stoke on trent', 'southend on sea', 'i can be']
    popular_list += ['or canada', 'on twitter', 'on holiday', 'peace on', 'turn on', 'east bay, ca', 'bay area ca', 'ca  ignoring']
    popular_list += ['seen on', 'on nik', 'free state of ca', 'barrio echo parque', 'bay area  ca', 'nb muse', 'bc  fl', 'on planet']
    popular_list += ['on tour', 'where i can', 'mountain view  ca', 'canada   belarus', 'westeros  ca', 'lost angeles', 'ca united states']
    popular_list += ['wurundjeri land', 'land   naarm', 'yaegl land', 'dungeon ca', 'uk  nl', 'london uk', 'on hold', 'us  uk']
    popular_list += ['on this planet', 'fish on', 'ne hampshire']
    popular = set(popular_list)
    return popular

def get_nebraska_cities_sub():
    popular = ['auburn', 'fairbury', 'ohio']
    cities_1_10 = ['omaha', 'lincoln', 'bellevue', 'grand island', 'kearney', 'fremont', 'hastings', 'norfolk', 'papillion']
    #skipped 10 colombus
    cities_11_20 = ['north platte', 'la vista', 'scottsbluff', 'south sioux city', 'beatrice', 'gering', 'alliance', 'blair']
    locations_list = popular + cities_1_10 + cities_11_20
    locations = set(locations_list)
    return locations
    #skipped 16 lexington and 19 york

def get_californian_cities_sub():
    #I don't think i can put county here as of now. perhaps people say stuff like york county, ontario
    popular = ['hollywood', 'beverly hills', 'stanford', 'lake forest', 'newport beach', 'sacramento', 'buena park', 'galt', 'sonora']
    popular += ['laguna beach', 'palm_beach', 'hermosa beach', 'manhattan beach', 'daly city', 'prunedale', 'cathedral city', 'chino hills', 'placerville']
    popular += ['sonoma county', 'pacific palisades', 'half moon bay', 'north vallejo', 'palo alto', 'davis', 'encinitas', 'chesapeake', 'silicon valley']
    popular += ['sierra madre', 'menifee', 'simi valley', 'marina del rey', 'moreno valley', 'buena park', 'citrus heights', 'hmb ca', 'valencia']
    popular += ['palm desert', 'santee', 'hesperia', 'whittier', 'palm springs', 'malibu', 'bermuda dunes', 'laguna niguel', 'coachella valley']
    popular += ['marina  ca', 'mountain view  ca', 'capitola  ca', 'freedom  ca', 'camarillo', 'woodland hills', 'palos verdes', 'culver city']
    popular += ['lake tahoe', 'la jolla', 'perris', 'mission viejo']
    cities_1_10 = ['los angeles', 'fresno', 'long beach', 'oakland', 'bakersfield', 'anaheim']
    cities_11_20 = ['stockton', 'riverside', 'irvine', 'chula vista', 'fremont', 'modesto']
    cities_21_26 = ['fontana', 'oxnard', 'huntington beach', 'glendale', 'elk grove', ]
    #skipped 27 since it's ontario california lol
    cities_28_38 = ['rancho cucamonga', 'oceanside', 'lancaster', 'garden grove', 'salinas', 'hayward', 'corona', 'sunnyvale', 'pomona', 'escondido']
    cities_39_50 = ['roseville', 'torrance', 'fullerton', 'visalia', 'orange', 'pasadena', 'victorville', 'thousand oaks', 'simi valley', 'vallejo', 'concord']
    cities_51_60 = ['berkeley', 'clovis', 'fairfield', 'antioch', 'carlsbad', 'downey', 'costa mesa', 'murrieta', 'ventura']
    #skipped 54 which is richmond
    cali_cities_list = popular + cities_1_10 + cities_11_20 + cities_21_26 + cities_28_38 + cities_39_50 + cities_51_60
    cali_cities = set(cali_cities_list)
    return cali_cities
    #inglewood too

#hmm, some tweets were cut short like Grand Falls-Windsor, Newfoundl cause of the 30 char limit
def get_canadian_locations_sub():
    country = ['canada']
    p1 = ['newfoundland', 'labrador', 'terre neuve', 'labrador']
    p2 = ['prince edward']
    p3 = ['nova scotia', 'nouvelle ecosse']
    p4 = ['new brunswick', 'nouveau brunswick']
    p5 = ['quebec']
    p6 = ['ontario']
    p7 = ['manitoba']
    p8 = ['saskatchewan']
    p9 = ['alberta']
    p10 = ['british columbia', 'colombie britannique']
    t1 = ['yukon']
    t2 = ['northwest territories', 'territoires du nord ouest']
    t3 = ['nunavut']

    treaties = ['treaty 1', 'treaty 2', 'treaty 3', 'treaty 4', 'treaty 5', 'treaty 6', 'treaty 7', 'treaty 8', 'treaty 9', 'treaty 10', 'treaty 11']


    all_canadian_geo_list = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
    all_canadian_geo_list += t1 + t2 + t3 + country + treaties
    all_canadian_geo = set(all_canadian_geo_list)
    return all_canadian_geo

def is_tweet_canadian(tweet_loc):
    if tweet_loc == None:
        return False
    tweet_loc = tweet_loc.lower()
    #print(tweet_loc)
    tweet_loc = unidecode(tweet_loc)
    #print(tweet_loc)
    clean_tweet_loc = re.sub("[^0-9a-zA-Z]+", " ", tweet_loc)#for things like terre-neuve
    tweet_loc_words = clean_tweet_loc.split()
    can_locs_sub = get_canadian_locations_sub()
    can_locs_exact = get_canadian_locations_exact()
    cali_cities_exact = get_californian_cities_exact()

    for wrong_loc_sub in all_wrong_locations_sub():
        if wrong_loc_sub in clean_tweet_loc:
            return False
    for cali_cities_exact in cali_cities_exact:
        for tweet_word in tweet_loc_words:
            if cali_cities_exact == tweet_word:
                return False

    for can_loc_sub in can_locs_sub:
        if can_loc_sub in clean_tweet_loc:
            return True
    for can_loc_exact in can_locs_exact:
        for tweet_word in tweet_loc_words:
            if can_loc_exact == tweet_word:
                return True
    return False

def main():
    tweet_loc = 'quebec'
    print(is_tweet_canadian(tweet_loc))


if __name__ == '__main__':
    main()