from assertpy import assert_that


class main:

    def __init__(self):
        self.result = None

    # TEST1_____________________________________
    def array_sum(self, my_array):
        my_array = str(my_array)
        self.result = 0
        my_array = my_array.split(', ')
        for el in my_array:
            self.result = self.result + int(el)

    def check_array_sum(self, expected_result1):
        self.result = str(self.result)
        if self.result == expected_result1:
            result: bool = True
        else:
            result: bool = False
        assert_that(result, 'error message').is_true()

    # TEST2_____________________________________
    def greetings(self):
        dict2 = {'prop1': 'Hello,', 'prop2': ' World!'}
        dict1 = {'prop1': ' My name is,', 'prop2': ' Alex'}
        dict1['prop3'] = dict1.pop('prop1')
        dict1['prop4'] = dict1.pop('prop2')
        dict2.update(dict1)

        self.result = (''.join('{}'.format(v) for k, v in dict2.items()))

    def check_greetings(self, expected_result2):
        if self.result == expected_result2:
            result = True
        else:
            result = False
        assert_that(result, 'error message').is_true()

    # TEST3_____________________________________
    def math_operations(self, a: int, b: int, operation):
        self.result = 0
        if operation == '+':
            self.result = a + b
        elif operation == '-':
            self.result = a - b
        elif operation == '/':
            self.result = int(a / b)
        elif operation == '*':
            self.result = a * b
        else:
            print("wrong operation")

    def check_math_operations(self, expected_result3):
        #expected_result3 = int(expected_result3)
        self.result = str(self.result)
        if str(self.result) == expected_result3:
            result = True
        else:
            result = False
        assert_that(result, 'error message').is_true()

    # TEST4_____________________________________
    def hexadecimal(self):
        a = "830181000000E0010101C0"
        a_byte = bytearray.fromhex(a)
        six_bite = a_byte[6]
        six_bite -= 4
        a_byte[2] = six_bite
        self.result = a_byte.hex()

    def check_hexadecimal(self, expected_result4):
        if self.result == expected_result4:
            result = True
        else:
            result = False
        assert_that(result, 'error message').is_true()
