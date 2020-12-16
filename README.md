# Data Centric Development - Code Institute Milestone Project Three - Matt Inglis

## *Dungeon Club - A resource/database site for players of Dungeons and Dragons 5th Edition.*

![Image of Yaktocat](https://i.imgur.com/43YfaMH.png)

## Deployed link via Heroku: https://matt-inglis-ms3.herokuapp.com/

# Overview

The goal of this site, as a huge fan and player/DM of Dungeon's and Dragons (D&D), is to create something that I felt would be really handy and beneficial to supplement the game's experience. 

Dungon Club allows the user to achieve the following:
* Quickly look up Character Races/Classes/Spells and other rules/information, via a dataset created from the official D&D SRD. This is a free-use document for the creation of content based around the subject of D&D. 
* Choose from a list of official Source/Campaign books, with cover art, descriptions and links to purchase.
* Sign up for a secure account to gain access to a Profile area. This profile allows the user to create quick cards for all the characters for their games, and also a Quest To-Do list, to keep track of their in-game objectives. The site also has functionality to securely delete their account as they see fit.

# UI/UX

The wireframe for this site can be found in the submission_assets directory of the repository or at [this link.](https://github.com/mattingliscoding/code-institute-milestone-project-three/blob/master/submission_assets/matt-inglis-ms3-wireframe.pdf)

One of the first things I did was to try to find other websites that were doing a similar thing, with regard to displaying information from the D&D SRD. Many of the sites I found were lacking in any intuitive UI/UX choices and many looked extremely dated. However, one site I took great inspiration from was dndbeyond.com. They are a large company, that officially licenses D&D content and products in a scaled-up version of what I was aiming for with Dungeon Club.

I opted for a simple Bootstrap 4-oriented design, to focus on functionality and the maximising the easy access to the dataset, created via MongoDB Atlas. Due to the specified nature of the site, I wanted it to be simple and smooth for players of the game to arrive and instantly know where they needed to navigate to search for the information they needed for their gaming experience.

## User Stories

* As a user of Dungeon Club, I would like to quickly navigate through the menu to pull up the information I need.
* As a user, I would like the process of making an account be simple and secure.
* As a user, I would like to see a list of currently available products for the game, with images, descriptions, prices and easy links to purchase them.
* As a user, I would like to have a place to store characters I've made for various games I've been a part of.
* As a user, I would like to be able to keep a to-do list/log of current missions and quests I have undertaken during my games.
* As a user, I would like to be able to delete my account with minimal fuss.

# Features
* **Navigation bar, with brand and page links (All pages)** - This header was created using Bootstrap, and gives the user a clear point of navigation control and is focused on ease-of-use. The collapse feature from Bootstrap also features heavily across the site, helping to keep the site expandable and accessible on smaller screens.
* **Hero Image (All pages)** - The consistent use of the 'hero' banner across the pages helps the site feel fluid and light-weight, by letting the user become accustomed to the familiar UI across all the pages.
* **Cards (All pages)** - The card and shadow classes from Bootstrap 4 adds a sense of dynamicism and depth to the UI, while also engaging in the 'Material' style of web design.
* **Home Page - News Section** - Links to current news in the sphere of D&D keep the site feeling up-to-date and alive.
* **5th Edition Database Page** - The sidebar menu drops down smoothly and intuitively, so as to not let the user get lost or confused in the longer menus. The list items in the menu are colour coded when hovered over or focused on to also help the user. On smaller screens, the menu changes to a middle position for smooth ease-of-use.
* **5th Edition Database Page - Data Populated Card** - The selection from the menu is triggering the respective function inside the Python app file, using Flask to query the database. The card on screen is then populated via loops using the Jinja templating language to display the stored information from the MongoDB collection for the chosen document.
![Screenshot of database display cards](https://i.imgur.com/Ra79HmJ.png)
* **Resources Page** - The cards on the resources page are once again utilising the Jinja loops to fetch and display the information for each of the products listed. The Jinja loops iterates over one Bootstrap Card Deck element in the HTML and fills the page with all the products available.
* **Profile Page - Quest To-Do App** - The feature to add a quest allows the user to keep a log of their games missions and objectives in a handy to-do format, using a Bootstrap form. The inputs are stored in a MongoDB collection and then redistributed to the drop-down card where the user can see their new quest, and edit/delete as they see fit, as you can see from this image:
![Screenshot of to-do form/cards](https://i.imgur.com/eTlw6gt.png)
* **Profile Page - Character Creation** - The 'Add Character' functionality allows the user to store their own characters/stats to be accessed easily and displayed neatly. I once more utilisted a Bootstrap card deck feature here that is populated with the information filled in from the HTML form. The Python function collects data from the form and stores it to be iterated over by the Jinja loop that fills out the cards, as can be seen in the following image:
![Screenshot of character cards](https://i.imgur.com/DmkO7O8.png)
* **Register/Login Pages** - These pages were designed intentionally simple to enable the user to access their profile as quickly as possible.
# Future Features 

With regards to the dataset used in the site from the D&D 5th Edition SRD, given the absolutely mammoth amount of data in the source documents, I used a curated subset of data aimed at fulfilling the goals of the assignment criteria. In the future, I aim to make this site a passion project and keep filling the database. 

Also in the future, I would like to add a public messageboard/forum application for the site, to move further into the field of social networking, with more in-depth user profiles.

# Technologies Used
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Werkzeug](https://pypi.org/project/Werkzeug/)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [PyMongo](https://api.mongodb.com/python/current/) 
- [Bootstrap](https://getbootstrap.com/)
- [Material Color Tool](https://material.io/resources/color/#!/?view.left=0&view.right=0)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

# Testing
## Code Validation & Known Errors
All HTML/CSS files for the site were formatted using [this free online formatter](https://www.freeformatter.com/html-formatter.html), then validated via [W3C Markup Validation Service](https://validator.w3.org/). The W3C check did spring some errors in the code but when checked through, they were all as a result of the bad functionality for validating Jinja Templating language, and any other errors were rectified.

The app.py Python file was checked and verified as completely PEP8 compliant, using [this checker](http://pep8online.com/checkresult):
![Python pep8 screenshot](https://i.imgur.com/wAYKNJsl.png)
## Browser Support and Functionality
The site was tested and working in several browsers; Google Chrome, Mozilla Firefox, Apple Safari and Microsoft Edge.

All site links, internal and external have been manually checked and tested thoroughly and no errors were found as a result of bad pathing.

## Responsive Design Testing
The site was extensively tested on a range of devices and screen-sizes, and was regularly tested during development, using Google Chrome DevTools. The range of responsive design can be seen in the prototype image at the top of this document but I will also include some screenshots from DevTools here from testing:
![Site on Phone display](https://i.imgur.com/9vjYgVDl.png)
![Site on Tablet display](https://i.imgur.com/FUH9cY7l.png)
![Login on Phone display](https://i.imgur.com/329ksSTl.png)

## Debugging
Extensive debugging was done throughout development of the site, mainly using Chrome DevTools to fix UI issues, and Werkzeug to debug issues with the Python/Flask code and routing.

# Deployment and Cloning

## Deployment
Dungeon Club is deployed on Heroku, using a free account. To set up my project for deployment on Heroku, I followed this process:
* Login to/create account on Heroku and navigate to 'Create New App' on the dashboard.
* Fill in the details for the new app, and select a server. 
* The environment variables for the project are entered on the app settings. These include the MONGO_URI, and SECRET_KEY.
* Navigate to the 'Deploy' section, and from that menu, link the existing GitHub repo master branch to the Heroku app and enable automatic deployment.

## Cloning this project
In order to clone this repository, to work on the code yourself, please follow these steps:
* On the GitHub main page of the repository, above the file-list click on the 'Code' button, with the download symbol.
* In the HTTPS tab, click the clipboard symbol to copy the clone URL.
* On your system, open your terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
* Press Enter to create your local clone.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

# Credits
## Content, Media and Credits
Much of the assets and content was provided via the [Dungeons and Dragons Fan Site Kit](https://dnd.wizards.com/articles/features/fan-site-kit), such as many of the banner images, and of course the data from the SRD Document was also courtesy of Wizards of the Coast LLC.

The sidebar menu for the 5th Edition Database page was inspired by/is a heavily customised version of [this brilliant code snippet on CodePly](https://www.codeply.com/go/3e0RAjccRO/bootstrap-4-collapsing-sidebar-menu) by Skelly.

Articles and images linked on Dungeon Club Homepage:
* https://allthingsdnd.com/amazon-prime-orders-2-seasons-for-critical-role-the-legend-of-vox-machine/
* https://io9.gizmodo.com/joe-manganiello-takes-the-internets-toughest-and-most-f-1845873249
* https://arstechnica.com/gaming/2020/12/dungeons-dragons-linked-to-new-movie-starring-chris-pine/

Some additional Google Image searching was required for the card images on the Resources page, however the majority was simply the image file hosted on the Amazon listing for the product.






