I'm trying to run this on Heroku.

SCRIPT BY: Egypt#2325

BOOST THE SERVER OR INVITE 10 PEOPLE TO GAIN EARLY ACCESS AND GET SHOUT OUTS IN ALL MY FUTURE SCRIPTS!

Steps by GiorgioBrux:
Go to https://dashboard.heroku.com/new?template=https://github.com/SomeRandomGithub-User/CookieGeneratorV1R

After deployment, make sure you go to your app -> Configure dynos/Resources and turn off web and start worker.
You can then see logs by clicking on More (top right) and then View logs.
To update see here or just remove your app and recreate it.
