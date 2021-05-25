from OneStream import OneStream
from MultiStream import MultiStream
if __name__ == '__main__':
    one = OneStream()
    one.print_results()
    one.get_partial_accuracy()

    mul = MultiStream()
    mul.print_results()
    mul.get_partial_accuracy()
