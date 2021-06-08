# volleyball-data-wrangling


## Specifications

Name: String  
Week No.#: Int - OR TOTAL -  
Serve Errors: Int  
Serve Success: Int  
Serve % = Serve Success / SE + SS Float  
Receive Errors (No consecutive Touch): Int  
Receive Passes (Consecutive Touch must’ve been made): Int  
Receive % = Receive Passes / RE + RP Float  
Spike Errors (No consecutive Touch): Int  
Spike Success (Goes over the court and is not out): Int  
Spike % = Spike Success / HE + HS  
Block Errors (Play ends after block with point loss, must’ve contacted ball): Int  
Block Successes (No point loss, play resumes or ends): Int  
Block % = Block % / BE + BS Float  
Faults: Int  


Need to be able to view team stats (all players combined) over the week and total. Need to be able to view a certain players stats over the week and total.  
Need to be able to add in data for a specified week, and be able to create new weeks.  


## GUI 


VIEW TEAM STATS -> CHOOSE WEEK \ ALL WEEKS  
VIEW PLAYER STATS -> CHOOSE PLAYER -> CHOOSE WEEK \ ALL WEEKS  
ADD STATS -> CHOOSE PLAYER -> CHOOSE WEEK      
-----------> ADD NEW PLAYER  

MAYBE: Separate Week by Seasons? Remove Player?  
