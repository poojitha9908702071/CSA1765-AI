bird(sparrow, fly).
bird(pigeon, fly).
bird(squirrel, cannotfly).
bird(tan, cannotfly).
can_fly(Bird) :- bird(Bird, fly).
fly_of(Birds) :- findall(Bird, can_fly(Bird), Birds).
