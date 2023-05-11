# Album Cover Search CLI

## Purpose:
To make the process of collecting Album Cover images for our blog's top 30 less tedious<br>
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
Pandas, Requests and Load_dotenv are needed.<br>
