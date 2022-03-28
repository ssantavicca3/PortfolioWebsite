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
5. in a separate column, type "=IF(ISNUMBER(SEARCH("@",A1)), LEFT(A1, SEARCH("@",A1,1)-1), A1)"
	- drag down to substring the local paths out of the package reference
6. copy & paste back into the requirements.txt file