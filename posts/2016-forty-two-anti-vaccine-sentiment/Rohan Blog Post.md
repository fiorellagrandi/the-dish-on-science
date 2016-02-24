#Quantifying the effects of anti-vaccine sentiment on the spread of disease
---------------------------------------------------------------------
###Background
Anti-vaccine sentiment is as old as vaccination itself.  Edward Jenner published his [results][1] of the smallpox vaccine in 1801, and by 1802, enough people were scared of it that political cartoonist James Gillray produced an extremely unsubtle satirical painting entitled "The Cow-Pock---or---the Wonderful Effects of the New Inoculation!":  

![cowpock.jpg]!\[](https://www.dropbox.com/pri/get/DOS/cowpock.jpg?_subject_uid=239246141&w=AADvXjw6ntGP0ghUXMfIBZtuz-R5BL1ANrb--prhWLOkag)

Even as the smallpox vaccine began to gain ground, a vociferous anti-vaccination movement in [Stockholm][2] which bears striking similarities to the anti-vaccine movements of today, down to charismatic individuals (in this case a Dr. Melander of Visby) proposing quack treatments and making everything worse, led to a steep drop in vaccine coverage in the city and a corresponding dramatic increase in the incidence of the disease.  Nowadays, anti-vaccine movements are still quite influential and have played a role in [pertussis outbreaks][3] in the 60s and 70s, and, more recently, the well-publicized [measles outbreaks][4] linked to Disneyland.  One truly terrifying example is in Nigeria, where distrust of both western intervention and local governments has led to a [boycott][5] of vaccines, which has in turn led to a resurgence for polio in the region.  [Anti-vaccine sentiment][6] is greatly impacting disease dynamics today. 

Despite its obvious presence in real-life scenarios, people have not incorporated human behavior into mathematical models of disease transmission on a wide scale until [relatively recently][7].  One group of researchers that are ahead of the curve is the [Salathé group][website] at Penn State University, who study the interaction between human behavior (specifically anti-vaccine sentiment) and disease dynamics.

###SIR Model
The classic model of disease transmission is called the SIR model.  The SIR model considers a single population of individuals and splits them up into three groups, or "compartments": 1) people (S)usceptible to the disease, 2) people (I)nfected with the disease, and people (R)ecovered from the disease (R).  The model then tracks the rate of change of the number of people in each compartment over time.  

  To model this process you need to know four numbers: the rate of infection ($r$), the rate of recovery from infection ($\gamma$) , the birth rate ($b$), and the mortality rate ($m$).  One way to incorporate vaccination into the standard SIR model is to consider all vaccinated people as "recovered" and then the process of vaccination takes people from S to R.  If you do this, you also need to know the rate of vaccination ($v$).  The below figure depicts this model framework.

![sirmodel.png](https://photos-2.dropbox.com/t/2/AABYAMmCK_wP-cea4aCzJKYYLtwEb2XDtHKbp8sTwbHB7A/12/239246141/png/32x32/1/_/1/2/sirmodel.png/EMHrm9MBGJKBAyACKAI/ilN0evixa3Gpo2CBaJqjt22rVRalyeKyQT99NwdfnWs?size=1024x768&size_mode=3)

A crucial assumption of the SIR model is that the population is well-mixed and that people interact with each other like particles in an ideal gas.  This assumption makes analyzing the model very easy and generally works well in small communities where everybody interacts frequently with each other, but when we start to try to model more complicated scenarios and at larger scales (like the spread of a disease through a city or a country) it doesn't work as well because at these scales people don't actually behave like an ideal gas.  Is your chance of meeting somebody in New York close to your chance of meeting somebody in California?  Is your chance of meeting somebody even in the next city close to your chance of meeting somebody in your own city?  Populations of humans are rarely well-mixed, and so researchers have been forced to come up with ways to remove the assumption of a well-mixed population.  The most common (and probably best) approach is to model the population as a social network.

Social networks are mathematical structures that consist of nodes (which represent people) and edges (which connect the nodes and represent social interactions).   We'll call people who are connected to other people "friends" here, even though you don't have to be a friend to have a social interaction.  If we consider a population as a social network, we can label each node either S, I, or R, and then only allow disease transmission if an S individual is connected to an I individual on the network.  This strategy allows for much more accurate modeling of population structure in epidemiology.  

###Vaccine opinion on social networks

We can also model vaccine opinion formation on social networks.  Salathé and Bonhoeffer [(2008)][8] randomly generated a social network with $2000$ people in it where on average each person has 10 friends.  People were then randomly assigned either a positive or negative opinion of vaccination.  They then modeled opinion spreading by allowing people to change their opinion based on how many friends they have with a different opinion (more friends with different opinions means you are more likely to change your opinion to match theirs).  This opinion-generation process created clusters of people on the network who shared the same opinion.  

After the network was set up, the researchers vaccinated all the pro-vaccine people and infected a random unvaccinated person and then simulated an SIR model where unvaccinated people can get infected with probability proportional to the number of infected friends they have.  An "outbreak" occurred if there were 10 or more people infected at any point in the simulation.

![salbonfig1.jpg](https://photos-5.dropbox.com/t/2/AAAlt9DhGYKgKduOxOTozgIbYDcfYHV6V6BYEIPnFDpo0Q/12/239246141/jpeg/32x32/1/_/1/2/salbonfig1.jpg/EMHrm9MBGJaBAyACKAI/PEDClJiHcivK9rWau1EAeorPgfTjBQudKIt5lpy_1gw?size=1024x768&size_mode=3)

Salathé and Bonhoeffer found that even people only weakly clustered based on their vaccine opinion, the probability of an outbreak dramatically increased.  This effect was strongest at intermediate vaccination levels ($75-85\%$), when there is a decent chance that clusters of unvaccinated people are not isolated from each other by vaccinated people.  So opinion clustering can have a large, potentially very detrimental effect on the spread of a vaccine-preventable disease.

Does opinion clustering actually occur in real populations?  And how do opinion-forming processes really work with respect to vaccines?  The [Salathé group][website] at Penn State have been using [Twitter][xkcdswineflu] to investigate these and more questions. 

###Using Twitter to analyze vaccine sentiment in social networks

Salathé and Khandelwal [(2009)][9] collected all English tweets from August 25th, 2009 to January 19th, 2010 that contained at least one of the following words: vaccination, vaccine, vaccinated, vaccinate, vaccinating, immunized, immunize, immunization, immunizing.  For each tweet, they collected date, time, location, user ID, follower IDs, and friend IDs.  They then developed a statistical classifier (this was very difficult) to sort the tweets into four categories: positive, negative, neutral, and irrelevant.  An example of a positive tweet:  

>off to get swine flu vaccinated before work

An example of a negative tweet: 

>What Can You Do To Resist The U.S. H1N1 "Vaccination" Program? Help Get Word Out. The H1N1 "Vaccine" Is DIRTY.DontGetIt.

An example of a neutral tweet: 

>The Health Department will be offering the seasonal flu vaccine for children 6 months - 19 yrs. of age starting on Monday, Nov. 16.

And finally, an example of an irrelevant tweet:

> Filipino discovers new vaccine against malaria that 'treats' the mosquitoes, too!

The researchers created a Twitter network by taking every user who had at least one positive, negative, or neutral tweet as a single node, and put an edge between users that were followers or friends.  All users were given an overall vaccine sentiment score, which was the net number of positive vaccine tweets divided by the total number of relevant tweets for that user.

![salkhanfig1.png](https://photos-5.dropbox.com/t/2/AACmoStkoDZV93gCBvt0dm9wr29sha3o5YOG3cAl0eOugw/12/239246141/png/32x32/1/_/1/2/salkhanfig1.png/EMHrm9MBGJiBAyACKAI/-IwYP7DY57d3TORgA4b7FbVQYLuBI6i1B__0LoqFp9Y?size=1024x768&size_mode=3)

Overall, $14\%$ of relevant tweets were considered positive and $10\%$ were negative.  There was a positive correlation between sentiment score (which is positive if the sentiment is positive) and vaccination coverage (see figure below), which is useful because it may allow public health efforts to find areas to target with vaccination "communication interventions," as Salathé and Khandelwal put it.

Another interesting result of the Twitter network study was real-time tracking of vaccine opinion dynamics.  The researchers measured the average vaccine sentiment score over time, and found out that over the time frame of the study the score started off negative but then quickly became positive and stayed that way throughout the remainder of the study.  In general, for this study, people are pro-vaccine and relatively consistent about it.  This technique seems like it could be useful in monitoring real-time opinions and therefore being able to intervene in a potentially troublesome population before an outbreak actually occurs due to poor vaccination sentiment.

Does the Twitter network demonstrate opinion clustering?  Do people follow/friend people who share their vaccine opinion?  The researchers measured this quantity by calculating an assortativity coefficient $r$, which is positive if nodes are preferentially connected to nodes of the same type (with a maximum of 1), 0 if the nodes are randomly connected to other nodes (the population is "well-mixed," like in the SIR model), and negative (with the minimum at -1) when nodes are connected preferentially to nodes of opposite type.  For the Twitter network, $r = 0.144$, which implies that people do friend/follow people who share the same opinion, but not to an particularly extreme degree.

###Difficulties for management strategies

So how about actually trying to solve these issues?  Salathé, Vu, Khandelwal, and Hunter [(2013)][10] explored the Twitter network in more depth and found that anti-vaccination sentiment was contagious but pro-vaccination sentiment was not, and that it is possible for exposure to pro-vaccine sentiment to lead to an increase in anti-vaccine sentiment!  This second observation was neatly capture in a survey [study][11] conducted by Brendan Nyhan and colleagues.  This study distributed online surveys that measured a person's initial attitude towards the MMR vaccine, then presented that person with a passage that corrected misconceptions about the vaccine/autism link, a list of risks of measles, mumps, and rubella, a dramatic narrative about a child hospitalized with measles, a picture of a child with measles, or a control passage (on the costs and benefits of bird feeding).  The survey then asked the individuals some questions about the MMR vaccine.  

![nyhanfig2](https://photos-1.dropbox.com/t/2/AACIWJozf96LonkhZzRP5ZpcPDQzpvNWQwVryy6ai_VrMw/12/239246141/jpeg/32x32/1/_/1/2/nyhanfig2.jpg/EMHrm9MBGJqBAyACKAI/tbS07Hapy01gvNL7U1ayGFfYfWErUDiroy9eyaXmfSI?size=1024x768&size_mode=3)

The above figure displays the proportion of people in three categories of initial vaccine sentiment (given by the headers of each of the subpanels) that answered "Very likely" to the question "If you had another child, how likely is it that you would give that child the measles, mumps, and rubella vaccine, which is known as the MMR vaccine?"  The only passage that actually affected the results was the passage that corrected misconceptions, and that passage made people who were unfavorable to vaccines to begin with become even _more_ anti-vaccine!  So the practice of actually disseminating information to increase the incidence of pro-vaccination behavior is a bit more complicated than one would think and requires a lot of serious thought and effort.

If you want more information about the topic of incorporating human behavior into epidemiological models, [these][12] [papers][13] are recent and relevant.

###References
1. Jenner, Edward. _An inquiry into the causes and effects of the variolae vaccinae, a disease discovered in some of the western counties of England, particularly Gloucestershire, and known by the name of the cow pox._ printed for the author, by DN Shury, 1801.
2.  Nelson, Marie Clark, and John Rogers. "The right to die? Anti-vaccination activity and the 1874 smallpox epidemic in Stockholm." _Social History of Medicine_ 5.3 (1992): 369-388.
3. Gangarosa, Eugene J., et al. "Impact of anti-vaccine movements on pertussis control: the untold story." _The Lancet_ 351.9099 (1998): 356-361.
4. Zipprich, Jennifer, et al. "Measles outbreak-California, December 2014–February 2015." _Morb. Mortal. Wkly. Rep_ 64 (2015): 153-154.
5. Jegede, Ayodele Samuel. "What led to the Nigerian boycott of the polio vaccination campaign." _PLoS Med_ 4.3 (2007): e73.
6. Dubé, Eve, Maryline Vivion, and Noni E. MacDonald. "Vaccine hesitancy, vaccine refusal and the anti-vaccine movement: influence, impact and implications." _Expert review of vaccines_ 14.1 (2014): 99-117.
7. Funk, Sebastian, Marcel Salathé, and Vincent AA Jansen. "Modelling the influence of human behaviour on the spread of infectious diseases: a review." _Journal of the Royal Society Interface_ 7.50 (2010): 1247-1256.
8. Salathé, Marcel, and Sebastian Bonhoeffer. "The effect of opinion clustering on disease outbreaks." _Journal of The Royal Society Interface_ 5.29 (2008): 1505-1508.
9. Salathé, Marcel, and Shashank Khandelwal. "Assessing vaccination sentiments with online social media: implications for infectious disease dynamics and control." _PLoS Comput Biol_ 7.10 (2011): e1002199.
10. Salathé, Marcel, et al. "The dynamics of health behavior sentiments on a large online social network." _EPJ Data Science_ 2.1 (2013): 1-12.
11. Nyhan, Brendan, et al. "Effective messages in vaccine promotion: a randomized trial." _Pediatrics_ 133.4 (2014): e835-e842.
12. Funk, Sebastian, et al. "Nine challenges in incorporating the dynamics of behaviour in infectious diseases models." _Epidemics_ 10 (2015): 21-25.
13. Wang, Zhen, et al. "Coupled disease–behavior dynamics on complex networks: A review." _Physics of life reviews_ 15 (2015): 1-29.

[1]:(http://archive.samj.org.za/1945%20VOL%20XIX%20Jan-Dec/Articles/10%20October/2.2%20AN%20ENQUIRY%20INTO%20THE%20CAUSES%20AND%20EFFECTS%20OF%20VARIOLAE%20VACCINAE.%20J.J.%20DuPr'e%20Le%20Roux%20and%20W.F.%20Rhodes.pdf)
[2]:(http://shm.oxfordjournals.org/content/5/3/369.full.pdf)
[3]:(http://www.sciencedirect.com/science/article/pii/S0140673697043341)
[4]:(http://www.cdc.gov/mmwr/preview/mmwrhtml/mm6406a5.htm?s_cid=mm6406a5_w)
[5]:(http://dx.plos.org/10.1371/journal.pmed.0040073)
[6]:(http://www.ncbi.nlm.nih.gov/pubmed/25373435)
[7]:(http://rsif.royalsocietypublishing.org/content/early/2010/05/25/rsif.2010.0142.full.pdf+html)
[website]:(http://www.salathegroup.com/)
[8]:(http://rsif.royalsocietypublishing.org/content/5/29/1505.full.pdf+html)
[9]:(http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002199#s3)
[10]:(http://link.springer.com/article/10.1140%2Fepjds16)
[11]:(http://pediatrics.aappublications.org/content/133/4/e835.short)
[12]:(http://www.sciencedirect.com/science/article/pii/S1755436514000541)
[13]:(http://www.sciencedirect.com/science/article/pii/S1571064515001372)
[xkcdswineflu]:(https://xkcd.com/574/)