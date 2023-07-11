import re 
import csv


DateOfInsertInList = []
Rating = [] #8
ReleaseDate = [] #13
Genres = []
Runtime = [] #9
count = 0
GenderToSearch = "Horror"

with open("WATCHLIST.csv", mode="r", encoding="utf8") as OpenFile:
    FileContent = csv.reader(OpenFile)
    next(FileContent)  # Supprime la première ligne car pas de films présents dessus
    
    for row in FileContent:
        Genres.append(row[11])
        DateOfInsertInList.append(row[3])
        Rating.append(row[8])
        ReleaseDate.append(row[13])
        Runtime.append(row[9])
        if GenderToSearch in row[11]:
            print(row[5])
            count = count + 1
    print(count)
def LongestWatch():
    Total = 0 
    Longest = 0
    for EnumerationOfTime in Runtime:
        Total = int(Total) + int(EnumerationOfTime)
        if int(EnumerationOfTime) > Longest:
            Longest = int(EnumerationOfTime) 
    print("Durée total de visionage de films :",round((Total/60),1),"heures")
    print("Durée du film le plus long :",Longest,"minutes")


def StatGENDER():
    GenderSeparated = []
    AllDifferentGenders = []
    #Action,Adventure,SciFi,Horror,Family,Drama,Romance    = 0
    for EnumerationOfGenres in Genres:
        GenderSeparated = GenderSeparated + EnumerationOfGenres.split(",")
    AllDifferentGenders = set(GenderSeparated)

    
    
    for Genders in AllDifferentGenders:
        PercentGenders = {}
        PercentGenders[Genders] = round(GenderSeparated.count(Genders)/len(GenderSeparated)*100,2)
        print(PercentGenders)

    

        
    
