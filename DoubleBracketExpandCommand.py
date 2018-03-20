import sublime, sublime_plugin

class DoubleBracketExpandCommand(sublime_plugin.TextCommand):

	def run(self,edit):
		self.view.run_command('expand_selection',{"to": "brackets"})
		self.view.run_command('expand_selection',{"to": "brackets"})
		self.view.run_command('copy')
