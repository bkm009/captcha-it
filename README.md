# captcha-it
Django Project that will provide service for captcha intergration on Webpage

### requirements
Django==2.1

djangorestframework==3.9.0

numpy==1.15.4

opencv-python==3.4.3.18

### License Mentions
License: OSI Approved (BSD) for numpy

License: BSD License (BSD) for Django

License: BSD License (BSD) for djangorestframework

License: MIT License (MIT) for opencv-python

### How to Use

run the project with command 

python manage.py runserver    # It will run server at localhost:8000

If you use on other ip or port, please update same in `captcha.js` file

To use it in your website, include one `div` tag as,

`<div id="captcha"></div>`

and include script file as `<script type="text/javascript" src="http://127.0.0.1:8000/static/js/captcha.js"></script>`


You will see captcha as, 

![alt ](https://github.com/bkm009/captcha-it/blob/master/Screenshot%20from%202019-10-02%2017-26-50.png)


Moreover, in `CaptchaGenerator.py` file, you can increse/decrease number of letters in captcha. :D


