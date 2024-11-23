% Define birds and their ability to fly
bird(sparrow, fly).
bird(pigeon, fly).
bird(squirrel, cannotfly).
bird(tan, cannotfly).

% Predicate to check if a bird can fly
can_fly(Bird) :- bird(Bird, fly).

% Query to find all birds that can fly
fly_of(Birds) :- findall(Bird, can_fly(Bird), Birds).
