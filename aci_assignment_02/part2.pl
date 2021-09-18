

start :-
   write('Write the value of PH: '),
   read(Ph),nl,
   write('Write the value of Solids: '),
   read(Sol),nl,
   write('Write the value of Sulphate: '),
   read(Sul),nl,
   
   input(Ph,Sol,Sul).
input(stop) :- !.


input(Ph,Sol,Sul):-
	Ph > 4.636,
	Sul =< 387.796,
	Sul > 258.97,
	write("The Results are"),nl,nl,
	write(" Non Drinkalble"),nl,
	write(" proba: 62.19%"),nl.
	
input(Ph,Sol,Sul):-
	Ph =< 7.61,
	Sul > 387.796,
	write("The Results are"),nl,nl,
	write("Drinkalble"),nl,
	write(" proba: 66.04%"),nl.
	
input(Ph,Sol,Sul):-
	Ph =< 4.636,
	Sul =< 387.796,
	Sul > 258.97,
	write("The Results are"),nl,nl,
	write("Non Drinkalble"),nl,
	write(" proba: 79.45%"),nl.

input(Ph,Sol,Sul):-
	Ph > 7.61,
	Sul > 387.796,
	write("The Results are"),nl,nl,
	write("non Drinkalble"),nl,
	write(" proba: 78.08%"),nl.

input(Ph,Sol,Sul):-
	Ph > 5.825,
	Sul =< 258.97,
	Sol > 21161.408,
	write("The Results are"),nl,nl,
	write("Drinkalble"),nl,
	write(" proba: 94.34%"),nl.
	
input(Ph,Sol,Sul):-
	Ph =< 7.947,
	Sul =< 258.97,
	Sol =< 21161.408,
	write("The Results are"),nl,nl,
	write("Non Drinkalble"),nl,
	write(" proba: 73.91%"),nl.

input(Ph,Sol,Sul):-
	Ph =< 5.825,
	Sul =< 258.97,
	Sol > 21161.408,
	write("The Results are"),nl,nl,
	write("Non Drinkalble"),nl,
	write(" proba: 50.0%"),nl.

input(Ph,Sol,Sul):-
	Ph > 7.947,
	Sul =< 258.97,
	Sol =< 21161.408,
	write("The Results are"),nl,nl,
	write("Drinkalble"),nl,
	write(" proba: 100.0%"),nl.


