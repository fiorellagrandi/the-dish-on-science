#Quantifying the effects of anti-vaccine sentiment on the spread of disease
---------------------------------------------------------------------
###Background
Anti-vaccine sentiment is as old as vaccination itself.  In 1801, Edward Jenner published his [results][1] of the smallpox vaccine.  By 1802, enough people were scared of it that political cartoonist James Gillray produced an extremely unsubtle satirical painting entitled "The Cow-Pock---or---the Wonderful Effects of the New Inoculation!":  

![Yes, these people are emanating cows.]!\[](https://www.dropbox.com/pri/get/DOS/cowpock.jpg?_subject_uid=239246141&w=AADvXjw6ntGP0ghUXMfIBZtuz-R5BL1ANrb--prhWLOkag)

Even as the smallpox vaccine began to gain ground, a vociferous anti-vaccination movement in [Stockholm][2] which bears striking similarities to the anti-vaccine movements of today, down to the charismatic individuals proposing quack treatments and making everything worse (a Dr. Melander of Visby was 19th-century Stockholm's answer to Jenny McCarthy), led to a steep drop in vaccine coverage in the city and a corresponding dramatic increase in the incidence of the disease.  Nowadays, anti-vaccine movements are still quite influential and have played a role in [pertussis outbreaks][3] in the 60s and 70s, and, more recently, the well-publicized [measles outbreaks][4] linked to Disneyland.  One truly terrifying example is in Nigeria, where distrust of both western intervention and local governments has led to a [boycott][5] of vaccines, which has in turn led to a resurgence for polio in the region.  [Anti-vaccine sentiment][6] is greatly impacting disease dynamics today. 

As long as there are vaccines, there will be people who oppose vaccination and as long as there are people who oppose vaccination, there will be effects of anti-vaccination sentiment on the spread of disease.  Despite these obvious facts, incorporation of human behavior (in particular anti-vaccination sentiment) into mathematical models of disease transmission has only started occurring [relatively recently][7].  In this article I will highlight the work of the [Salathé group][website] at Penn State University conducted on the interaction between human behavior (specifically anti-vaccine sentiment) and disease dynamics.

###SIR Model
The classic model of disease transmission is called the SIR model.  The SIR model considers a single population of individuals and splits them up into three groups, or "compartments": 1) people Susceptible to the disease (S), 2) people Infected with the disease (I), and people Recovered from the disease (R).  The model then tracks the rate of change of the number of people in each compartment over time.  

  This process is usually modeled with four parameters: $r$ is the rate of infection, the rate at which people move from the S compartment to the I compartment; $\gamma$ is the rate of recovery, the rate at which people move from the I compartment to the R compartment; $b$ is the birth rate, the rate at which people enter the population (usually in the S compartment); $m$ is the mortality rate, the rate at which people leave the population (by dying). 

![standard SIR model](https://photos-2.dropbox.com/t/2/AABYAMmCK_wP-cea4aCzJKYYLtwEb2XDtHKbp8sTwbHB7A/12/239246141/png/32x32/1/_/1/2/sirmodel.png/EMHrm9MBGJKBAyACKAI/ilN0evixa3Gpo2CBaJqjt22rVRalyeKyQT99NwdfnWs?size=1024x768&size_mode=3)

We usually assume that the population size is constant over time, so that $b=m$ (the birth rate equals the death rate).  This assumption is clearly wrong, but it isn't usually wrong by that much (at the time scales we study most infectious diseases population growth isn't really important) and it simplifies analyses considerably.

If you want to incorporate vaccination into an SIR model, you have two choices: 
1. Create a new compartment, V, for vaccinated individuals, and a new parameter $v$, for the rate of vaccination, the rate at which people move from the S compartment to the V compartment
2. Put all vaccinated people in the R compartment and create a new parameter $v$ that is the rate at which people move from the S compartment to the R compartment.  The diagram above shows this version with the dashed line.

A crucial assumption of the SIR model is that the population is well-mixed and that people interact with each other like particles in an ideal gas: interaction rate is proportional to the frequencies of both susceptible and infected individuals.  This assumption is also clearly wrong: is your chance of meeting somebody in New York close to your chance of meeting somebody in California?  Is your chance of meeting somebody even in the next city close to your chance of meeting somebody in your own city?  People don't interact like particles in an ideal gas, and populations of humans are rarely well-mixed (although advances in transportation technology are making this statement increasingly false).  Unlike with the assumption of constant population size, real populations behave dramatically differently from a well-mixed population.[^footnote]  What do people do to get around this quite clearly incorrect assumption?  The most common (and probably best) approach is to model the population on a social network.

Social networks are mathematical structures that consist of nodes and edges.  Each node is a person, and each edge connects two nodes and represents a social interaction.   We refer to nodes connected by at least one edge as "neighbors". If we consider a population as a social network, we can label each node either S, I, or R, and then only allow disease transmission if an S individual is connected to an I individual on the network.  This strategy allows for much more accurate modeling of population structure in epidemiology.  

DIAGRAM THAT ILLUSTRATES THE DIFFERENCE BETWEEN INTERACTIONS IN A WELL-MIXED POPULATION AND ON A NETWORK.

[^footnote]: The reason people even bother with a well-mixed population is that it is astronomically easier to analyze than a network model.  We usually have to simulate everything when using a network model but with a well-mixed model we can do lots of things by hand.

###Vaccine opinion on social networks

We can also model vaccine opinion formation on social networks.  Salathé and Bonhoeffer [(2008)][8] used the following model:

1. Randomly generate a social network (with $2000$ people in it) so that on average each person has $10$ neighbors.  Initially, everybody is disease-susceptible (S).
2. For each person in the network, flip a coin with probability $c$ of heads and probability $1-c$ of tails (real coins have $c \approx 0.5$).  If heads, the person is assigned a positive opinion about vaccination.  If tails, the person is assigned a negative opinion about vaccination.[^footnote2]  
3. For each person, calculate the proportion of its neighbors that do not share its opinion and call this proportion $d$.  If, for example, an anti-vaccine person has $10$ neighbors and $4$ of them are pro-vaccine, then $d=0.4$.
4. Choose a parameter $\Omega$ between $0$ and $1$ that symbolizes the "strength of opinion formation".  This parameter measures how likely a person changes his opinion based on the proportion of neighbors that are of a different opinion.  
5.  Randomly choose a person and flip a coin, this time with probability $d\Omega$ of heads, where $d$ is the value of $d$ for this person.  If heads, the person's opinion changes from positive to negative or from negative to positive and you now have to recalcualte $d$ for the neighbors.  If tails, nothing happens.
6.  If you switched someone's opinion in step 5, randomly choose someone with the same opinion as the new opinion for the person in step 5 and flip a coin with probability $d\Omega$.  If heads, switch the new person's opinion and recalculate $d$ for the neighbors.  Repeat this step until you get a heads.  This step is to ensure that the proportion of people with anti-vaccine sentiment stays the same throughout the opinion-formation process.
7.  Repeat steps 5 and 6 as many times as you want ($N$ times).
8.  Vaccinate all pro-vaccine individuals (change their label to R).
9.  Infect a random susceptible individual (change its label to I).
10. Begin the simulation. For each time step, any susceptible individual becomes infected with probability $1-e^{ri}$, where $i$ is the number of infected neighbors.  Also at each time step, any infected individual can recover with probability $\gamma$. 

[^footnote2]: Note that this does NOT mean than exactly $2000c$ individuals will be pro-vaccine, but rather than on average (if you repeat this network generation process over and over) $2000c$ individuals will be pro-vaccine.

Salathé and Bonhoeffer set $r=0.05$ and $\gamma=0.1$ and ran the simulation for $300$ time steps.  They called it an "outbreak" if there were at least $10$ new infections.  

The opinion-formation process here is supposed to simulate the idea that people are likely to change their opinion to match the opinion of people they interact with.  This process is likely to create opinion clustering, where pro-vaccine people are likely to have pro-vaccine people as neighbors and anti-vaccine people are likely to have anti-vaccine as neighbors.

![Figure 1 from Salathé and Bonhoeffer 2008](https://photos-5.dropbox.com/t/2/AAAlt9DhGYKgKduOxOTozgIbYDcfYHV6V6BYEIPnFDpo0Q/12/239246141/jpeg/32x32/1/_/1/2/salbonfig1.jpg/EMHrm9MBGJaBAyACKAI/PEDClJiHcivK9rWau1EAeorPgfTjBQudKIt5lpy_1gw?size=1024x768&size_mode=3)

Salathé and Bonhoeffer found that even weak opinion formation (and therefore weak opinion clustering) dramatically increased the probability of an outbreak (for example, $\Omega = 0.5$ led to an increase in outbreak probability of almost $20\%$ when vaccination coverage was at around $80\%$).  Interestingly enough, the effect was strongest at intermediate, relatively high values of vaccination coverage ($c$).  This is because if vaccination coverage is low, most people aren't going to get vaccinated anyway, so clustering them together doesn't make any difference (any random individual already has a high chance of having anti-vaccine neighbors without any clustering necessary).  If vaccine coverage is super high ($> 90\%$), then clustering also has no effect because there are just too many vaccinated people; each person has a very high probability of having mostly pro-vaccine people as neighbors anyways.  It is in the intermediate cases where clusters of anti-vaccine (and therefore susceptible) individuals can form and have a local outbreak.  These intermediate cases still have relatively high vaccine coverage ($75-85\%$), which is pretty concerning because those are the levels vaccine coverage is dropping to in some areas SOURCE.  Another interesting result is that even when vaccination coverage was high, opinion clustering dramatically increased the probability of an outbreak (at a coverage of $90\%$ the outbreak probability with clustering was about the same as that of coverage at $70\%$ with no clustering).  So opinion clustering can have a large, potentially very detrimental effect on the spread of a vaccine-preventable disease.

I SHOULD MAKE GRAPH GIFS WITH EXAMPLE SIMULATIONS FOR EACH OF THE THREE CASES

Does opinion clustering actually occur in real populations?  And how do opinion-forming processes really work with respect to vaccines?  Salathé's group at Penn State have been using Twitter to investigate these and more questions. 

###Using Twitter to analyze vaccine sentiment in social networks

Salathé and Khandelwal [(2009)][9] collected all English tweets from August 25th, 2009 to January 19th, 2010 that contained at least one of the following words: vaccination, vaccine, vaccinated, vaccinate, vaccinating, immunized, immunize, immunization, immunizing.  For each tweet, they collected date, time, location, user ID, follower IDs, and friend IDs.  They then developed a statistical classifier (this was very difficult to do) to sort the tweets into four categories: positive, negative, neutral, and irrelevant.  An example of a positive tweet:  

>off to get swine flu vaccinated before work

An example of a negative tweet: 

>What Can You Do To Resist The U.S. H1N1 "Vaccination" Program? Help Get Word Out. The H1N1 "Vaccine" Is DIRTY.DontGetIt.

An example of a neutral tweet: 

>The Health Department will be offering the seasonal flu vaccine for children 6 months - 19 yrs. of age starting on Monday, Nov. 16.

And finally, an example of an irrelevant tweet:

> Filipino discovers new vaccine against malaria that 'treats' the mosquitoes, too!

The researchers created a Twitter network by taking every user who had at least one positive, negative, or neutral tweet as a single node, and put an edge between users that were followers or friends (in the appropriate direction).  All users were given an overall vaccine sentiment score, which was the net number of positive vaccine tweets divided by the total number of relevant tweets for that user.  Only users with nonzero vaccine sentiment score were kept in the network.  The resulting network had $39,284$ nodes and $685,719$ edges, where $34,025$ nodes ($87\%$) formed a single connected ("giant") component of the network.

![Figure 1 from Salathé and Khandelwal 2009](https://photos-5.dropbox.com/t/2/AACmoStkoDZV93gCBvt0dm9wr29sha3o5YOG3cAl0eOugw/12/239246141/png/32x32/1/_/1/2/salkhanfig1.png/EMHrm9MBGJiBAyACKAI/-IwYP7DY57d3TORgA4b7FbVQYLuBI6i1B__0LoqFp9Y?size=1024x768&size_mode=3)

Overall, $14\%$ of relevant tweets were considered positive and $10\%$ were negative.  There was a positive correlation between sentiment score (which is positive if the sentiment is positive) and vaccination coverage (see figure below).  This correlation is a useful finding because it would allow public health efforts to find areas to target with vaccination "communication interventions," as Salathé and Khandelwal put it.

Another interesting result of the Twitter network study was real-time tracking of vaccine opinion dynamics.  The researches measured the average vaccine sentiment score over time, and found out that over the time frame of the study the score started off negative but then quickly became positive and stayed that way throughout the remainder of the study.  Thus, in general people are pro-vaccine and relatively consistent about it.  This technique seems like it could be useful in monitoring real-time opinions and therefore being able to intervene in a potentially troublesome population before an outbreak actually occurs due to poor vaccination sentiment.

Does the Twitter network demonstrate opinion clustering?  Do people follow/friend people who share their vaccine opinion?  The researchers measured this quantity by calculating an assortativity coefficient $r$, which is a little complicated but basically is positive if nodes are connected to nodes of the same type (with a maximum of 1), 0 if the nodes are randomly connected to other nodes (the population is "well-mixed," like in the SIR model), and negative (with the minimum at -1) when nodes are connected to nodes of opposite type.  For the Twitter network, $r = 0.144$, which implies that people do friend/follow people who share the same opinion, but not to an particularly extreme degree.

The researchers also divided up the network into densely-connected "communities" and found that all but one community had a much higher or much lower proportion of users with negative attitudes towards vaccines, further strengthening the argument that vaccine opinions cluster.  They also conducted some disease simulations similar to those I described above and found that if the level of clustering in an actual population were to be the same as that seen in the Twitter network, the risk of an outbreak strongly increases.

###Difficulties for management strategies

So how about actually trying to solve these issues?  Salathé, Vu, Khandelwal, and Hunter [(2013)][10] explored the Twitter network in more depth and found (in a very technical paper that I do not recommend you actually read) that anti-vaccination sentiment was contagious but pro-vaccination sentiment was not, and that it is possible for exposure to pro-vaccine sentiment to lead to an increase in anti-vaccine sentiment!  This second observation was neatly capture in a survey [study][11] conducted by Brendan Nyhan and colleagues.  This study distributed online surveys that measured a person's initial attitude towards the MMR vaccine, then presented that person with a passage that corrected misconceptions about the vaccine/autism link, a list of risks of measles, mumps, and rubella, a dramatic narrative about a child hospitalized with measles, a picture of a child with measles, or a control passage (on the costs and benefits of bird feeding).  The survey then asked the individuals some questions about the MMR vaccine.  

![Figure 2 from Nyhan et al. 2014](https://photos-1.dropbox.com/t/2/AACIWJozf96LonkhZzRP5ZpcPDQzpvNWQwVryy6ai_VrMw/12/239246141/jpeg/32x32/1/_/1/2/nyhanfig2.jpg/EMHrm9MBGJqBAyACKAI/tbS07Hapy01gvNL7U1ayGFfYfWErUDiroy9eyaXmfSI?size=1024x768&size_mode=3)

The above figure displays the proportion of people in three categories of initial vaccine sentiment (given by the headers of each of the subpanels) that answered "Very likely" to the question "If you had another child, how likely is it that you would give that child the measles, mumps, and rubella vaccine, which is known as the MMR vaccine?"  The only passage that actually affected the results was the passage that corrected misconceptions, and that passage made people who were unfavorable to vaccines to begin with become even _more_ anti-vaccine!  So the practice of actually disseminating information to increase the incidence of pro-vaccination behavior is a bit more complicated than one would think and requires a lot of serious thought and effort.

###Conclusions

The research I have highlighted here provides evidence for a few related claims: one, that anti-vaccination sentiment clusters in populations, 2) that such clustering increases the risk of epidemics, and 3) we can use social media as a source of data to try to analyze this clustering and to try to prevent outbreaks from occurring in the future.

Incorporating human behavior in general (and anti-vaccination sentiment in particular) into population models of the spread of contagious diseases is becoming more and more popular.  The research I have discussed above is only (mostly) the work of a single group of people.  There has been much more work done on the subject in recent years (see [this paper][7],  [this paper][12], and [this paper][13] for reviews of the field).  However, we have still only scratched the surface of the relationship between human behavior and disease, especially now that we have the treasure trove of human behavioral data that is [social media][xkcdswineflu].  Considering what we as scientists have [already accomplished][xkcdpolioday], just think of how much more we can do with all this new information and more sophisticated modelling techniques.  The future of epidemiology is bright.

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
[7]:(http://rsif.royalsocietypublishing.org/content/early/2010/05/25/rsif.2010.0142.full.pdf+html)
[website]:(http://www.salathegroup.com/)
[8]:(http://rsif.royalsocietypublishing.org/content/5/29/1505.full.pdf+html)
[9]:(http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002199#s3)
[10]:(http://link.springer.com/article/10.1140%2Fepjds16)
[11]:(http://pediatrics.aappublications.org/content/133/4/e835.short)
[12]:(http://www.sciencedirect.com/science/article/pii/S1755436514000541)
[13]:(http://www.sciencedirect.com/science/article/pii/S1571064515001372)
[xkcdswineflu]:(https://xkcd.com/574/)
[xkcdpolioday]:(https://www.gatesnotes.com/Health/XKCD-Marks-the-Spot)