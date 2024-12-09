# Spotify Data Analysis
Analyzes your Spotify listening data collected through IFTTTT and stored in Google Sheets
<br>
<br>
<b>WARNING!</b> I have no idea how to stop IFTTTT from logging all of my data into Google Sheets. If you don't want it to log your songs forever, continue at your own risk. (Mine has been logging songs for literal years with no end in sight)

## Python Setup
I run this in the terminal because I write code from the terminal like a madman. (I'm not sure how this would affect running through an IDE, etc.)
1. Make sure you have [Python](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) installed
2. Install `pandas`: run `pip install pandas` in the terminal. Extra information can be found [here](https://www.geeksforgeeks.org/how-to-install-python-pandas-on-windows-and-linux/)

## Easier Python setup for those with less experience with Python
1. Follow the instructions for installing Jupyter Notebook and <b>Anaconda</b> [here](https://github.com/liz-stippell/Intro_To_Python). For help with understanding how Jupyter Notebook works, find information [here](https://github.com/liz-stippell/Intro_To_Python/blob/main/1_Basic_Math.ipynb)
2. Download the Jupyter Notebook version of the code (the file that ends in `.ipynb`). You will still need to install pandas (see above in general Python Setup)

# IFTTTT Workflow: Setting It Up
1. You will need [this IFTTTT applet](https://ifttt.com/applets/nin7BxVm-keep-a-log-of-your-recently-played-tracks) and connect it to an account with Google Sheets
2. Wait for your data to roll in as you listen to songs!
3. Make sure the Google Sheet that is created is open for viewing for anyone with a link
4. Copy the Google Sheet link <b>from the browser</b> (i.e. not the link that Sheets gives you to share, <i>yes they are different!</i>) insert it in <b>line 6</b> of the code
5. Add a row at the very top with the following headers: "date" "song" "artist" for columns a, b, and c
6. Run the code! (Feel free to change it accordingly, I usually run this at the end of each month to see my monthly round-up and other cool data facts)


This repository would not be possible without IFTTTT, Google Sheets, and wherever I got the `convert_google_sheet_url()` function.

Pull requests should be open. 


For testing, please feel free to use the `.xlsx` Excel spreadsheet (this is for more advanced users) OR use my Google Sheet with my Spotify wrapped: https://docs.google.com/spreadsheets/d/1AUxY8Cjr5MMgrTzoewKzGfqO1fnUzzkOBapEGpt1I7A/edit?gid=0#gid=0


Any questions about this code, please email me at <a href="mailto:lizstip3@gmail.com">lizstip3@gmail.com</a>
