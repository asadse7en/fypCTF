# Django project to Host Catpure the Flag Events



---

## Diploy on Heroku

1. Create `runtime.txt` add you python version to this file ie. `python-x.xx.xx`
2. Add all the required packeges to `requirements.txt` with `pip freeze > requirements.txt`if on a virtual envirement
3. Create Procfile with no extension and add this `web: gunicorn projectname.wsgi --log-file -` change project name to yours.