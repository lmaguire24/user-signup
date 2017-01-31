# #!/usr/bin/env python
# #
# # Copyright 2007 Google Inc.
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.
# #
#
import webapp2
import cgi

# # html boilerplate for the top of every page
# page_header = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>FlickList</title>
#     <style type="text/css">
#         .error {
#             color: red;
#         }
#     </style>
# </head>
# <body>
#     <h1>
#         <a href="/">FlickList</a>
#     </h1>
# """
#
# # html boilerplate for the bottom of every page
# page_footer = """
# </body>
# </html>
# """
#
#
# # a list of movies that nobody should be allowed to watch
# terrible_movies = [
#     "Gigli",
#     "Star Wars Episode 1: Attack of the Clones",
#     "Paul Blart: Mall Cop 2",
#     "Suicide Squad",
#     "Nine Lives"
# ]
#
#
# def getCurrentWatchlist():
#     """ Returns the user's current watchlist """
#
#     # for now, we are just pretending
#     return [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]
#
#
# class Index(webapp2.RequestHandler):
#     """ Handles requests coming in to '/' (the root of our site)
#         e.g. www.flicklist.com/
#     """
#
#     def get(self):
#
#         edit_header = "<h3>Edit My Watchlist</h3>"
#
#         # a form for adding new movies
#         add_form = """
#         <form action="/add" method="post">
#             <label>
#                 I want to add
#                 <input type="text" name="new-movie"/>
#                 to my watchlist.
#             </label>
#             <input type="submit" value="Add It"/>
#         </form>
#         """
#
#         # a form for crossing off movies
#         # (first we build a dropdown from the current watchlist items)
#         crossoff_options = ""
#         for movie in getCurrentWatchlist():
#             crossoff_options += '<option value="{0}">{0}</option>'.format(movie)
#
#         crossoff_form = """
#         <form action="/cross-off" method="post">
#             <label>
#                 I want to cross off
#                 <select name="crossed-off-movie"/>
#                     {0}
#                 </select>
#                 from my watchlist.
#             </label>
#             <input type="submit" value="Cross It Off"/>
#         </form>
#         """.format(crossoff_options)
#
#         # if we have an error, make a <p> to display it
#         error = self.request.get("error")
#         error_element = "<p class='error'>" + error + "</p>" if error else ""
#
#         # combine all the pieces to build the content of our response
#         main_content = edit_header + add_form + crossoff_form + error_element
#         content = page_header + main_content + page_footer
#         self.response.write(content)
#
#
# class AddMovie(webapp2.RequestHandler):
#     """ Handles requests coming in to '/add'
#         e.g. www.flicklist.com/add
#     """
#     def post(self):
#         # look inside the request to figure out what the user typed
#         new_movie = self.request.get("new-movie")
#
#         # TODO 2
#         # if the user typed nothing at all, redirect and yell at them
#         if (not new_movie) or (new_movie.strip() == ""):
#             error = "You didn't enter anything!".format(new_movie)
#             self.redirect("/?error=" + cgi.escpape(error, quote=True))
#
#
#         # TODO 3
#         # if the user wants to add a terrible movie, redirect and yell at them
#         if new_movie in terrible_movies:
#             error = "How can you even think about watching that movie?!?!".format(new_movie)
#             self.redirect("/?error=" + cgi.escape(error, quote=True))
#
#         # TODO 1
#         # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
#         escaped_movie = cgi.escape(new_movie)
#
#         # build response content
#         new_movie_element = "<strong>" + escaped_movie + "</strong>"
#         sentence = new_movie_element + " has been added to your Watchlist!"
#         content = page_header + "<p>" + sentence + "</p>" + page_footer
#         self.response.write(content)
#
#
# class CrossOffMovie(webapp2.RequestHandler):
#     """ Handles requests coming in to '/cross-off'
#         e.g. www.flicklist.com/cross-off
#     """
#
#     def post(self):
#         # look inside the request to figure out what the user typed
#         crossed_off_movie = self.request.get("crossed-off-movie")
#
#         if (crossed_off_movie in getCurrentWatchlist()) == False:
#             # the user tried to cross off a movie that isn't in their list,
#             # so we redirect back to the front page and yell at them
#
#             # make a helpful error message
#             error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)
#             error_escaped = cgi.escape(error, quote=True)
#
#             # redirect to homepage, and include error as a query parameter in the URL
#             self.redirect("/?error=" + error_escaped)
#
#         # if we didn't redirect by now, then all is well
#         crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
#         confirmation = crossed_off_movie_element + " has been crossed off your Watchlist."
#         content = page_header + "<p>" + confirmation + "</p>" + page_footer
#         self.response.write(content)
#
#
# app = webapp2.WSGIApplication([
#     ('/', Index),
#     ('/add', AddMovie),
#     ('/cross-off', CrossOffMovie)
# ], debug=True)
#
#


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

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', build_page())
], debug=True)
