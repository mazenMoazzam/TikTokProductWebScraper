# voiceBot (In Progress)
The following project is a voice-controlled bot created using C# and .NET framework (Version 5) as well with the Speech Recognition library. Interactive voicebot that allows you to say a command and it will execute the following. For example, I say to the bot, "go to youtube", the bot (named Botimus Prime), will take you to Youtube with no work from the user. 

Working On/To-Do: 
-Youtube interaction with videos (play, pause, rewind, ahead, search etc...). This will be accomplished by setting up a client server application within the bot. Bot receives voice command to pause the 
video from the user, which then intializes an http object to send HTTP requests to. An HTML page containing the embedded youtube video and the necessary interactive functions (play, pause, rewind etc.). The html page serves as the webserver and will take in requests from the bot which will then respond with the necessary function. UPDATE: API will need to made (Python, Flask) to implement video bot interactions. 

-Calender event creator

-Set reminders by asking bot to set reminders, prompt to mention what reminder (message and prompt time will be stored in a database, preferably SQLite or PostgreSQL). 

-Check due reminders, bot checks for reminders that have passed, if found, bot fetches them and reads it to the user which will then be removed from the database (the bot checks for due reminders periodically). 

