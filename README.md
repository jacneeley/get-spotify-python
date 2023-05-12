# Album Cover Search Script

## Purpose:
To make the process of collecting Album Cover images for our blog's top 30 less tedious<br>

## About:
This python script reads KTSW's NACC Chart CSVs to collect the Artist and Record (album name).<br>
This data is saved locally and then passed to Spotify's Web API using GET from the requests Library.<br>
'Artist' and 'Album' are passed as arguments using the Web API's search endpoint.<br>
Data about the Album is then returned and from that Image URL's for each album is provided.<br>
The URL's can be opened, and the images can be saved for our blog.<br>

### Limitations:
Spotify's search endpoint queries the most popular results.<br>
If an artist is niche, then this script may return incorrect results.<br>
In its current state, this script is only approx. 90% accurate. Note: results are based on limited testing.<br>
Efforts will be made to improve the accuracy of searches.<br>
Searches are conducted to retrieve Album ID's. As of now this is the best way to return needed data.<br>

## Dependencies
Several python libraries are used.<br>
 - Pandas 
 - Requests
 - Load_dotenv

.env must be created to hold the CLIENT_ID, the CLIENT_SECRET, and optionally, a FILE_PATH for NACC Chart CSVs.

 ## Getting Started
 
 ### Installs
 #### Pandas
 `pip install pandas`<br>
 #### load_dotenv<br>
 `pip install python-dotenv`<br>
 #### requests
 `python -m pip install requests`<br>
 
 ### Creating dotenv
 - simply open your get-spotify-python directory
 - create new file and name it ".env"[recommended] or give it a name if you want just make sure it ends with .env.

 The .env will contain key-value pairs needed to run the script.
 - CLIENT_ID = 'some_string'
 - CLIENT_SECRET = 'some_string
 - FILE_PATH [Optional] = csv_path

 if a path is not given in .env, the script will ask for a file path once ran.
 
 ### Obtaining Client ID and Client Secret

 Client Id and Secret can be obtained from the spotify webapi dashboard.<br>
 1. Sign into the [dash board](https://developer.spotify.com/dashboard) using ktsw's spotify credentials.
 2. Click on "Python app" then click on "settings".
 3. Copy the client ID, create a `CLIENT_ID` key and paste the key as the value.
 4. Now go back and click "view client secret" repeat step 3 for `CLIENT_SECRET`
 5. Create a `FILE_PATH` key value pair and paste the file path of the NACC chart CSV.

 #### .env syntax example
 `CLIENT_ID = "[CLIENT_ID here]"`<br>
 `CLIENT_SECRET ="[CLIENT_SECRET here]"`<br>
 `FILE_PATH ="[FILE_PATH here]"` <- optional but recommended.<br>
