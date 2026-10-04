from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.12, 1)


class JMRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=24, spacing=16, **kwargs)

        self.add_widget(Label(
            text="JM 下载器",
            font_size="28sp",
            size_hint=(1, 0.2),
        ))

        self.input = TextInput(
            hint_text="输入本子 ID 或链接",
            multiline=False,
            font_size="18sp",
            size_hint=(1, 0.12),
        )
        self.add_widget(self.input)

        self.btn = Button(
            text="下载",
            font_size="20sp",
            size_hint=(1, 0.15),
        )
        self.btn.bind(on_release=self.on_download)
        self.add_widget(self.btn)

        self.log = Label(
            text="就绪",
            font_size="16sp",
            size_hint=(1, 0.4),
        )
        self.add_widget(self.log)

    def on_download(self, *_):
        text = self.input.text.strip()
        self.log.text = "收到：{}".format(text or "(空)")


class JMApp(App):
    title = "JM 下载器"

    def build(self):
        return JMRoot()


if __name__ == "__main__":
    JMApp().run()