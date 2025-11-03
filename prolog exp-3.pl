% student_teacher_subject.pl

% --- Database ---
teaches('Dr.Nandhini', 'CSA0305', 'Data Structures').
teaches('Dr.Saranya', 'CSA0201', 'C Programming').
teaches('Dr.Priya', 'CSA0402', 'Artificial Intelligence').

enrolled('Anusha', 'CSA0305').
enrolled('Saadhana', 'CSA0201').

% --- Rules ---
student_teacher(Student, Teacher) :-
    enrolled(Student, Code),
    teaches(Teacher, Code, _).

student_subject(Student, Subject) :-
    enrolled(Student, Code),
    teaches(_, Code, Subject).

% --- Main program with example ---
main :-
    Student = 'Anusha',
    student_teacher(Student, Teacher),
    student_subject(Student, Subject),
    format('~w is taught by ~w in subject ~w.~n', [Student, Teacher, Subject]).
