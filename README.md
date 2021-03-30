## Stock market portfolio updater for LibreOffice Calc
### Support
Currently, Portfolio Updater is fully supported on Linux.
Making it work on Windows or MacOS should not be much of a hassle, if some at all.
Yahoo Finance updates their website quite often, sometimes leaving the script broken.
If this is the case, please open a new issue.
### Dependencies
`python3` <br />
`beautifulsoup4` <br />
`requests` <br />
`pyoo` <br />
`uno` <br />
### How does it work?
This script is started by running `run.sh` file. I prefer using bash alias for this. 
It opens up LibreOffice Calc document and looks at predefined location for ticker symbols.
When it finds the first ticker symbol in that predefined cell location, it appends it into a list and then moves one cell down as long as there is some content in these cells, appending ticker symbols with each iteration.
Once the following cell is empty, it moves to next step, which is sending these ticker symbols to web scraper that retrieves current stock price from Yahoo Finance.
Web scraper then sends the current stock prices back and they are written right next to their corresponding ticker symbol.
### Why?
As far as I am aware, there is no functionality regarding current stock market prices in LibreOffice, as there is in Excel for example.
Also, I was not able to find any free API service that would provide me with current stock market prices.
So as a little project to learn more about python, web scraping and interaction with LibreOffice, I made this little script!
### How to
### Linux
1. Clone this repository into your computer with `git clone https://github.com/MichalRybecky/Portfolio-updater.git`
2. `cd Portfolio-updater`
3. Open `options.py` file in your text editor.
4. Change `file_path`, `sheet_number` and `start_position` according to your need. You can read what each option means in the file.
5. Allow execution of `run.sh` with `chmod +x run.sh`
6. Go to home directory (`cd ~`) and open your `.bashrc` or `.bash_aliases` (where you configure your aliases)
7. Add this line: `alias YOUR_ALIAS='/PATH/TO/REPOSITORY/run.sh & disown ; exit'` <br />
Change YOUR_ALIAS with the command you want to use to run the script and /PATH/TO/REPOSITORY with full path of the repository you cloned.
In my case, this line looks like this: `alias fin='cd ~ ; ./.config/Portfolio-updater/run.sh & disown ; exit'`
8. After all of this, you should be all set. Just open your terminal emulator, type YOUR_ALIAS (`fin` in my case), hit enter and current stock prices will appear in your spreadsheet.
