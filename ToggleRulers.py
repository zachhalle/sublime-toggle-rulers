import sublime, sublime_plugin

class ToggleRulersCommand(sublime_plugin.TextCommand):
	def run(self, edit, **kwargs):
		if self.view.settings().get("rulers") == []:
			rulers = kwargs["rulers"]
		else: 
			rulers = []
		self.view.settings().set("rulers", rulers)
