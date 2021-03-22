from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Connects kv style files to the main.py file
Builder.load_file('mainView.kv')


class CameraScreen(Screen):
    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen(Screen):
    pass


class VideoStreamScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        self.title = 'End Street Harassment'
        # TODO: Create app icon
        # self.icon = 'filepath/customIcon.png'
        return RootWidget()


MainApp().run()
