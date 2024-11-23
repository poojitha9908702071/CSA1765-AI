% Facts: parent relationships
parent(john, mary).
parent(john, joe).
parent(susan, mary).
parent(susan, joe).
parent(mary, ann).
parent(mary, tom).
parent(david, ann).
parent(david, tom).

% Rules: defining relationships based on parent relationships

% X is a child of Y if Y is a parent of X
child(X, Y) :- parent(Y, X).

% X is a grandparent of Z if X is a parent of Y and Y is a parent of Z
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% X is a grandchild of Z if Z is a grandparent of X
grandchild(X, Z) :- grandparent(Z, X).

% X is a sibling of Y if they share at least one parent
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% X is a cousin of Y if their parents are siblings
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).

% X is an aunt or uncle of Y if X is a sibling of Y's parent
aunt_or_uncle(X, Y) :-
    parent(Z, Y),
    sibling(X, Z).

% X is a niece or nephew of Y if Y is a sibling of X's parent
niece_or_nephew(X, Y) :-
    parent(Z, X),
    sibling(Z, Y).

% X is a descendant of Y if Y is a parent of X or Y is an ancestor of Z who is a parent of X
descendant(X, Y) :- parent(Y, X).
descendant(X, Y) :- parent(Y, Z), descendant(X, Z).

% X is an ancestor of Y if X is a parent of Y or X is an ancestor of Z who is a parent of Y
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
