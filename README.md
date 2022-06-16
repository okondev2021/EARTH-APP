# CS50 WEB PROGRAMMING WITH PYTHON AND JAVASCRIPT CAPSTONE PROJECT
##### My web application was built with html, css, bootstrap, django and javascript.

## Project-5 Main Idea:

I created a donation web application, where there are two types of users.
1. Those looking for help (Donee)
2. Those providing the help (Donor)
Help seekers can raise request due to certain predicaments like flood, sickness with image as proof.The site admin will have to verify the request before before those providing donations can see it. Those providing donations have two options, either they donate finacially or materially. If the user chooses to donate finacially the amountdonated is sent to the receiver but if the donator chooses to give material item, the item is placed in the app's commerce site and when it is sold the amount is sent to the receiver .Please note that the main idea for this project is to build a donation platform the ecommerce site is only a plus to this very fine project.

## THE MAIN Page

Home Page:a small landing page containing basic information about the donation platform named Earth.
Login/Logout/Registeration Page:to register, login and logout users using this web app
404 Page:A Page not found template just in case a request isn't found the user will be redirected to the 404 page. The page also contains a link to the Dashboard(UserProfile Page)
UserProfile Page:For this donation app there are three types of user, the donor the receiver and the admin
1. The admin profile page contains a list of request if any made by the receiver and a button that take the admin to the authrequest page where the full detail of the receiver and the request is displayed and they can confirm the request if its meets the requirement for a proper request 
2. The donor profile page contains a list of request made by those looking for donation with a see more button, if clicked will direct the user RequestPage where it displays to the donor images, about the cause, the country of the receiver 
3. The receiver profile page displays instruction on how to make a request  if they haven't made any and if they have made a request the instruction is replaced with a button when clickd disply how much they have raised
RequestPage:displays to donors more detail on a request/cause if clicked on details like about the cause, images to backup and a button which says contribute if clicke bring up a modal built with bootstrap that asks if the user will like to donate/contribute finacially or materially. It also has a progressbar to show how much the donor has
Payement Page: If the donor decides to donate finacially they are taken to the payment page where they donate generously

### The ecomerce section was added to make this project more challenging since the app is a combination of a donation app and an ecommerce app

Donate material Page : If the donor decides to donate material item they are taken to donatematerial page where they create an item and when saved the item is added to the ecommerce site
The ecommerce page: Contains all the product that have donated 
The Product page: Shows product detail , amount and purchase button 
The Purchase page: Where the  user makes payment the payamount is given to the receiver whose request that item was created and is directed to the ecommerce site 

**auth.html is the template for my login and logout page**
**earthapplayout.html is the layout for my the donation part of my app it has a reponsive sidebar built with html css bootstrap and javascript**
**ecommerce_template.html is the layout for the commerce part of my app**
**layout1.html is the layout for my landing page**

## DISTICTIVENESS AND COMPLEXITY

This project is not similar to any other project either submitted as a final project or during the courese first the donation platform is different because it offers donor the choice of donating finacially or material item and is merged with an ecommerce site still in the same app and for the ecommerce site its not an auction site where buyers bid the items are bought by users of the app and every product is created to support a particular cause and when the product is bought the amount is given to the receiver whose cause was slected to donate the material item. In terms of complexity the app was created using djnango with more than one model, javascript ajax to make asynchronous request to the server and is mobile responsive as well

## Files information

**The views.py** 14 views handdling our web app including the login,logout,registration views
1:	index view- displays the landing page
2:	profile view- Show different thing based on the usertype if loggedin user is the admin it shows all the request yet to be confirmed, if loggedin user is a donor it displays all the confirmed request made by the donees if logged in user is a donee it displays their track(how much they have raised) 
3:	authrequest view- update the requeststatus so the request can be confirmed allowing donors to see the request
4:	requestpage view- for saving a request made by a donee
5:	donate_material view - saves material from users who which to donate material items 
6:	commerce view - displays all the product given by users who which to donate material items
7:	product view - displays more information on a particular product
8:	purchase view - allow users to pay for the item they want to buy and send the amount gotten to the right donee
9:	payment view - allows donator who choose to donate financially to donate and the money is sent to the right donee
10 	not_found view - displays a 404 page
11:	receiver - receiver using Userrequest id it gets the amount a donee has raised

**Models.py**: contains three models
a User model for the apps users
a Create model for the ecommerce 
a UserRequest model for donees making request

**My javascript files**
request.js redirects the user to either the Payment page or the donatematerial page
profile.js asynchronously make request to the server to get the amount the logged in donee has raised if he/she has made a request
index.js redirect the user to another page
earthapplayout.js contains the javascript code for the sidenavigation bar

**My template(html files)** have been discussed above

**My css files** contain all the css styles for the web app

**My Media Folder**: to store images uploaded bu users

**My urls.py** contain all the routes for my web app

### How to run the application

make and apply migrations bu running py manage.py makemigrations earth and py manage.py migrate

**Thank you.**
