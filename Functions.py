def duplic(nba):
    duplicates= nba[nba.duplicated(subset=["Name"], keep=False)]
    if duplicates.empty:
        print("No duplicate names in the nba DataFrame!")
    else:
        print("People found with the same name")
