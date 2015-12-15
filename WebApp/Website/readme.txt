Make sure you have installed:

Node.js
Modules: Install the following with "npm install moduleName"
	express //for directory organization
	colors //cosmetics for command prompt
	socket.io //for opening connection to the server
	mysql //for communicating with the mysql database

Running the node local server:

-Open "Node Command Prompt"
-Use "cd" to navigate to the server folder. "dir" will tell you the contents of your current directory
-Launch the server with "node index.js"
-Server will start listening on a particular port (set to 8000)
-Open browser and go to "localhost:8000"
-From here you can navigate to individual html pages stored in the view folder
by adding /yourFileHere.html to localhost:8000. When adding new pages,
be sure to add a new app.get in the index.js script.

Batch File Instructions (in case you don't want to retype the same instructions every time you debug):

cd "C:\Program Files\nodejs" //Default Directory of where Node should be stored
call nodevars.bat //Calls the batch file connected to Node Command Prompt
cd "C:\YourRepoWebsiteDirectoryGoesHere" //Add your index.js folder directory here
node index.js //Launches index.js
cmd /k //Prevents the cmd from immediately closing

Troubleshooting:
"I can't connect to the website and I didn't change anything!"
There's a good chance your local host server thinks your still connected on
that port even after you restart it. Try to change the port number to
something else to see if that's the case.

"I keep getting an error for something involving favicon.ico!"
We honestly have no idea. It might have something to do with the
Font Awesome icons we used, but as of right now, it's a mystery.

"The node console keeps giving me tons of errors when I try to connect!"
Make sure you have all of the required modules installed. If you are sharing
the repo from computer to computer, all computers attempting to test run
the local server need these installed on their local machines.

"I tried to play a song and I can't hear anything!"
Your testAudio/songUpload/Songs folder is empty for copyright reasons. Fill that with the audio files you recieve from the audio analysis output and make sure information about them (directory, artist, title, etc) has been loaded into the database.

"I keep getting a 404 on a html/css/js/mp3/etc file!"
I means that, in the jumble of html and javascript files, it's having trouble appending the file to the front end because it can't find it. Double check the directory. All resources for the site should come from the public folder.