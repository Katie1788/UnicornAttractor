# UnicornAttractor
Stream 3 project
This project was created using django in pycharm

I used existing files which had been created by following the insructions on code institute so create a unicorn attractor project, 
an accounts app, profile, register and login page, along with a products page and cart. I then created a new repository in github and added 
the project to it. 
There were some errors in the files at this stage, causing the display to be off when I viewed the app in my browser

I was also unable to open the admin panel, which was the result f having the following line of code in my 'settings' file 'accounts.backends.CaseInsensitiveAuth'. I removed this file which resolved the issue

Next I created a home page. I had already created an app called 'home' by following the code institute tutorial, and created a 'templates' folder into which I had created an 'index.html' file. I had also created a 'views.py' file.
Next, I added a 'urls.py' file to the app, and created a url for 'home'. I also added this to my list of urls under my 'ecommerce/urls.py' file. I then added a 'home' link to my list of links in my 'base.html' file, and lastly I added 'home' to my installed apps in 'settings.py'.   

