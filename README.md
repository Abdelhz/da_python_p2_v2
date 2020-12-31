# Project : "Web scrapper"  Using Python basis to analyse a market
This projet consists of writing a program that analyses product information in a website and save them in a specific files, *file.csv*.
This program is called a scrapper and has the ability to connect to a website, parse inside this website and save the required information and wanted.

# Creating a vitual environment for the web scrapper :
We will have to create and environment for this projet.

**NOTE :** In this project we are using *python 3.9*

*Crate a folder for the project :*
1st open a terminal (in this case using git bash on windows)

**mkdir web_scrapper_project**

create the environment using *venv*

**cd web_scrapper_project**

**pyton -m venv env_scrap**

At this point the environment is created and we have to acticate it.

# Activate the virtual environment :
Once env_scrap is created we have to navigate inside the *scrips* folder. In linux the folder is called "*bin*"

**cd env_scrap/scripts**

**source activate**

now we have activated the environment.

# Install the required lib in the virtual environment :
We are using many libraries for this project thats have to be installed manually after activating the environment.

*install numpy :*

**pip install numpy==1.19.3*  *The version 1.19.4 of numpy causes errors when executing*

*install BeautifulSoup :*

**pip install bs4**

*install requests :*

**pip install requests**

*install lxml :*

**pip install lxml**

*install urllib3 :*

**pip install urllib3**

*install pandas :*

**pip install pandas**

*install pathlib :*

**pip install pathlib**



**Other required libraries are already installed with python 3.9 .**

# Opening project and executing :

Now we have to go back to the main folder "*web_scrapper_project*"

**cd ../..**

and copy files inside the "*web_scrapper_project*" next to the "*env_scrap*" folder.

#files list :

**scrapper_main.py**
**scrapper_books.py**
**url_mod.py**
**file_saver.py**
**folder_mod.py**

*at this point we can use vs code to open the projet :*

in the main folder "*web_scrapper_project*"
*and environment activated :*

**code .**

We can execute the project from vs code by executing the "*scrapper_main.py*" file

*Or by typing the following on the terminal :*

**python scrapper_main.py**


The program will save all files in *book_to_scrap* folder and inside each category folder.














