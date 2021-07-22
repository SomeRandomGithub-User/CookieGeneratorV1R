I'm trying to run this on Heroku.

SCRIPT BY: Egypt#2325

BOOST THE SERVER OR INVITE 10 PEOPLE TO GAIN EARLY ACCESS AND GET SHOUT OUTS IN ALL MY FUTURE SCRIPTS!

Steps by GiorgioBrux:
Fork the repo.
Go to https://dashboard.heroku.com/new?template=https://github.com/YOURUSERNAME/CookieGeneratorV1R making sure to change YOURUSERNAME in the url to your actual github username.
To update your fork, you can use the Fetch upstream button on github.
ℹ️ While directly using someone else's fork is possible, it is heavily discouraged for novice users because malicious code can be added and if one becomes very popular it will also be blacklisted by heroku.

After deployment, make sure you go to your app -> Configure dynos/Resources and turn off web and start worker.
You can then see logs by clicking on More (top right) and then View logs.
To update see here or just remove your app and recreate it.
