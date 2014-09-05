Title: Playing with the World Bank API
Date: 2014-09-05 16:01
Tags: mashups, programming, javascript, api
Slug: playing-with-the-world-bank-api
Author: Joe Jean

As part of my first homework for <a href="https://github.com/craigprotzel/Mashups" target="_blank">Mashups: Creating with web API</a>, I had to first find, post and describe an API that returns JSON data. <!-- PELICAN_END_SUMMARY -->

After playing around with a couple of APIs, I decided to use the World Bank API. I like the fact that
one does not need a key to make requests to this API. And I also found the documentation
to be clear and useful.

I used the following url ```http://api.worldbank.org/incomeLevels/LIC/countries?format=json```
in order to get a list of countries with income level classified as low income. As you can see four parameters are used
in the url. "incomeLevels" is used for information about all levels of income, "LIC" is an acronym that stands for
Low Level Income, and "countries" is the list of countries. By default, the World Bank API returns XML data. Since I wanted JSON, I had to explicitly specify that in the request url using ```format=json```.

For the second part of the assignment, I created a small script that sends a request to the API with the url mentioned above
and display the data on a nicely formatted HTML page. The page can be accessed <a href="" target="_blank"> here. </a>

