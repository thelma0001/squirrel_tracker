# squirrel_tracker
1. What has been implemented:  
  We have created two apps, naming 'sightings' and 'map', there are three specific functions in 'sightings' app:  
(1) 'add', adding a new squirrel sighting to the current database, including all attributes of a specific squirrel;  
(2) 'update', updating the new information about the existing sightings on several given attributes;
(3) 'stats', showing some basic statistical information of the squirrel data. 
  Then 'map' app shows exactly where the first 100 sightings in the database are on the map (and the showing sightings can be changed as wanted).  
  We render the webpages with Bootstrap and realize the management commands, to import the original csv data and export it (run the command "python manage.py import_squirrel_data 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv" to import the original data, and run the command "python manage.py export_squirrel_data file_name.csv" to export the data).  
  The development of webpages are under the framework of Django. All the migrations have been made and run the command "python manage.py runserver" to see the webpages.
  
2. Group Name and Section:  
  Yimen & Qi, Section 1

3. A list containing the UNI for each member on the team:  
  [qs2226, yl4561]  
