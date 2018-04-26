from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
import random, webbrowser
#from admob import Admob

__version__ = '1.2'
#ad_inst = Admob()


class HomeScreen(Screen):
    def info_popup(self):
        InfoPopup().open()


class NumberScreen(Screen):
    sn = NumericProperty(0)
    mn = NumericProperty(40)
    r = NumericProperty(0)

    def goto(self, snText, mnText):
        self.sn = snText
        self.mn = mnText
        self.r = random.randint(self.sn, self.mn)

        RandomNumberPopup().open()


class RandomNumberPopup(Popup):
    r = NumericProperty(0)

    def get(self):
        self.r = App.get_running_app().root.ids.random_app_screen_manager.get_screen("number_screen").r


class ClockScreen(Screen):
    r1t = NumericProperty(0)
    r2t = NumericProperty(24)
    r1m = NumericProperty(0)
    r2m = NumericProperty(60)

    rh = NumericProperty(0)
    rm = NumericProperty(0)

    def goto(self, r1tText, r2tText, r1mText, r2mText):
        self.r1t = r1tText
        self.r2t = r2tText
        self.r1m = r1mText
        self.r2m = r2mText

        self.rh = random.randint(self.r1t, self.r2t)
        self.rm = random.randint(self.r1m, self.r2m)

        RandomClockPopup().open()


class RandomClockPopup(Popup):
    rh = NumericProperty(0)
    rm = NumericProperty(0)

    def get(self):
        self.rh = App.get_running_app().root.ids.random_app_screen_manager.get_screen("clock_screen").rh
        self.rm = App.get_running_app().root.ids.random_app_screen_manager.get_screen("clock_screen").rm
        pass


class RatingScreen(Screen):
    person_1 = StringProperty('')
    person_2 = StringProperty('')
    person_3 = StringProperty('')
    person_4 = StringProperty('')
    person_5 = StringProperty('')
    person_6 = StringProperty('')

    def goto(self, person_1Text, person_2Text, person_3Text, person_4Text, person_5Text, person_6Text):
        self.person_1 = person_1Text
        self.person_2 = person_2Text
        self.person_3 = person_3Text
        self.person_4 = person_4Text
        self.person_5 = person_5Text
        self.person_6 = person_6Text

        RandomRatingPopup().open()


class RandomRatingPopup(Popup):
    r = NumericProperty()
    person_values = {}

    def get(self):
        r = random.randint(1, 6)
        print r
        person_values = {0: 'Error',
                         1: App.get_running_app().root.ids.random_app_screen_manager.get_screen(
                             "rating_screen").person_1,
                         2: App.get_running_app().root.ids.random_app_screen_manager.get_screen(
                             "rating_screen").person_2,
                         3: App.get_running_app().root.ids.random_app_screen_manager.get_screen(
                             "rating_screen").person_3,
                         4: App.get_running_app().root.ids.random_app_screen_manager.get_screen(
                             "rating_screen").person_4,
                         5: App.get_running_app().root.ids.random_app_screen_manager.get_screen(
                             "rating_screen").person_5,
                         6: App.get_running_app().root.ids.random_app_screen_manager.get_screen(
                             "rating_screen").person_6}
        self.r = r
        self.person_values = person_values


class InfoPopup(Popup):
    def open_url(self, url):
        webbrowser.open(url)


class RandomAppRoot(FloatLayout):
    pass


class RandomApp(App):

    def build(self):
        return RandomAppRoot()

    def on_pause(self):
        return True

    def on_resume(self):
        pass

'''
    def on_start(self):
        print 'random_run_test123987'
        AdBuddiz.setPublisherKey("4e2d2e75-a927-4bc0-b140-12a49672a131")  # replace the key with your app Key
        AdBuddiz.setTestModeActive()  # test mode will be active
        AdBuddiz.cacheAds(PythonActivity.mActivity)  # now we are caching the ads
'''


if __name__ == '__main__':
    RandomApp().run()
