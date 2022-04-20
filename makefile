
all: README.md

README.md: Math_Quiz.py
	echo "# Math Quiz" > README.md
	echo "## This is a real-time generated math quiz." >> README.md
	echo "### Kids of age 10 and older are 'Biggie'" >> README.md
	echo "### Kids younger than 10 are 'Chiggie'" >> README.md
	echo "#### Time of run of make file : `date`" >> README.md
clean:
	rm README.md
