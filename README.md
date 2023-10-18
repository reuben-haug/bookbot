# bookbot
a Python program that can analyze an entire book's text and print out an interesting statistical report.
BookBot is my first git project!

This script reads the contents of a specified text file & generates an on-screen report listing
the total number of words & a count of each alphabetical character (ignoring case).

10/15/2023
I've started learning more about functional designs & typing in the last few days.  When I was programming in highschool & college I don't think this sort of expression existed, or at least I had enough going on working through OOP paradigms & mathematical operations (I'm getting better, I swear).

I was struck with a thought while working on this earlier: In our year of the Lord 2023, just how behind do I feel struggling with these basic functionalities & concepts other people much smarter than me built more sophisticated tools with much less.  I mean, a bookbot?  I'm trying to learn & see the light at the end of the tunnel & damn it bookbot, you're going to get me there. 

10/16/2023
I was looking for some more text resources (shout out Project Gutenberg) and found a transcription note I thought would be fun to add functionality for:
    Transcriber's note: 
    Text enclosed by underscores is in italics (_italics_).
    A single underscore introduces a subscript (CO_2), and a caret a
    superscript (B^1).

    Page numbers enclosed by curly braces (for example: {25}) have been
    incorporated to facilitate the use of the Alphabetical Index and other page
    references in the text.

My mind went to HTML tags immediately.  Again, it feels so dinky but I did a little bit of stuff with a Python package called Typer earlier this week & now I'm in CLI mode.  Having some crossover & make it so little symbols or formatting appear in a CLI style script.

10/17/2023
I just started an exercise like this on boot.dev.  The twist is you need to check for specific positions, instead of just identifying every instance of a value or group of values.  This is my first crack at it:

    def markdown_to_text(doc_content):

    """Remove any '#' from the beginning of a line; any '*' from the start or end of a word."""
    doc_copy = doc_content
    lines = doc_copy.split()
    
    def remove_hash(line):
        return line.replace("#", "")

    def remove_asterisk(line):
        return line.replace("*", "")
    
    for i in lines:
        remove_hash(i)
        remove_asterisk(i)

Not quite there, huh?  I felt like I needed to get the structure blocked out quickly & I quickly latched onto having two separate functions for each character.  It will return a formatted line but that's not the problem we need to solve.  Tomorrow we go again.



10/17/2023
__________
-Separated reading the text file into its own function
-Pass the 'file_path' as an argument to 'generate_text_report'
-Removed the global variable 'file_contents'
-Added main block to call the function