Hi, this Readme file is going to be both a log of my decisions during this test and if necessary a guide on how to run my code, although this will be secondary.


The first main decision was choosing the language, I juggled between doing it in c# which is the language im most familiar with and Python, which I believe to be more apt for this specific challenge, in the end due to time constraints I am going with python, since I know it will be faster due to how powerful the python libraries are for this type of challenges. The downside of this is that it may end up becoming too easy and unhelpful in what is supposed to be a showcase of my technical skills, unfortunately I only have today available in the 72h period I was given to accomplish this test, so I will approach the problem with a focus on having a MVP ready and then if I have the time for it I will either expand upon it or make another version completely.

To start I will just create a basic test that checks if the crawler when given the url returns anything resembling an html, to check this I will just check if it has a html ending tag.

Since I'm not familiar with unit testing in python I will directly pass the test before doing a commit, as I need to make sure I know how to do it for the rest of the challenge.

After this I will make the first commit and start making tests for the rest of the tasks before continuing any development.

note: I am using the standard library unittest for testing, so tests are ran using "python -m unittest discover" while inside the folder.

The next step is adding the test for the news extraction, in this case I will test that the amount extracted is 30, and that the resulting objects contain all the expected keys.

While doing this i re-read the test, and am confused by the line "The solution should store usage data, including at least the request timestamp and a field to identify the applied filter" as before reading this again it hadnt hit me that it would be an interfacing program, as while reading it I originally thought it to be a program that would return the requested data either on the terminal or as a csv file, I had not thought that the filtering would be an option chosen by the user. Fortunately this doesnt change my approach, and will not change my current plans besides when it eventually comes to the point where I make the interface.

After a bit of research BeautifulSoup seems to be the best approach to parse an html file, so next step is extracting all the items with class 'athing' (deduced after inspecting the hackernews website), and then etracting the number, title, comments and points from those to create an array of "news" objects.

I now have finished the get_news function, and adjusted the test to account for some mistakes I did while creating it, to correctly filter the title, number, points and comments I needed to have different approaches since unfortunately they are not all in the same <tr>, and they dont all have classes that make it easy to parse.
For the title and rank I just needed to filter the <tr> with classes "athing" and extract from them the tags with class "titleline" and "rank", meanwhile for the points and comments I needed to get the next sibling to the "athing" tags, and then navigate inside it for the comments tag since id did not have any class (the points tag had the a class to find it) then I needed to parse the int from the points and the comments tags.

The test for news extraction is now passed.
 
Implemented tests for sorting and filtering, checking for all the required parameters as well as ascending and descending sortings.
Added a function to filter by title word count, it splits the title into strings, checks whether its smaller or bigger than the given count argument, and then depending on if you want the articles longer than that count or the ones smaller/equal then it returns those.

finally after this is just implemented a simple sorting function using the sorted function.
All test are now passed, next step is just doing the UI part of this, and adding logs to it.