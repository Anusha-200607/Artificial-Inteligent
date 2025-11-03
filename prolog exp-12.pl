% medical_diagnosis.pl
% Simple Medical Diagnosis Expert System

% --- Facts: symptoms related to diseases ---
disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(sore_throat).

disease(cold) :-
    symptom(runny_nose),
    symptom(sneezing),
    symptom(sore_throat).

disease(covid) :-
    symptom(fever),
    symptom(cough),
    symptom(loss_of_taste),
    symptom(tiredness).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(headache).

% --- Ask user for symptoms dynamically ---
symptom(S) :-
    format('Do you have ~w? (yes/no): ', [S]),
    read(Response),
    Response == yes.

% --- Diagnosis rule ---
diagnose :-
    (   disease(Dis)
    ->  format('You may have ~w.~n', [Dis])
    ;   writeln('No matching disease found.')
    ).

% --- Main program ---
main :-
    writeln('--- Medical Diagnosis System ---'),
    diagnose.
