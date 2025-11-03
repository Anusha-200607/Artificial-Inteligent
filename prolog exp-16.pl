% vowel_count.pl
% Program to count number of vowels in a word

% --- Facts: vowels ---
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% --- Rule to count vowels ---
count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, Rest),
    Count is Rest + 1.
count_vowels([_|T], Count) :-
    count_vowels(T, Count).

% --- Main program example ---
main :-
    Word = [h, e, l, l, o],
    count_vowels(Word, Count),
    format('Number of vowels: ~w~n', [Count]).
