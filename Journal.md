Date: 8.29.2025 - Subject: We coverd how to generate ssh keys, which i have done be for for github it I kinda forgot how it worked so the refresher was nice. I also didnt know that  ssh -T git@github.com was a command that could check your git hub connection status. Also im glad that I use a mac since windows with WSL looks like a pain. 

Date 9.5.2025 - Ask good questions get product owners/ people to really say what they want and need, people dont always know what they want but the do know that the have a problem usually. Then read it back draw pictures anything to make sure that what they are saying is what they want. product managers can be satiated by having good estimations and help get your stuff done. The Flask assignment was helpful in friguring out to host things localy Im going to take some screenshots to document it since there are a lot of words to copy. 

Date 9.10.25 - Know the domain you are working in, regardless of how good of a programmer you are if you dont know the doamin it can be challenging to code anything for it. 

Date 9.12.25 - talked about branch merging and how to do it, if you have a conflict use git pull --no-rebase so that it pulls down the main branch and you can edit them in your ide to fix the conflict and then you can push, and everyone will need to pull again 

Date 9.15.25 - how to make a new branch "git checkout -b {new_branch_name}" to set new branch as your working branch" git git push --set-upstream origin {branch_name}" to switch between branchs use "git switch {desired_branch}" then you must deleeat an old branch that is no longer in use by "git branch -d {branch_name}"  

Date 9.22.25 - Some key things for a impactfull presentation are, Who's the audiance, What are goals, and Design Principles, and  color can be very usefull. some color guides are, Red is for alerts, Yellow(soft) is for highlighting changes, Green is good and familiar things, Gray is out of scope, Blue is for neutral, and orange is for things that are changing. Be consitance with shapes use diffrent shapes for diffent things just make sure the reason for this is obvious and clear.

Date 10.03.25 -Project Management has different processes depending on the person. and for this class story points are our measurements. WHICH IS NOT TIME, its complexity not how long it will take. 
    
    A Gant chart is a way to help see how long something could take. You have your timeline on the top and features listed vertically on the side, and you can measure how long a feature will take. This won't always be correct since its estimates, these charts have an uncanny similarity to cpu task charts. This chart can also help keep track of how much is done, yet with bad estimates it can be inaccurate when you say “ I'm 80% of the way done” and that last 20% is the slowest part. This chart's value is mostly to help executives feel like they have some control over how the project is going. 
    
    A Kanban Board can be better by keeping simplicity, with three sections: a TODO, in progress, and a Done section where you can put your tasks. It's a simple way to track and you can even color code for measure difficulty.

    Also the def of done: is diffrent for each stakeholder form sales, markiting, managemtnet, and others. and there needs to be a set def between these groups. for engineers, the common def is the code compleat, tested, reveiwed(fix issues),and then merge(intergration test)   

Date 10.08.25 - eXtreme programming, is an agile software dev methodology that emphasizing high quality software, and cutomer responsiviness, through simplicity, communication, feedback, courage, and respect. some of the preactics are pair programing, test drivin devolpment, contiunus intergration, frequent releases, and collective code ownership 

Date 10.13.25 - ethics in code, can be a difficult idea. going over the trolly problem is interesting with how subtle changing of a senario can have a large inpact on what people thing what the correct thing to do. 

Date 10.20.25 - what is software quality, does what it says, easy to use, secure, predictable, presetent. How can you improve the quality of your software? Testing, planning architecture, refactoring, foucus on subsytems. Our tests are limited by our understanding on the software. Basicly software we write and tests for that software will not be very usefull since its our own tests against our owwn code which means it could have the same inherint flaws. 

    python has something called a test harness called pytest and you can use it to test code 

    Quality is built from the ground up and is the responsibility of the developer. 
    to ensure quality a solid regimen of rigouris testing must occur. 
    your never going to be 100% positive

Date 10.27.25 - Refactoring was made to help with Maintainability, Reusability, Preformance, and Cost Reduction. I am also the scrum master for this week 
    projects at week start: 
        Cameron    - add the tables to supabase 
        Dayne      - API 
        Elliot(me) - Importing Supabase to replace the tiny db in the handelers and db files 
        Emma       - UI and pages 
        Suzzanne   - db intergration 

    
    
Date 10.29.25 - Try to keep code reusable. do this by minimizing set up code and making it into its own function. the most inportant reason of re-usabillity in refactoring is becasue it allows others to work on other projects since clean and resuable code frees up so much dev time. Effciency and preformance is valuble, but most fo the time it isnt noticable, BUT code that runs all the time or massive wait times it cen be in your intrest to optimize it. last there is cost reduction

Date 11.03.25 - there are a lot of steps in deploying software. it often goes from you to dev enviroment to QA testing to User acceptence tests then to users. and even if you get a promblem on one part of the cycle you do NOT jsut fix it and send it back to where it was. You start over and keep the cycle intact. 

Date 11.07.25 - we talked about coverage and lint and they can be used for helping see how much code is being used for your unit tests and lint can be used to help clean up code and you can just pip install {lint or coverage}