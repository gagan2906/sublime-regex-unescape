import sublime
import sublime_plugin
import ast


class RegexEscapeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            # escaped_string = 'This is a backslash-escaped string: \n foo'
            substr = self.view.substr(sel)
            unescaped_string = ast.literal_eval(f'"{substr}"')
            self.view.replace(edit, sel, unescaped_string)
