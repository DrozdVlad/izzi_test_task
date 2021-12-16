After downloading project you need install all requirements 
Write command in terminal - pip install -r requirements.txt

Then you need create super-user for get permission to admin cabinet. Use command in terminal - python
manage.py createsuperuser

Then you can runserver in terminal - python manage.py runserver And get admin cabinet and logining

- http://127.0.0.1:8000/admin/

For import user go to - http://127.0.0.1:8000/admin/izzi/user/ in your browser Press button "Import csv"

After get data users from file TestData.csv you can get list users in browsers - http://127.0.0.1:8000/izzi/users/
If you want get filtered users by registration date you need write in url date as on example

- http://127.0.0.1:8000/izzi/users/?date_of_registration=2018/05/09
