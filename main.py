# Copyright 2016 Google Inc.
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

import webapp2

<<<<<<< HEAD
=======
class WeatherPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		s = open('empty-profile-form.html', 'r')
       	 	self.response.write(s.read())
>>>>>>> 557514507f3620193f5383c100c2e2ca0565dbf1

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
<<<<<<< HEAD
        self.response.write('Hello World')

class CustomPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<a href="http://www.google.com/">Google</a>')

class ManyDogPage(webapp2.RequestHandler):
	def get(self, number):
		self.response.headers['Content-Type'] = 'text/plain'
		#self.response.write('Woof, woof, woof!\n' * int(number))
		L = [];
		for i in range(1, int(number) + 1):
			L.append('{}: Woof, woof, woof!'.format(i))
		s = '\n'.join(L)
		self.response.write(s)
class DogPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Woof, woof, woof!')

class weather(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		#import codecs
		#f=codecs.open("/254application/index.html", 'r')
		#print f.read()
		import webbrowser
		f = open('/254application/index.html', 'w')

		print f.read()

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/254', CustomPage),
    ('/dog', DogPage),
    ('/dog/(\d+)', ManyDogPage),
    ('/weather', weather),
=======
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
	('/weather',WeatherPage)
>>>>>>> 557514507f3620193f5383c100c2e2ca0565dbf1
], debug=True)
