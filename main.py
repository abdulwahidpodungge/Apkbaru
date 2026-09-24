from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class KalkulatorApp(App):
    def build(self):
        # Layout utama (Vertikal)
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Layar Tampilan Angka
        self.solution = TextInput(
            multiline=False, 
            readonly=True, 
            halign='right', 
            font_size=40,
            input_filter='float'
        )
        main_layout.add_widget(self.solution)

        # Susunan Tombol Kalkulator
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]

        # Grid untuk Tombol (4 Kolom)
        grid = GridLayout(cols=4, spacing=5)

        for row in buttons:
            for label in row:
                if label == '':
                    grid.add_widget(BoxLayout()) # Spacer kosong
                    continue
                
                button = Button(
                    text=label,
                    font_size=24,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5}
                )
                button.bind(on_press=self.on_button_press)
                grid.add_widget(button)

        main_layout.add_widget(grid)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            # Hapus layar
            self.solution.text = ''
        elif button_text == '=':
            # Hitung hasil matematika
            try:
                self.solution.text = str(eval(self.solution.text))
            except Exception:
                self.solution.text = 'Error'
        else:
            # Cegah input jika layar berisi teks 'Error'
            if current == 'Error':
                current = ''
            self.solution.text = current + button_text

if __name__ == '__main__':
    KalkulatorApp().run()
