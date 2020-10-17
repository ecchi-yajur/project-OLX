# project-OLX

# OLX Fraud Analysis 
## INTRODUCTION

Recently online classified sites have become a popular way to sell goods or services. The popularity of websites such as OLX, Quikr, eBay and now with Facebook entering with its marketplace are continuously rising. The World Wide Web provides a convenient, cheaper and easy way for people to browse and post advertisement as compared to newspapers and printed booklet. The increasing popularity of online classifieds has led to gaining unwanted attention of scammers posing as genuine sellers attempting to defraud buyers[1][2].


Telephony has been an effective method for scammers from a long time, according to Truecaller report 22.1M Americans lost $9.5B in 2017 to these scammers [3]. There is no proper reporting of these frauds. Also, these companies generally do not publicly report fraud numbers. Many victims do not publicly report about these frauds because of embarrassment from friends or family or due to lack of proper knowledge about where to report them. 


In 2017 OLX recorded a groundbreaking 58% surge in profit at ₹92.5 crores as compared to ₹58 crores in FY16[Tofler], whereas Quikr recorded a 52% jump at ₹199.98 crores in FY18 as compared to FY17 [Ministry of Corporate Affairs (MCA) filings]. By 2020 Indian Online Classified market is expected to be worth ₹7700-7900 crores [KPMG and Google India]. Considering that most of the ads placed on these sites are free any person listing an ad must be expecting a net profit, the amount of money being traded through the platform is much greater than its net revenue.


With transactions on order of tens of thousands to lakhs it is imperative that these sites must take measures to detect potential fraudulent activity. We went through OLX policies and found out that sellers must not post their phone numbers or their personal information. 

![alt text]( https://github.com/ecchi-yajur/project-OLX/blob/main/Images/Screenshot%20(61).png)

But sellers find creative ways to post them. 

![alt text]( https://github.com/ecchi-yajur/project-OLX/blob/main/Images/Screenshot%20(63).png)

This research focusses on applying text mining techniques to discover patterns in classified ad data.

## DATA

In this section we will discuss our methodology for collecting classified ad data which we later use to detect presence of phone numbers. These ads will then be tagged according to presence of phone numbers. We picked OLX as our starting point as most of the ad data was already public. 

![alt text]( https://github.com/ecchi-yajur/project-OLX/blob/main/Images/Screenshot%20(65).png)

