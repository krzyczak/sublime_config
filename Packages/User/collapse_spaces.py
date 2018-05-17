import sublime
import sublime_plugin
import re

class CollapseSpacesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = sublime.Region(0, self.view.size())
    txt = self.view.substr(region)
    new_txt = re.sub(r"([a-zA-Z|:])( {2,})", r"\1 ", txt)
    self.view.replace(edit, region, new_txt)

# class CollapseSpacesCommand(sublimeplugin.Plugin):
#     def onPreSave(self, view):
#         print view.fileName(), "is about to be saved"
