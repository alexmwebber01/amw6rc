I started by trying to follow the instructions to set up a dex app, and got as far as using "make" to build the app, but was not able to run the OPENID Connect Provider or, run the OPENID app. For some reason, running the "make" command gave me an error when creating the bin folder: "make: *** [Makefile:26: bin/dex] Error 2". I searched online for a solution to this, but didn't really find much. I tried following some of the ideas in this thread, https://github.com/dexidp/dex/issues/1118, but no luck. I figured this was probably somehow due to me using windows, so I looked into running Ubuntu and trying it, but in the end I didn't have enough time to do this.

I also ran into an error when creating the Google SSO app. I followed the steps completely, and got my app to be created and accessible. But when trying to login, I get the error: "Error 401: invalid_client. The OAuth client was not found". I made sure my GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET were set correctly using echo, and even set them again and reset the key, but I still got the same error. I tried every possible solution in this thread https://console.developers.google.com/apis/credentials/oauthclient/1007870812878-d9ngct138eddnv2rq7fv50m6a3jgcpgh.apps.googleusercontent.com?project=swe-demo-app&supportedpurview=project, but again no luck. I was able to get the login to work by hard-coding the values for GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET in the app.py file (thanks to Jonah Marz for the solution). 

I hope by the end of the semester and I can fix these errors (probably by using Ubuntu), and have a functional application. 