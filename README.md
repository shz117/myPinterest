myPinterest
===========

pinterest like web app

Sign in page

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/login.png)

Sign up page

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/signup.png)

User home page: all boards, follow streams and friends

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/userpage.png)

User profile page: public page also for settings and friend request

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/userprofile.png)

Search pictures by tag, key words; search user by name; search follow stream by keywords; recommendations (feeling lucky!)
![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/search.png)

Recommendations
![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/recommend.png)

Search results

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/searchresult.png)

Board page: all pins in it. Owner can delete board here; visitor can follow board here

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/boardpage.png)

Create new pin: from local file OR from web url

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/newpin.png)

Pin page: display image, providing reference to source page if provided. Display like numbers, discriptions and comments.

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/pinpage_picture_tags_description_likes.png)

User can: like/unlike picture; add tags(pin owner only); add comments; delete pin(owner only)

![myPinterest Screenshot](https://raw.github.com/shz117/myPinterest/master/pinpage_comments.png)

Use:

1. install python and django
2. configure db(mySQL in this project) according to settings.py 
3. cd /dir/you/want/put/it 
4. git clone https://github.com/shz117/myPinterest.git
5. cd /manage.py/dir
6. python manage.py runserver
7. access by http://localhost:8000/
8. Have fun! :-)

A few thoughts:
1. data models live in different Django Apps, if we deploy them to different server instance, any pass data object around when joining, is that kind of sharding?
