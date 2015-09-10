
<b>Introduction </b> </br>
CHMS stands for comprehensive hospital management system and  </br>
is developed as an exercise for IUST System Design And Analysis Course </br>


<b>Quick Setup </b>

<b>Prerequisites</b>:  
all requirements are listed in the requirements.txt . </br>
just run the following command on console :</br>
        pip install -r /path/to/requirements.txt </br>

<b>Database Creation</b> : </br>
you can whether use django’s default  Sqlite or MySQl . The desired database can be set easily in CHMS/settings.py </br>
at  “DATABASES” part by using using one of the setting provided there . </br>
Note that currently , settings for the Sqlite database is commented out and so the MySql database is used as the default </br> database. However you can change it to your desired way by commenting out each one of them.</br>

In Case of Sqlite: </br>
        Python manage.py syncdb</br>
In Case of MySQL:</br>
        Python manage.py migrate</br>
        Python manage.py createsuperuser</br>

<b>Finally Run The Server:</b></br>
        Python manage.py runserver</br>
