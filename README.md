## Inspiration<br>

All of us have multiple chats in which there is definitely an instance where we have asked our friend to give a mind-blowing caption for a beautiful picture to put it up on social media. 
That particular friend of our's probably googles a good caption and suggests it. 
CaptionMe.ai is intended to be exactly that friend -only more original! 

## What it does<br>

CaptionMe.ai is intended to be a API for suggesting captions for pictures by detecting the key elements and using persona and sentiment analysis to suggest a caption that a particular person might like.
It is intended to be intelligent and learn with time , what kind of captions might be liked by the user so that accurate suggestions can be made.

## How we built it<br>
The following points are how we basically built it:<br>
1) In 24hrs :P <br>
2) Computer Vision/Image Recognition.: We have used a set of data , annotated it to train an Image Classification and Object Detection model to give an idea of the elements and the theme of the picture. <br>
3) Persona Creation : For the vanilla version of the project we have created personas of celebrities who are very active on social media such as twitter and Instagram. We have used their tweets and captions to create a score vector which captures the emotions of their captions.<br>
4) Sentiment Analysis : Created a database of good/meaningful captions and quotes. We used the theme and objects detected from the picture to filter out these captions further to make it contextual.
We ran sentiment analysis on this and classified them as Positive or Negative. Using this we further analyzed it for detailed vector similar to persona to get the emotion of the caption.<br>
5) Comparison and Suggestion : We compared the Persona vector with the analyzed quotes and ran a normal score comparison to get top 5 quotes/captions that the user might like.<br>

## Challenges<br>

1) Persona Creation is often very tricky and ideally should involve a lot of characteristics. In this vanilla version we have considered only 5 celebrities and included their tweets as well for increasing the accuracy of persona. <br>
2) The iterative AI algorithm will need a lot of RnD and we intend to implement this as a plugin to social media sites<br>


## Accomplishments

Computer Vision and NLP both done to a very good accuracy in 1 day for the vanilla version.
Originality to get the personas for giving the top 5 suggestions for captions

## Learnings

1) Tensorflow-keras, Nltk packages practical usage.<br>
2) Accuracy training <br>

## What's next for CaptionMe.ai

Future Scope : <br>
1) Web Scrape captions from users to train a AI model which will learn as and when new captions are put up or new social activity is done by the user ( with due permissions ) <br>
2 ) Robust Object Detection <br>
3) Personality traits should include characteristics as Liberal, Inspiring , Goal-driven etc which can be used to make user profiles and has a variety of applications ( Advertisement , recommender etc) <br>
4) Video Captioning <br>
5) Instagram Plugin <br>
