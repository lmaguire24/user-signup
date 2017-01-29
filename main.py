#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

# # html boilerplate for the top of every page
# page_header =
# """<!DOCTYPE!>
# <html>
# <head>
#     <title>User Signup</title>
#     <style type="text/css">
#         .error {
#         color: red;
#         }
#     <style>
# </head>
# <body>
#     <h1>
#         <a href="/">Signup</a>
#     </h1>
# """"
#
# # html boilerplate for the bottom of every page
# page_footer = """
# </body>
# </html>
# """


def build_page(textarea_content):
    user_label = "<label> Username:</label>"
    user_input = "<input type='text' name='user'/>"

    password_label = "<label>Password:</label>"
    password_input = "<input type='text' name='password' />"

    verify_label = "<label>Verify Password</label>"
    verify_input  = "<input type='text' name='verify' />"

    email_label = "<label>Email (optional)</lanel>"
    email_verify = "<input type='text' name='email' />"

    submit = "<input type='submit' />"

    header = "<h2>Signup</h2>"

    form = ("<form method='post'>" +
            user_label + user_input + "<br>" +
            password_label + password_input + "<br>" +
            verify_label + verify_input + "<br>" +
            email_label + email_verify + "<br>" +
            submit + "</form>")

    return header + form

# class Index(webapp2.RequestHandler):
#     """ Handles requests coming in to '/' (the root of our site)
#         e.g. www.flicklist.com/
#     """
#
#     def get(self):
#

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
