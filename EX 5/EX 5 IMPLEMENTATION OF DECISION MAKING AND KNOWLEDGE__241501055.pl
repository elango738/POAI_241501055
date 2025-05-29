
% Given facts
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rules based on the conditions:
likes(john, X) :- likes(mary, X).         % John likes anything that Mary likes
likes(john, Y) :- likes(Y, wine).         % John likes anyone who likes wine
likes(john, Y) :- likes(Y, Y).            % John likes anyone who likes themselves

% Sample queries:
% Query 1: Does John like food?
% ?- likes(john, food).

% Query 2: Does John like wine?
% ?- likes(john, wine).

% Query 3: Does John like food if Mary likes food?
% ?- likes(john, food).

% Query 4: Who does John like?
% ?- likes(john, Y).
