det = {"AC/DC","Back in Black","Thriller"}
print(det)
det.add("NSYNC")
print(det)
det.add("NSYNC")
print(det)
det.remove("NSYNC")
print(det)

print("AC/DC" in det)
print("Who" in det)


album_set_1 = {"AC/DC","Back in Black","Thriller"}
album_set_2 = {"AC/DC","Back in Black","The Dark Side of the Moon"}
print(album_set_1&album_set_2)
album_set_3 = album_set_1&album_set_2
print(album_set_3)
album_set_union = album_set_1.union(album_set_2)
print(album_set_union)
album_set_issubset = album_set_3.issubset(album_set_1)
print(album_set_issubset)


music_geners = ["rap","house","electronic music","rap"]
music_geners_set = set(music_geners)
print(music_geners_set)

A = [1,2,2,1]
B = set([1,2,2,1])
C = sum(A) == sum(B)
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))
print(C)

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_subset = album_set1.issubset(album_set2)
print(album_subset)

ted = {"a","b"}
ted_2 = {"a"}

ted_3 = ted&ted_2
print(ted_3)