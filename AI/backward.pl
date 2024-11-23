likes(john, pizza).
likes(mary, sushi).
eats_out(X) :- likes(X, _).
backward_chaining(Goal) :-
    call(Goal), !.
