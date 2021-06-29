# volleyball-data-wrangling


## Specifications
This is a simple GUI interface that interfaces with an excel spreadsheet designed to record player statistics for volleyball when viewing a game recording.
The primary imports used are Tkinter and Openpyxl
Currently the app is able to make all the required edits to the excel spreadsheet and has a simple indicator for current statistics in that same editor. It is lacking a more official viewport with more detailed assessments of player statistics and if they are show week to week improvements.

Known Issues:

Doesn't have an adequate way to record covers following a poor receive or set.

If someone is not tall enough for blocking to be useful how do we record their perfomance on blocking?

Occasionally difficult to see if set positioning was correct (Using our personal recording setup).


## GUI 
Currently The GUI consists of a main menu which leads into three options. Two of these options are for viewports of the statistics which have yet to be developed. The remaining button leads to a season selector window allowing you to select which season of your team's data you wish to edit. After selecting a season the editor window opens allowing you to make edits to playerstatistics, add or remove players, and contains a more rudimentary series of stats values so as to appropriately inform the editor that their inputs are being recorded.

## STATS
The statistics is broken down into the primary actions being perfomed during play. Those being:  
Serves  
Receives  
Sets  
Spikes  
Tips  
Blocks  

These 6 actions are then broken down into 4 categories attempting to indicate best to worst for each category using the success of the play.
For example Serves are broken up into:  
Aces: The serve was performed well enough that the opposing team was unable to receive it.  
In: The serve made it into the enmey court but they managed to receive it.  
Out: The serve made it over the net but failed to make it into the enemy court.  
Short: The serve failed to make it over the net.  
