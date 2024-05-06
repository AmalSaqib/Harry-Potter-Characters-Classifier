# Harry-Potter-Characters-Classifier

I wanted to do an end-to-end project regarding something that excites me. Of course I landed on Harry Potter.

I want to do everything from scratch; making the dataset, managing it, test different classifiers, everything on my own.

# Let's start!!

I want to cover at least the most important characters. Harry Potter has a lot of characters in it so I chose the main ones.

1) Harry Potter
2) Hermione Granger
3) Ron Weasley
4) Voldemort
5) Ginny Weasley
6) Fred Weasley
7) George Weasley
8) Percy Weasley
9) Sirius Black
10) Albus Dumbledore
11) Severus Snape
12) Minerva McGonagall
13) Rubeus Hagrid
14) Draco Malfoy
15) Luna Lovegood
16) Dobby
17) Neville Longbottom
18) Cedric Diggory
19) Remus Lupin
20) Hedwig
21) Dolores Umbridge
22) Bellatrix Lestrange
23) Lucius Malfoy
24) Aunt Petunia
25) Dudley Dursley
26) Uncle Vernon
27) Argus Filch


# resize.py
I wrote this code to make my life easier. When I am collecting the data, I save all my images in one directory. This code then parses through all the files in this input directory and for every image it finds the respective folder to add the image in. First it resizes the image, it moves it to that character's folder in the train folder, and then it deletes it from the input directory.
