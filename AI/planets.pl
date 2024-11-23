planet(jupiter,30000).
planet(earth,40000).
planet(satrun,7000).
planet(venus,8999).
planet(neptune,90000).

list_of(Planets,Distance):-
    findall(Planets,planet(Planets,_),Planets).
list_distance(Distance):-
    findall(Distance,planet(_,Distance),Planets).
list_distance(Distance):-
    findall(Distance,planet(_,Distance),Distance).
