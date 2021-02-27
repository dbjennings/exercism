class PhoneNumber:
    def __init__(self, number: str):
        self.number = self._format_number(number)
        self.area_code = self.number[:3]

        self._verify_number()

    def _format_number(self, number):
        return ''.join(d for d in number if d.isdigit()).lstrip('1')

    def _verify_number(self):
        if len(self.number)!=10: raise ValueError('Invalid #')
        if self.area_code[0]=='0': raise ValueError('Invalid Area Code')
        if self.number[3] in '01': raise ValueError('Invalide Exchange Code')

    def pretty(self):
        return '({})-{}-{}'.format(self.area_code,self.number[3:6],self.number[6:10])