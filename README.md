# project-wildfire
# dev branch
Using similarity distance and machine learning algorithms to detect wildfires and show information about them to relevant people. Part of NASA's app challenge 2019. https://www.spaceappschallenge.org/  www.marlwoodcodeclub.org

Yes, there have been hundreds of projects like this in the past. But they're fun, they teach machine learning, and they can be useful! This one is being built to work in Indonesia as they don't have any wildfire prediction algorithms right now and they have very bad wildfires.

This has introduced some interesting challenges: First off, they don't have that much processing power, so they can't do much on site processing and applications need to be fast.

The biggest one is their low bandwidth: about 5mbps. We can't send them massive JSON files with all the data for the area in.

Because of these two problems, we are going to:

*   Do all processing server side, and only add wildfires to the API.
*   Not keep additional information about the wildfire with the API. The client will have to request additional data when required. 

That is, if we finish it. We have two days!


PS Mostly writing this readme because I am out of things to plan. This will probably be my last commit until Wednesday.
