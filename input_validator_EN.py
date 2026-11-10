def valid_int_input(prompt=""):
    while True:
        try:
            return int(input(prompt).strip().lower())
        except ValueError:
            print("Please choose an integer or alternative.")

def valid_float_input(prompt=""):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please choose a number.")

def valid_int_string_input(prompt="", allowed_strings=[]):
    while True:
        in_put = input(prompt).strip().lower()

        if in_put in [s.lower() for s in allowed_strings]:
            return in_put
        try:
            return int(in_put)
        except ValueError:
            print("Please choose an alternative.")

def valid_alternative_input(prompt="", allowed_inputs=[]):
    while True:
        in_put = input(prompt).strip().lower()

        if in_put in [str(s).lower() for s in allowed_inputs]:
            try:
                return int(in_put)
            except ValueError:
                pass

            try:
                return float(in_put)
            except ValueError:
                return in_put
        else:
            print("Please choose an alternative.")