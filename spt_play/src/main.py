from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input

class spt_play(App):
 
    BINDINGS=[("q", "quit", "Quit"),("d", "toggle_dark_mode" , "Toggle Dark Mode")]
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder="Search")
    def action_toggle_dark_mode(self) -> None:
        self.dark = not self.dark
    def action_quit(self) -> None:
        quit()
    if Input.Submitted == False:
        quit()
if __name__=="main":
  app = spt_play()
  app.run()
