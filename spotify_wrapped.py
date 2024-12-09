import pandas as pd
import re
from datetime import datetime
from collections import Counter

CONFIG = {
    'columnA-name': 'date',
    'columnB-name' :'song',
    'columnC-name': 'artist'
}

WRAP = "" # Insert Google Sheet link between quotes

if WRAP == "" or WRAP is None:
    print("WRAP value not defined. Please configure the value to continue.")
    exit()

current_datetime = datetime.now()
current_month = current_datetime.strftime("%B") # Automatically computes current month if you want to do it monthly
current_month = "2024"

google_sheets_link = WRAP

def convert_google_sheet_url(url):
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'

    # Replace function to construct the new URL for CSV export
    # If gid is present in the URL, it includes it in the export URL, otherwise, it's omitted
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'  # noqa: E731

    # Replace using regex
    new_url = re.sub(pattern, replacement, url)

    return new_url

pandas_url = convert_google_sheet_url(google_sheets_link)

df = pd.read_csv(pandas_url)
artist = CONFIG['columnC-name']
try:
    counts = Counter(df[artist])
    wrapped_artist = CONFIG['columnC-name']
    wrapped_song = CONFIG['columnB-name']
except (KeyError, AttributeError):
    print("Please check your google spreadsheet and ensure the headers both exist and match the config.")
    quit()


df_date = df[CONFIG['columnA-name']]

print("\n")
if df_date.str.contains(f'{current_month}').any():
    wrapped = (df[df_date.str.contains(f'{current_month}')])
    print(f"JANUARY SONG NUMBER: {len(df[df_date.str.contains('January')])} (ROUGHLY {3*len(df[df_date.str.contains('January')]) / 60} HOURS)")
    print(f"FEBRUARY SONG NUMBER: {len(df[df_date.str.contains('February')])} (ROUGHLY {3*len(df[df_date.str.contains('February')]) / 60} HOURS)")
    print(f"MARCH SONG NUMBER: {len(df[df_date.str.contains('March')])} (ROUGHLY {3*len(df[df_date.str.contains('March')]) / 60} HOURS)")
    print(f"APRIL SONG NUMBER: {len(df[df_date.str.contains('April')])} (ROUGHLY {3*len(df[df_date.str.contains('April')]) / 60} HOURS)")
    print(f"MAY SONG NUMBER: {len(df[df_date.str.contains('May')])} (ROUGHLY {3*len(df[df_date.str.contains('May')]) / 60} HOURS)")
    print(f"JUNE SONG NUMBER: {len(df[df_date.str.contains('June')])} (ROUGHLY {3*len(df[df_date.str.contains('June')]) / 60} HOURS)")
    print(f"JULY SONG NUMBER: {len(df[df_date.str.contains('July')])} (ROUGHLY {3*len(df[df_date.str.contains('July')]) / 60} HOURS)")
    print(f"AUGUST SONG NUMBER: {len(df[df_date.str.contains('August')])} (ROUGHLY {3*len(df[df_date.str.contains('August')]) / 60} HOURS)")
    print(f"SEPTEMBER SONG NUMBER: {len(df[df_date.str.contains('September')])} (ROUGHLY {3*len(df[df_date.str.contains('September')]) / 60} HOURS)")
    print(f"OCTOBER SONG NUMBER: {len(df[df_date.str.contains('October')])} (ROUGHLY {3*len(df[df_date.str.contains('October')]) / 60} HOURS)")
    print(f"NOVEMBER SONG NUMBER: {len(df[df_date.str.contains('November')])} (ROUGHLY {3*len(df[df_date.str.contains('November')]) / 60} HOURS)")
    print(f"DECEMBER SONG NUMBER: {len(df[df_date.str.contains('December')])} (ROUGHLY {3*len(df[df_date.str.contains('December')]) / 60} HOURS)")

print("\n")

counts_1 = Counter(wrapped[wrapped_artist])
counts_2 = Counter(wrapped[wrapped_song])

most_popular_artist = dict()
most_popular_song = dict()

print(f"I LISTENED TO {len(counts_1.items())} DIFFERENT ARTISTS IN 2024\n")

print(f"I LISTENED TO {len(wrapped)} SONGS IN 2024 (ROUGHLY {3*len(wrapped)} MINUTES OR {3*len(wrapped) / 60} HOURS OR {3*len(wrapped) / 60 / 60} DAYS) \n")

print(f"I LISTENED TO {len(counts_2.items())} DIFFERENT SONGS IN 2024\n")

print("_________________________________________________________\n")

for key, value in counts_1.items():
    if value >= 2: # Looks at how many artists you've listened to more than ten times
        most_popular_artist[key] = value

for key, value in counts_2.items():
    if value >= 2: # Looks at how many songs you've listened to more than fifteen times
        most_popular_song[key] = value


most_popular_artist = (dict(sorted(most_popular_artist.items(), key=lambda x:x[1], reverse = True)))
most_popular_song = (dict(sorted(most_popular_song.items(), key=lambda x:x[1], reverse = True)))

keys_list_artist = list(most_popular_artist.keys())
values_list_artist = list(most_popular_artist.values())

#print(f"ARTISTS WITH MORE THAN 10 PLAYS IN {current_month}:\n")

print("MY TOP TEN ARTISTS ON SPOTIFY OF 2024")

try:
    for i in range(0, 10): #range(len(keys_list_artist)): # Provides your top ten artists, if you want all artists more >= 10, change range to commented
        print(values_list_artist[i], keys_list_artist[i])
except IndexError:
    print("IndexError ~ list index out of range. This error will be handled gracefully.\nFalling back to listing minimum amount of artists...")
    max_range = len(keys_list_artist)
    if max_range != 0:
        print(f"Found {max_range} artists. Continuing.")
        for i in range(0, max_range):
            print(values_list_artist[i], keys_list_artist[i])
    else:
        print("Found 0 artists. Skipping.")
        print("TIP: Change the value of value in `counts_1.items():` to something within range to continue. (Uppermost block - not the one under this!)")


keys_list_song = list(most_popular_song.keys())
values_list_song = list(most_popular_song.values())

print("_________________________________________________________\n")

#print(f"SONGS WITH MORE THAN 5 PLAYS IN {current_month}:\n")
print("MY TOP TEN SONGS ON SPOTIFY OF 2024")

try:
    for i in range(0, 5): #range(len(keys_list_artist)): # Provides your top ten artists, if you want all artists more >= 10, change range to commented
        print(values_list_song[i], keys_list_song[i])
except IndexError:
    print("IndexError ~ list index out of range. This error will be handled gracefully.\nFalling back to listing minimum amount of songs...")
    max_range = len(keys_list_song)
    print(f"Max_range: {max_range}")
    if max_range != 0:
        print(f"Found {max_range} songs. Continuing.")
        for i in range(0, max_range):
            print(values_list_artist[i], keys_list_artist[i])
    else:
        print("Found 0 songs. Skipping.")
        print("TIP: Change the value of value in `counts_1.items():` to something within range to continue. (Uppermost block - not the one under this!)")

for key, value in counts_1.items():
    if value == 1: # Counts artists you've only played one time
        most_popular_artist[key] = value

for key, value in counts_2.items():
    if value == 1: # Counts number of songs only played one time
        most_popular_song[key] = value


most_popular_artist = (dict(sorted(most_popular_artist.items(), key=lambda x:x[1], reverse = True)))
most_popular_song = (dict(sorted(most_popular_song.items(), key=lambda x:x[1], reverse = True)))

keys_list_artist = list(most_popular_artist.keys())
values_list_artist = list(most_popular_artist.values())

keys_list_song = list(most_popular_song.keys())
values_list_song = list(most_popular_song.values())


print("\n")
print("_________________________________________________________\n")
print("\n")
print(f"I LISTENED TO {len(keys_list_artist)} ARTISTS ONLY ONE TIME IN 2024")
print("\n")
print(f"I LISTENED TO {len(keys_list_song)} SONGS ONLY ONE TIME IN 2024")
print("\n")


artist_counts = Counter(wrapped[wrapped_artist])
count_taylor_swift = artist_counts["Taylor Swift"] # Can change "Taylor Swift" to any artist
print(f"TAYLOR SWIFT COUNT: {count_taylor_swift}")
print("\n")
