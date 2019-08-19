from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random
import string


class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='site name:'))
        self.sitename = TextInput(multiline=False)
        self.add_widget(self.sitename)
        self.add_widget(Label(text='4 digit passkey:'))
        self.passkey = TextInput(multiline=False, password=True)
        self.add_widget(self.passkey)
        self.password_label = Label(text='Site Password is:')
        self.add_widget(self.password_label)
        self.password = Label()
        self.add_widget(self.password)
        self.genpass = Button(text='Get Password!')
        self.genpass.bind(on_press=self.get_pass)
        self.add_widget(self.genpass)
        self.clearpass = Button(text='Clear Password!')
        self.clearpass.bind(on_press=self.clear_pass) 
        self.add_widget(self.clearpass)
   
    def get_pass(self, instance):
        sitename = self.sitename.text
        passKey = self.passkey.text
        k = sitename.lower().encode('utf-8')
        j = sum(bytearray(k))
        random.seed(passKey*j)
        length = 14
        chars = string.ascii_letters + string.digits
        self.password.text = ''.join(random.choice(chars) for i in range(length)) + random.choice('!@#$%^&*')
        # return self.password
           
    def clear_pass(self, instance):
        self.password.text = ""


class TheApp(App):
    def build(self):
        return MainPage()


if __name__ == "__main__":
    TheApp().run()
