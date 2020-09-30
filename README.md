# Introduction

As the internet becomes bigger and applications become more complex, the "simple" front end we all know and love is slowly dying. It still works well for certain types of websites, but the user (and the developers) are getting more and more accustomed to a more complex, but more extendable, way of building things.

The purpose of this project is to build a React front end that interfaces with a Django Rest Framework back end running on the same machine.

The GhostPost Machine™ is a website where people can anonymously post Boasts or Roasts of whatever they want. Like Twitter, there is a character limit: 280 characters. We are deliberately not dealing with logins, as that is outside the scope of the project (and beyond our time constraints).

## Task

Build a back end API using Django Rest Framework. This API will connect to your front end React app and serve the required data.

## Back end

Model(s) for boasts and roasts with appropriate attributes as derived from other requirements
GET, and POST endpoints for boasts and roasts
POST endpoints for voting on boasts and roasts
hint: add extra actions (Links to an external site.)Links to an external site. to your viewset
Note: You will likely run into issues with CORS --> https://www.django-rest-framework.org/topics/ajax-csrf-cors/#cors (Links to an external site.)Links to an external site.

## Extra credit (4 points)

Add a DELETE method that works for both boasts and roasts. "Wait, how will we delete if it's anonymous?", I hear you ask. When a boast or a roast is created, it should have a random 6 character string associated with it (so that it's hard to guess). If that string is sent in a URL with the DELETE method to the boast or roast endpoints, then it should delete the object. For example, if boast 2 has the "magic string" of "abcdef", then you would use a GET call on  localhost:8000/api/posts/2 and a DELETE call against localhost:8000/api/posts/abcdef. When the object is created, the magic string should be passed back to the front end and given to the user; something like "If you want to delete your post, click this link!"
Submission
Create a pair of repositories, one for the front end and one for the back end.

Link each one in the readme for the repos, then submit either one.

## Repository URLs

GitHub Back End URL [<https://github.com/cheriaa43/ghostpost_backend>].
GitHub Front End URL [<https://github.com/cheriaa43/ghostpost_frontend>].
