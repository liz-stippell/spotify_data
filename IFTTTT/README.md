# IFTTTT Workflow: Setting It Up
1. You will need [this IFTTTT applet](https://ifttt.com/applets/nin7BxVm-keep-a-log-of-your-recently-played-tracks) and connect it to an account with Google Sheets
2. Wait for your data to roll in as you listen to songs!
3. Make sure the Google Sheet that is created is open for viewing for anyone with a link
4. Copy the Google Sheet link <b>from the browser</b> (i.e. not the link that Sheets gives you to share, <i>yes they are different!</i>) insert it in <b>line 6</b> of the code
5. Add a row at the very top with the following headers: "date" "song" "artist" for columns a, b, and c
6. Run the code! You can use either `IFTTTT_spotify_wrapped.py` or `IFTTTT_spotify_wrapped_NOTOEBOOK.ipynb`. The second option is recommended for beginner Python users. (Feel free to change the code accordingly, I usually run this at the end of each month to see my monthly round-up and other cool data facts)

# `error_handling` Version

This pull request aims to minimize errors that can be caused by misconfiguration and tell the user what went wrong (along with how to fix it).

The main file, IFTTTT_spotify_wrapped_error_handling.py uses try/except blocks to catch errors and attempt to try again. At the top of the file, you have config where you can change the names of the different columns. By implementing these changes, we reduce the chance of user error.

The next file, IFTTTT_spotify_wrapped_NOTEBOOK.ipynb` is the notebook entry for the corresponding code shown above. This provides information as to how to configure the program.

Lastly, IFTTTT_spotify_wrapped.py was an attempt to drop the changes I attempted to make to the original file and overwrite it with the main file's contents.

#

This repository would not be possible without IFTTTT, Google Sheets, and wherever I got the `convert_google_sheet_url()` function.

Pull requests should be open. 


For testing, please feel free to use the `.xlsx` Excel spreadsheet (this is for more advanced users) OR use my Google Sheet with my Spotify wrapped: https://docs.google.com/spreadsheets/d/1AUxY8Cjr5MMgrTzoewKzGfqO1fnUzzkOBapEGpt1I7A/edit?gid=0#gid=0


Any questions about this code, please email me at <a href="mailto:lizstip3@gmail.com">lizstip3@gmail.com</a>
