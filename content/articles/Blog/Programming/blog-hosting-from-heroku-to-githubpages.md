Title: Moving My Personal Website from Heroku to Github Pages
Date: 2015-11-08 09:07
Tags: python,pelican, githubpages
Slug: deploying-my-personal-website-to-github-pages
Author: Joe Jean


When I first built my personal website I deployed it to Heroku. At that time Heroku was the best option for me because it offered a free tier and it was relatively easy to use. But one thing I did not like about it was that the application dyno&mdash;the container that handles all the HTTP traffic to the site&mdash; would go to sleep if my website receives no traffic in a 30-minute period. Consequently the next time someone tries to access the site it will take longer to load as the dyno will need to wake up first. 

The site is built with [Pelican](http://docs.getpelican.com/en/3.6.3/) which is a static site generator written in Python. A static site generator basically takes text written in a plain text markup format such as Markdown and converts it to HTML pages using predefined templates. So, after defining the templates for my website, whenever I need to publish new content such as this article I only need to write raw text in a MarkDown file and Pelican will handle the rest for me. Among other advantages, this approach is easy to use and results in a really fast website that can be easily deployed to GitHub Pages. 

This weekend I decided to move my website from Heroku to GitHub Pages. Here is how I went about it.

## Deploying the site to GitHub Pages
In order to publish a Pelican site to GitHub as a User Page, one needs to push the content of the output direrctory generated by Pelican to the master branch of their ```<username>.github.io``` repository on GitHub.

First, I created a new repository named [```joejean.github.io```](https://github.com/joejean/joejean.github.io) on GitHub. Note that this repository name must have the form ```<github username>.github.io```.

Secondly, I installed the Python package ```ghp-import``` and issued the command ```ghp-import output```. This command updates the local gh-pages branch with the content of the output directory (creating the branch if it doesn’t already exist).

And third, I issued the command ```git push git@github.com:joejean/joejean.github.io.git gh-pages:master``` to push the content of the gh-pages branch to the master branch of the github repo where the site will live. After this the site was live and it could be accessed from http://joejean/github.io but I wanted to use my custom domain name "www.joejean.net".

## Setting up the custom domain
I tried many different approaches while setting up the custom domain, but what follows is the only approach that worked for me. 
I started by creating a [CNAME file](https://github.com/joejean/joejean.github.io/blob/cname/CNAME) with the content ```www.joejean.net``` and commit it to a different branch&mdash;which can have any name&mdash; in the same ```joejean.github.io``` repository. Then I merged that branch with the master branch of the ```joejean.github.io``` repository. 

Then I opened the domain administration page at my domain name registrar and I created two A records which points respectivley to the GitHub IPs ```192.30.252.153``` and ```192.30.252.154```. After that, the last step was to create a CNAME record for the subdomain ```www.joejean.net``` that points to ```joejean.github.io```. The following screenshot summarizes the configurations:
<img src ="{filename}/images/dns.png" class="img-responsive img-rounded" />

So now my site is being served from GitHub pages and loads with the same lightning speed no matter when it is accessed. It is important to note that GitHub Pages only work for static sites. 










