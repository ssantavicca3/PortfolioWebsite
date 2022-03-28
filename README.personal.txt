To pick back up with website, 
1. open Anaconda prompt
2. direct to the "Portfolio_Website" folder in Desktop
3. run "atom ."
4. in the integrated shell/prompt, direct to the "alt_project" folder
5. type "flask run"


To update requirements.txt
1. Anaconda prompt
2. direct to "PortfolioWebsite folder
3. type "python -m pip freeze > requirements.txt"
4. copy & paste to an excel spreadsheet
5. in a separate column, type "=LEFT(A2, SEARCH("@",A2,1)-1)"
	- drag down to substring the local paths out of the package reference
	- copy & paste the other values over (those that didn't have "@" in them)
	- note this could probably be quicker if adding into an IF statement
6. copy & paste back into the requirements.txt file