from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from decimal import Decimal

Builder.load_string('''

<TokenAmountDialog@Popup>
    id: popup
    unit: ''
    title: _('Token Amount')
    AnchorLayout:
        anchor_x: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.9, 1
            Widget:
                size_hint: 1, 0.2
            BoxLayout:
                size_hint: 1, None
                height: '80dp'
                Button:
                    id: tamount
                    background_color: 0, 0, 0, 0
                    text: kb.amount + ' ' + root.unit
                    color: 1, 1, 1, 1
                    halign: 'right'
                    size_hint: 1, None
                    font_size: '20dp'
                    height: '48dp'
            Widget:
                size_hint: 1, 0.2
            GridLayout:
                id: kb
                amount: ''
                size_hint: 1, None
                update_amount: popup.update_amount
                height: '300dp'
                cols: 3
                KButton:
                    text: '1'
                KButton:
                    text: '2'
                KButton:
                    text: '3'
                KButton:
                    text: '4'
                KButton:
                    text: '5'
                KButton:
                    text: '6'
                KButton:
                    text: '7'
                KButton:
                    text: '8'
                KButton:
                    text: '9'
                KButton:
                    text: '.'
                KButton:
                    text: '0'
                KButton:
                    text: '<'
                Widget:
                    size_hint: 1, None
                    height: '48dp'
                Button:
                    id: but_max
                    opacity: 1 if root.show_max else 0
                    disabled: not root.show_max
                    size_hint: 1, None
                    height: '48dp'
                    text: 'Max'
                    on_release:
                        kb.is_fiat = False
                        kb.amount = kb.max_amount
                Button:
                    size_hint: 1, None
                    height: '48dp'
                    text: 'Clear'
                    on_release:
                        kb.amount = ''
            Widget:
                size_hint: 1, 0.2
            BoxLayout:
                size_hint: 1, None
                height: '48dp'
                Widget:
                    size_hint: 1, None
                    height: '48dp'
                Button:
                    size_hint: 1, None
                    height: '48dp'
                    text: _('OK')
                    on_release:
                        root.callback(tamount.text if kb.amount else '')
                        popup.dismiss()
''')

from kivy.properties import BooleanProperty

class TokenAmountDialog(Factory.Popup):
    show_max = BooleanProperty(False)
    def __init__(self, show_max, amount, unit, max_amount, cb):
        Factory.Popup.__init__(self)
        self.show_max = show_max
        self.callback = cb
        self.unit = unit
        self.ids.kb.max_amount = max_amount
        if amount:
            self.ids.kb.amount = amount

    def update_amount(self, c):
        kb = self.ids.kb
        amount = kb.amount
        if c == '<':
            amount = amount[:-1]
        elif c == '.' and amount in ['0', '']:
            amount = '0.'
        elif amount == '0':
            amount = c
        else:
            try:
                Decimal(amount+c)
                amount += c
            except:
                pass
        kb.amount = amount
