import pandas as pd


def and_perceptron(v1, v2):
    weight1 = 1.0
    weight2 = 1.0
    bias = -2.0
    linear_combination = weight1 * v1 + weight2 * v2 + bias
    output = int(linear_combination >= 0)

    return output


def or_perceptron(v1, v2):
    weight1 = 1.0
    weight2 = 1.0
    bias = -1.0
    linear_combination = weight1 * v1 + weight2 * v2 + bias
    output = int(linear_combination >= 0)
    
    return output


def not_perceptron(v):
    weight = -1.0
    bias = 0.0
    linear_combination = weight * v + bias
    output = int(linear_combination >= 0)

    return output


def xor_perceptron(v1, v2):
    # TODO: create an XOR perceptron
    # ( p AND NOT q )  OR     ( NOT p AND q )
    a = and_perceptron(v1,v2)
    b = or_perceptron(v1,v2)
    c = not_perceptron(a)
    linear_combination = and_perceptron(c, b)
    
    return linear_combination


if __name__ == "__main__":

    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [False, True, True, False]
    outputs = []

    for test_input, correct_output in zip(test_inputs, correct_outputs):
        output = xor_perceptron(test_input[0], test_input[1])
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1],
                        output, is_correct_string])
    num_wrong = len([output[3] for output in outputs if output[3] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=[
                                'Input 1', '  Input 2', '  Activation Output', '  Is Correct'])
    if not num_wrong:
        print('Nice!  You got it all correct.\n')
    else:
        print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))
