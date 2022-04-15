import itertools
import numpy as np
import random
import time
import math


class Net(object):
    def __init__(self):
        self.time_step = 0

        self.num_inputs = 198
        self.num_hidden_units = 40
        self.num_output_units = 2
        self.cycles = 100
        self.learning_rate = 0.1
        self.discount_rate = 0.9
        self.l = 0.7

        self.features = [
            [np.random.randn() for x in range(self.num_inputs)]
            for y in range(self.cycles)
        ]
        self.hidden_layer = [np.random.randn() for x in range(self.num_hidden_units)]
        self.output_layer = [np.random.randn() for x in range(self.num_output_units)]
        self.input_weights = [
            [np.random.randn() for x in range(self.num_hidden_units)]
            for y in range(self.num_inputs)
        ]
        self.hidden_weights = [
            [np.random.randn() for x in range(self.num_output_units)]
            for y in range(self.num_hidden_units)
        ]


        self.old_output = [0 for x in range(self.num_output_units)]
        self.input_eligibility_trace = [
            [
                [0 for x in range(self.num_output_units)]
                for y in range(self.num_hidden_units)
            ]
            for z in range(self.num_inputs)
        ]
        self.hidden_eligibility_trace = [
            [0 for x in range(self.num_output_units)]
            for y in range(self.num_hidden_units)
        ]
        self.reward = [[0 for x in range(self.num_output_units)] for y in range(self.cycles)]
        self.error = [0 for x in range(self.num_output_units)]

    def sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def getValue(self, features):
        out = [np.random.randn() for x in range(self.num_output_units)]
        h_l = [np.random.randn() for x in range(self.num_hidden_units)]
        i_w = [
            [np.random.randn() for x in range(self.num_hidden_units)]
            for y in range(self.num_inputs)
        ]
        h_w = [
            [np.random.randn() for x in range(self.num_output_units)]
            for y in range(self.num_hidden_units)
        ]
        for j in range(0, 40):
            for i in range(0, 198):
                h_l[j] += features[i] * self.input_weights[i][j]
                h_l[j] = self.sigmoid(h_l[j])

        for k in range(0, 2):
            out[k] = h_l[j] * self.hidden_weights[j][k]
            out[k] = self.sigmoid(out[k])
        return out

    def feedforward(self, features):
        for j in range(0, 40):
            for i in range(0, 198):
                self.hidden_layer[j] += features[i] * self.input_weights[i][j]
                self.hidden_layer[j] = self.sigmoid(self.hidden_layer[j])
        for k in range(0, 2):
            self.output_layer[k] = self.hidden_layer[j] * self.hidden_weights[j][k]
            self.output_layer[k] = self.sigmoid(self.output_layer[k])
        self.time_step += 1

    def do_td(self, features, out, error):
        gradient = []
        for k in range(0, 2):
            gradient.append(out[k] * (1 - out[k]))

        for j in range(0, self.num_hidden_units):
            for k in range(0, 2):
                self.hidden_eligibility_trace[j][k] = (
                    self.l * self.hidden_eligibility_trace[j][k]
                    + gradient[k] * self.hidden_layer[j]
                )
                for i in range(0, 198):
                    self.input_eligibility_trace[i][j][k] = (
                        self.l * self.input_eligibility_trace[i][j][k]
                        + gradient[k]
                        * self.hidden_weights[j][k]
                        * self.hidden_layer[j]
                        * (1 - self.hidden_layer[j])
                        * features[i]
                    )
        for k in range(0, 2):
            for j in range(0, 40):
                self.hidden_weights[j][k] += (
                    self.learning_rate * error * self.hidden_eligibility_trace[j][k]
                )
                for i in range(0, 198):
                    self.input_weights[i][j] += (
                        self.learning_rate
                        * error
                        * self.input_eligibility_trace[i][j][k]
                    )
