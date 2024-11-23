% Match an empty pattern with an empty list
match([], []).

% Match a wildcard (_) with any head of a list
match([_ | PatternTail], [_ | ListTail]) :-
    match(PatternTail, ListTail).

% Match a specific element in the pattern with the head of the list
match([Head | PatternTail], [Head | ListTail]) :-
    match(PatternTail, ListTail).

% Test cases
% Usage: Query match([a, _, c], [a, b, c]).
