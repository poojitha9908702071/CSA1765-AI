likes(john, pizza).
likes(mary, sushi).
eats_out(X) :- likes(X, _).
forward_chaining :-
    findall(X, likes(X, _), People),
    forall(member(Person, People), (eats_out(Person), assert(fact(eats_out(Person))))).
list_facts :-
    fact(Fact),
    write(Fact), nl,
    fail.
list_facts.
