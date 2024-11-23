edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, g).
edge(f, g).
bfs(Start, Goal, Path) :-
    bfs_helper([[Start]], Goal, RevPath),
    reverse(RevPath, Path).
bfs_helper([[Goal|Rest] | _], Goal, [Goal|Rest]).
bfs_helper([[Node|Path] | Paths], Goal, Result) :-
    findall([NextNode, Node | Path],
            (edge(Node, NextNode), \+ member(NextNode, [Node | Path])),
            NewPaths),
    append(Paths, NewPaths, UpdatedPaths),
    bfs_helper(UpdatedPaths, Goal, Result).
