# facebook-automated-invite
With the current python script we can use to automatically send invite to users which we would like to invite into a specific Facebook group. The current script will invite one user at a time which later will be limited by facebook as they have a hour limit. I'm yet to find a way how we can invite all the users at once.
Once you clone the script you can run it directly via: WIN+R > cmd > cd (path_to_folder) > python facebook_inviter.py
Script is using selenium and chromedriver to control over Chrome browser and automate the process of login and sending invite (1 by 1) to users from your friend list. 
Have in mind that Facebook has a hour limit of how many users you can invite and will stop you activity when you reach the limit.
