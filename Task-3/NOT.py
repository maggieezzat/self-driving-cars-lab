import pandas as pd

# TODO: Set weight and bias
weight = -1.0
bias = 0.0


# DON'T CHANGE ANYTHING BELOW
# Inputs and outputs
test_inputs = [(0), (1)]
correct_outputs = [True, False]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight * test_input + bias
    output = int(linear_combination >= 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input,
                    linear_combination, output, is_correct_string])

# Print output
num_wrong = len([output[3] for output in outputs if output[3] == 'No'])
output_frame = pd.DataFrame(outputs, columns=[
                            'Input 1', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))
