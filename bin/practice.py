import web

urls= ('/', 'practice')

app=web.application(urls, globals())

render = web.template.render('templates/')

class practice(object):
	def GET(self):
		message = "Welcome to this webpage, how can I help you?" 
		return render.yo(hello = message) 
		
if __name__== "__main__":
	app.run()
	
	