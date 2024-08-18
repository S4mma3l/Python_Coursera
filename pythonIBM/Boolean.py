# Boolean

album_year = int(input("de que aNo es el album?"))

if(album_year<1980) or (album_year>1989):
    print("este alnum fue lanzado en los 70s or 90s")
else:
    print("este album fue lanzado en los 80s")