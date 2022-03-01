# Student_record_management_app
this application allows you to easily manage your students record and their fee record and provide inherent security of mysql


    ```requirement :
                python packages:
                
                    keyboard                   https://pypi.org/project/keyboard/ ,
                    mysql-connector-python    https://pypi.org/project/mysql-connector-python/ ```

we have included .exe compiled by  
    ```pyinstaller --onefile --console mainscreen.py  ```
tested on window 10 
to run it:
      MySQL shoul be installed and setup must be completed
      Then open mysq enter password
      Then type copy paste following statements .:
```
CREATE DATABASE IF NOT EXISTS new_rsj ;
USE new_rsj;
DROP TABLE IF EXISTS students;
CREATE TABLE students (
srno int PRIMARY KEY,
name varchar(15) ,
class enum('9','10','11','12') ,
sec enum('a','b','c','math','bio','art','comm') ,
fee_status enum('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec') DEFAULT 'apr',
extra_rupee int
);
```
here are some pics:
![image](https://user-images.githubusercontent.com/99308084/156081028-d207f288-d2e3-44d5-b31b-a2b2c7b5314e.png)

if password is wrong :
![image](https://user-images.githubusercontent.com/99308084/156081110-f4c13cec-b447-4fc1-b763-e1928df834b8.png)

and if correct:

![image](https://user-images.githubusercontent.com/99308084/156081138-fe547465-b923-4889-be04-f4d259a06e70.png)

now if key is "3" :
![image](https://user-images.githubusercontent.com/99308084/156081184-2b7338e3-3413-4db6-ad79-34c52c1e5c10.png)

if key was "1"  :
![image](https://user-images.githubusercontent.com/99308084/156081252-6bcc0588-5b38-445a-8c21-93c3bce3bbf3.png)

if key was "4" :
![image](https://user-images.githubusercontent.com/99308084/156081299-ed48d37a-cb92-4be6-a7e2-9844e0c265ea.png)

you also can have a game by pressing "7" at main screen:
![image](https://user-images.githubusercontent.com/99308084/156081374-16e5572f-9592-4dc0-9635-1a871ccf0a5c.png)

and much more!
