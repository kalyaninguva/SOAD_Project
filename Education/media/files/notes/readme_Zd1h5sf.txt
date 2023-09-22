
One test user in this app is:
	Username : nithish_277
	password : simple@123

Here service is to show available jobs : 

	--> In the Home page it welcomes the user with username and displays the details of the jobs.
	--> here posting a job can be done by any User.
	--> Any User can GET,POST,UPDATE,DELETE the jobs.

api link : "http://127.0.0.1:8000/api/jobs"--(Can be tested in Insomnia or django restframework)--(Here I've tested with Insomnia)

As there are authorization permissions:
	Token for users are needed to be generated
	
	Here for Test User :
		Token for nithish_277 : "bc1234192affe88d4c7bdce480c9c262464cb347"
		It can be obtained by running this command "python manage.py drf_create_token nithish_277"