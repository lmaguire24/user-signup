import webapp2
import cgi
import re

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
        .inputs {

            text-align: left;
        }
    </style>
</head>

"""

# html boilerplate for the bottom of every page
page_footer = """
</html>
"""


# a form for adding new username
form = """
<body>
    <h1>Signup</h1>
    <form method="post">
       <label>Username
            <input type="text" name="username" value="%(username)s"/>
            <span class="error"> %(username_error)s</span>
        </label>
<br>
        <label>Password
            <input type="password" name="password" value="%(password)s"/>
            <span class="error">%(password_error)s</span>
        </label>
<br>
        <label>Verify Password
            <input type="password" name="verify_password" value="%(verify_password)s"/>
            <span class="error">%(verify_error)s</span>
        </label>
<br>
        <label>Email (optional)
            <input type="text" name="email" value="%(email)s"/>
            <span class="error"> %(email_error)s</span>
        </label>
<br>
        <input type="submit" value="Submit"/>
    </form>
</body>
"""

class SignUpHandler(webapp2.RequestHandler):
    def write_form(self, username="", username_error="", password="", password_error="",
                   verify_password="", verify_error="", email="", email_error=""):
        values = {"username": username,
                  "username_error": username_error,
                  "password": password,
                  "password_error": password_error,
                  "verify_password": verify_password,
                  "verify_error": verify_error,
                  "email": email,
                  "email_error": email_error}

        response = page_header + form % values + page_footer
        self.response.write(response)

    #validation functions
    def validate_username(self, username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return USER_RE.match(username)

    def validate_password(self, password):
        USER = re.compile(r"^.{3,20}$")
        return USER.match(password)

    def validate_verify(self,verify_password):
        VERY = re.compile(r"^.{3,20}$")
        return VERY.match(verify_password)

    def validate_email(self, email):
        Email_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
        return Email_RE.match(email)





    def get(self):
        self.write_form()

    def post(self):

        have_error = False

        #username validation
        username = self.request.get("username")
        valid_username = self.validate_username(username)

        #password validation
        password = self.request.get("password")
        valid_password = self.validate_password(password)

        #verify validation
        verify_password = self.request.get("verify_password")
        valid_verify = self.validate_password(verify_password)

        #email validation
        email = self.request.get("email")
        valid_email = self.validate_email("email")

        if not valid_username:
            username_error = "That's not a valid username"
            have_error = True
            self.write_form(username=username, username_error=username_error)
            if not valid_password:
                password_error = "That's not a valid password"
                have_error = True
                self.write_form(password=password, password_error=password_error)
                if not valid_verify:
                    verify_error = "Those passwords do not match!"
                    have_error = True
                    self.write_form(verify_password=verify_password, verify_error=verify_error)
                    if not valid_email:
                        email_error = "That's not a real email address"
                        have_error = True
        if have_error == True:
            self.write_form(username=username, username_error=username_error,
                            password=password, password_error=password_error,
                            verify_password=verify_password, verify_error=verify_error,
                            email=email, email_error=email_error)

        # self.redirect('/welcome?username=%s' % password)
            # self.write_form(email=email, email_error=email_error)
        else:
            self.redirect('/welcome?username=%s' % username)



class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write('<h1>Welcome, %s!' % username)


app = webapp2.WSGIApplication([
    ('/', SignUpHandler),
    ('/welcome', WelcomeHandler)
], debug=True)

