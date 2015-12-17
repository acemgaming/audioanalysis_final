import os
import shutil
import mysql.connector

db = mysql.connector.connect(user='csci413f15_1',
                             password='F9UnP31c',
                             host='rei.cs.ndsu.nodak.edu',
                             database='csci413f15_1')

cursor = db.cursor()
newArtists = 0
newGenres = 0
newAlbums = 0
newSongs = 0

artists = []
cursor.execute('SELECT artist FROM ARTISTS')
result = cursor.fetchall()
for artist in result:
    artists.append(artist[0])
    
genres = []
cursor.execute('SELECT genre FROM GENRES')
result = cursor.fetchall()
for genre in result:
    genres.append(genre[0])
    
albums = []
cursor.execute('SELECT album FROM ALBUMS')
result = cursor.fetchall()
for album in result:
    albums.append(album[0])

print('Running...')

path = "/SongUpload/Information"
source = os.listdir(path)
dest_path = "/SongUpload/ParsedFiles"
for dir_entry in source:
    dir_entry_path = os.path.join(path, dir_entry)
    if os.path.isfile(dir_entry_path):
        with open(dir_entry_path, 'r') as my_file:
            file_data = my_file.read()
            for line in file_data.split('\n'):

                if(line != ''):
                    fields = line.split(';; ')
                    #print(fields[1])
                    
                    if fields[2] not in artists:
                        #print('INSERT INTO ARTISTS (artist) VALUES("{0}")' .format(fields[2]))
                        cursor.execute('INSERT INTO ARTISTS (artist) VALUES("{0}")' .format(fields[2]))
                        newArtists += 1
                        artists.append(fields[2])
                        #print('Artist: {0}' .format(fields[2]))
                    cursor.execute('SELECT artistID FROM ARTISTS WHERE artist = "{0}"' .format(fields[2]))
                    artistID = cursor.fetchall()
                    
                    if fields[5] not in genres:
                        #print('INSERT INTO GENRES (genre) VALUES("{0}")' .format(fields[5]))
                        cursor.execute('INSERT INTO GENRES (genre) VALUES("{0}")' .format(fields[5]))
                        newGenres += 1
                        genres.append(fields[5])
                        #print('Genre: {0}' .format(fields[5]))
                    cursor.execute('SELECT genreID FROM GENRES WHERE genre = "{0}"' .format(fields[5]))
                    genreID = cursor.fetchall()
                    
                    if fields[3] not in albums:
                        #print('INSERT INTO ALBUMS (artistID, album) VALUES ({0}, "{1}")' .format(artistID[0][0], fields[3]))
                        cursor.execute('INSERT INTO ALBUMS (artistID, album) VALUES ({0}, "{1}")' .format(artistID[0][0], fields[3]))
                        newAlbums += 1
                        albums.append(fields[3])
                        #print('Album: {0}' .format(fields[3]))
                    cursor.execute('SELECT albumID FROM ALBUMS WHERE album = "{0}"' .format(fields[3]))
                    albumID = cursor.fetchall()
                    
                    #print('INSERT INTO SONGS (fileLocation, title, albumID, year, genreID, duration, bpm, loudness, songKey, scale, chordsKey, chordsScale, chordsChangesRate, chordsNumberRate, danceability, bassiness, dynamicComplexity, zeroCrossingRate, intensity) VALUES("{0}","{1}",{2},{3},{4},{5},{6},{7},"{8}","{9}","{10}","{11}",{12},{13},{14},{15},{16},{17},{18})' .format(fields[0], fields[1], albumID[0][0], fields[4], genreID[0][0], fields[6], fields[7], fields[8], fields[9], fields[10], fields[11], fields[12], fields[13], fields[14], fields[15], fields[16], fields[17], fields[18], fields[19])) 
                    cursor.execute('INSERT INTO SONGS (fileLocation, title, albumID, year, genreID, duration, bpm, loudness, songKey, scale, chordsKey, chordsScale, chordsChangesRate, chordsNumberRate, danceability, bassiness, dynamicComplexity, zeroCrossingRate, intensity) VALUES("{0}","{1}",{2},{3},{4},{5},{6},{7},"{8}","{9}","{10}","{11}",{12},{13},{14},{15},{16},{17},{18})' .format(fields[0], fields[1], albumID[0][0], fields[4], genreID[0][0], fields[6], fields[7], fields[8], fields[9], fields[10], fields[11], fields[12], fields[13], fields[14], fields[15], fields[16], fields[17], fields[18], fields[19]))
                    newSongs += 1
                    
print('No more files')
for files in source:
    print('moving %s...' % files)
    shutil.move(os.path.join(path, files), os.path.join(dest_path,files))
print('New Artists: {0}' .format(newArtists))
print('New Genres: {0}' .format(newGenres))
print('New Albums: {0}' .format(newAlbums))
print('New Songs: {0}' .format(newSongs))
db.commit()
db.close()
