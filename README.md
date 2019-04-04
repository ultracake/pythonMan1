# pythonMan1


# Step - by - step instructions for the assignment 


1. Get all repositories clone urls from the organization 'python-elective' and save them in a list, tuple, set or dictionary. For this you should make use of the urllib module, and you can get all info about the repositories at this api.
(Treat and read the json data as a text file. imagine something like a repository_info.txt. Then use the string searching and manipulations teqniques that we have worked with so far. Dealing with json data comes later this semester.)


2. Clone all repos from the organisation. (for this you will need the modul: subprocess) 
or if the repository is alredy cloned you should make sure that you have an up to date version of the repository by a pull request. (for some of the tasks in this operation you will need the modul: subprocess like before and for some you will need the module: OS)


3. Traverse through all repos locally and get the readme files content in a list ie. (for this you will need the module: glob)


4. Search the content of the list and find the "## Required reading" paragraph and put the content of that paragraph into list.


5. Write the list to a required_reading.md in a new curriculum repository. (for this operation you will again need the modul: OS) 
The links in the readme file should be: 
Ordered Alphabetically
Beginning character should be capitalized
The list should look good/normal, e.g no blank bullet points, no whitepsaces in wrong places etc.
No dublicate link should occour.

6. push that repository to your own github account.
