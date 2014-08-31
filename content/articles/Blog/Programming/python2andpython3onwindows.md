Title: How to run Python2 and Python3 together on Windows 7
Date: 2014-08-31 11:38
Tags: python, programming
Slug: how-to-run-python-2-and-python-3-together-on-windows-7
Author: Joe Jean

I have always wanted to have both Python 2 and Python 3 installed and running on my Windows 7 computer, but I feared that installation was going to be a nightmare. However, today I put my fear aside and dived right into the task. Here is how I did it:

###OPTION 1: Python 2, virtualenv and virtualenvwrapper already installed

My Windows 7 laptop already had Python 2, virtualenv and virtualenvwrapper installed. So I downloaded and installed 
<a target="_blank" href="https://www.python.org/downloads/"> Python 3 </a>. By default any virtual environment I create would use Python 2. In order to make them also use Python 3, I would create them with the following command: ```mkvirtualenv myenv -p c:\python3.4```


But then within that virtual environment, if I wanted to use Python 3, I would still have to call it explicitly using the command:```py -3```otherwise it would still default to Python 2. I found this observation weird and  I decided to do a little experiment. I activated one of the virtual environments that were created without pointing to Python 3. Then, in the terminal I type: ```py -3```and, bam, it worked. So I came to the conclusion that installing Python 3 on my windows was enough for me to still use it in my virtual environments whenever I want to. So I don't have to explicitlty point my virtual environments to Python 3 with the ```-p```flag. 

###OPTION 2: Python is not installed

If Python is not already installed on your computer. You should install Python 3. And at the beginning of your Python files you would just add ```#!python2``` or ```#!python3``` depending on whether you want to use the version 2 or the version 3 of Python. Then in order to run any of your python programs you would type:```py pythonfile.py```

Now, that I have both versions on my computer. I'm going to start exploring some of the interesting features of Python 3 while still keeping my Python code running. 



