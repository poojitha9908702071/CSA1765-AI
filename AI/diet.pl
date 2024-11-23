dise(heartatack,"heart").
dise(fever,"hot").
dise(cold,"runn").
diet(heart,"Avoid oil food").
diet(hot,"Avoid Cool food").
diet(runn,"Avoid cool food").
food(Dise,Diet):-
    dise(Dise,Fa),
    diet(Fa,Diet).
