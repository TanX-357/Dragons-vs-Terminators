# Dragons-vs-Terminators

> A tower defense game in which one has to defend the Dragon King and his throne from the terminators by using the various types of dragons.

## Table of contents
* [STORY-LINE OF THE GAME](#general-info)
* [My Contribution and Features of the project](#technologies)
* [Inspiration](#inspiration)
* [Setup](#setup)


## Story-line of the game
* The Terminators Robots are trying to steal the Dragon Eggs and heart of the Dragon King
* Dragons wins if all the dragons are destroyed
* Terminators win if all of thye terminators are destroyed.
* The player is expected to place different types of Dragons in path to protect the Dragon Colony and destroy the Terminators. 



## My Contribution and Features of the project.
* I implemented various classes of dragons,each with a specific functionality like NinjaDragon(which damages all the Teminators that pass by,but can never be stung),
ShortThrower and LongThrower Dragon(who hit based on terminator distance from them) and many more(around 12) more classes with specified functionality.
* There were container dragon class also which used to defend other dragons at their place.Two of which child class were Bodyguard and TankerDragon(which attacks also with defending).
* Also there was a DragonKing class which can instantialized only once and it doubles the damage of all dragons behind him.(only once for each dragon instance)
* Finally the 2 most special child class of thrower dragon-ScaryDragon and SlowerDragon were there,which did not do any damage but as their name suggests:
* SlowerDragon throws sticky syrup at the terminator,applying a slow effect for 3 turns(preventing dragon from doing action when the colony time was odd)
* ScaryDragon used to scare the Terminator and made him move back for 2 turns(provided the condition that each terminator instance can be scared only once)




## Inspiration
This project is based on exciting OOPs created by John DenNero,Tom Margino,and Eric Tzeng.So this project is inspired from the game Aunt vs Bees,which in turn was
inspired from Plant vs. Zombies.I would really like to thanks ib hubs team and lokesh Dabra sir,under whoose guidance i got the opportunity to contribute to the project.





## Setup
python3 gui.py(command in the project file working directory) will open the game in the web browser(after one downloads all the files and folders of the project)
