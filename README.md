[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18620034)
# slack-bot-sandbox

A repository for experimenting with the Slack API in Python by students in JOUR328, News Application Development.

----------------------------------------------------------------------------------------------------------------------------------
March 15, 2025

My idea for a bot would notify users whenever a federal website gets taken down, by tracking if the website has a 404 or some other related error. This bot would help reporters track down which federal departments and websites might be impacted by the Trump Administration.

The New York Times has already written an article (https://www.nytimes.com/2025/02/02/upshot/trump-government-websites-missing-pages.html) about how thousands of U.S. Government Web Pages were taken down in February. The Times downloaded a list of the most visited government domains in the U.S. (https://analytics.usa.gov/data/live/top-100000-domains-30-days.csv) and then compiled a complete list of pages using the site maps. The Times analysis found more than seven million pages to start with across 150 different sites.

However, even The Times had trouble capturing every single changes on the millions of website pages that the goverment hosts. Especially since The Times navigated this through site maps, rather than downloading actual copies of websites, its approach has some trade-offs.

For my bot, I'm thinking I could just work with the original downloaded list of the most visited government domains in the U.S. Though I'm not sure how I would be able to find errors within each website, or if this scope of a project is way too big for the first ever bot that I'm attempting to do.

As a first step though, I uploaded the same CSV from The Times onto this repository. I also started up my code and downloaded a few Python libraries that I might need.

I'm assuming that I would use requests in Python to each domain, and see if I get any errors in return. This can then be logged into another CSV that will trigger an alert the page is no longer running. Something I'm still wondering, though, is that the original NYT csv is multiple main website pages, and I'm not sure how to find website subpages of the main pages and then compile it into a CSV.

----------------------------------------------------------------------------------------------------------------------------------

March 28, 2025 

This week, I refocused my project on checking when the webpages of research centers and institutes at the University of Maryland are last updated. This is so that I can keep up with if databases or other research centers are being impacted by changes on the federal level. Not only do I want to check if these websites were taken down, but when they were last modified. However, I'm still trying to figure out which specific website links I would like to use, and if I would just like to use the homepages of institutions' websites or if I should be finding the links to specific databases instead. I was able to use Python code that iterates through URLs of different websites, and check the last published or modified date for each link. I was also able to connect this with my already-made Slack script so that my Slackbot will send out a message detailing when websites were last modified. 

For next steps, I want to refine the list of websites I'm checking. I also want to see if there's a way that I can check when the websites were not only last modified, but how they were modified as well. I'm also hoping to set up my Slackbot so that it will only notify me for websites that were changed within the last day or so, so that the notfications are more recent. And I'm hoping that my Slackbot will be able to send updates in real time, which I'm still not sure how to do yet. The blockers I'm encountering are just continuing to figure out the scope of this project and learning how my Slackbot works. However, I have learned how to connect my Python script with my inital Slack bot script, which will let me have a framework as I build more bots in the future. 

----------------------------------------------------------------------------------------------------------------------------------

April 5, 2025 

After working on this bot project for over a few weeks, I’m proud of the progress I’ve made and how I’ve learned to create a Slack Bot. This bot will be very useful in seeing if federal changes will impact research institutions, especially at the University of Maryland. However, finalizing and perfecting this bot came with many challenges that I am still attempting to fix. 

I’m happy that I was able to get my code to go through each University of Maryland institution website and check if the website is updated. Not only does the bot send a message when the website is updated, but it also sends the date of the update. However, a problem with my bot is that it seems to be one day off from a calculation, no matter how I try to fix this error. For example, when I run the code today (on Saturday) it says that the University of Maryland Institute for Governmental Service is updated tomorrow, when I believe it is one day off and it should mean today. I believe this has to do with a discrepancy between timezones, however, when I try to use different libraries to adjust this timezone, it will no longer read all of the links on my site. I tried changing the calculation of the timezone by simply subtracting a day, so that it would be properly adjusted, but even then it still said that many of my websites were updated in the future. I still think I have properly established the foundation to this bot, but that is the one discrepancy that I would like to fix to really solidify this project. 

In the future, I would love to create a CSV that stores data of when websites were updated within the last 24 hours, so that I could keep track of this information for future reporting. A more useful version of this bot would be able to identify the exact change within a website, whether that be the section of the website that’s changed or the exact wording of the website. I’m not exactly sure how to accomplish this next step, but that would be something intriguing to look into. 

Overall, I’m satisfied with this project, despite the date discrepancy. However, once I get this fixed, I do think that this will be a functioning bot that I can use to aid my reporting on the University of Maryland in the future. 
