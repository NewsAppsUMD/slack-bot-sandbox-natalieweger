[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18620034)
# slack-bot-sandbox

A repository for experimenting with the Slack API in Python by students in JOUR328, News Application Development.

----------------------------------------------------------------------------------------------------------------------------------

March 28, 2025 

This week, I refocused my project on checking when the webpages of research centers and institutes at the University of Maryland are last updated. This is so that I can keep up with if databases or other research centers are being impacted by changes on the federal level. Not only do I want to check if these websites were taken down, but when they were last modified. However, I'm still trying to figure out which specific website links I would like to use, and if I would just like to use the homepages of institutions' websites or if I should be finding the links to specific databases instead. I was able to use Python code that iterates through URLs of different websites, and check the last published or modified date for each link. I was also able to connect this with my already-made Slack script so that my Slackbot will send out a message detailing when websites were last modified. 

For next steps, I want to refine the list of websites I'm checking. I also want to see if there's a way that I can check when the websites were not only last modified, but how they were modified as well. I'm also hoping to set up my Slackbot so that it will only notify me for websites that were changed within the last day or so, so that the notfications are more recent. And I'm hoping that my Slackbot will be able to send updates in real time, which I'm still not sure how to do yet. The blockers I'm encountering are just continuing to figure out the scope of this project and learning how my Slackbot works. However, I have learned how to connect my Python script with my inital Slack bot script, which will let me have a framework as I build more bots in the future. 