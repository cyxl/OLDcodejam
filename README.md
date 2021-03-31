# cyxl-org
* This is my personal website but I have my Code submition here too!

## S-Tracker

S-Tracker is a social media tracker made be me, cyxl

I made this for a Tech With Tim codejam compitition 

The tracker has 1 feature right now and that is youtube tracking. I am planning to add more features like a chess elo tracker using there api, and a tiktok tracker.

## Features
1. [YoutubeTracker](#YoutubeTracker)


## **[YoutubeTracker](https://cyxl-cj-dot-sound-scene.uc.r.appspot.com/cj/youtube)**

I collect the data everynight at 9:00pm EST. I have a list of youtubers I track [here](youtubers.md). 

### How to use

Add gif here.

### Software used
* YoutubeData api v4 | For reciving data
* Firebase Realtime Datatbase | To store data
* Firebase Admin | To store/recive data from code
* Bokeh | Used to generate graphs
* Flask | Used to rought

### What it stores
* Subsribers
* Name of Youtuber
* Youtuber ID
* Youtuber bool(hiddensubscribers)
* Youtuber Subscribers
* Youtuber Views
* Youtuber Videos

### FAQ
* How do I generate a youtubers stats? Go to cyxl.org/stracker/youtube and in the search bar labeled YoutubeTracker scearch the Youtuber ID | I am gonna make it you you can search for there name also soon.
* How do I add a youtuber? First you go to cyxl.org/stracker/youtube and then you go to the bottom and find the bar that says add a youtuber and put in the youtuber's ID.
* A tried to add a youtuber but it didnt work, what should I do? First check if your youtuber you are trying to track meets the [requirements](requirements.md), then if it still dosnt work ping cyxl# in the TechWithTim discord and I will manualy add it. This should never happen. 
* How do I find a youtuber's id? To find a youtubers ID look at this [website](https://ultimate.brainstormforce.com/docs/how-to-find-youtube-channel-name-and-channel-id/)

## Examples
* Data example | At the top you can see the timestamp and the 0 is a list number. I have it so the name and id are the parents to the data.
![Data](https://github.com/cyxl/cyxl-org/blob/master/GithubPictures/CodeJam/data_show.png)

* Graph
Add picture here
