parent(john, mary).
parent(john, joe).
parent(susan, mary).
parent(susan, joe).
parent(mary, ann).
parent(mary, tom).
parent(david, ann).
parent(david, tom).
child(X, Y) :- parent(Y, X)
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandchild(X, Z) :- grandparent(Z, X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).
aunt_or_uncle(X, Y) :-
    parent(Z, Y),
    sibling(X, Z).
niece_or_nephew(X, Y) :-
    parent(Z, X),
    sibling(Z, Y).
descendant(X, Y) :- parent(Y, X).
descendant(X, Y) :- parent(Y, Z), descendant(X, Z).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
