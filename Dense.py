import numpy as np
import math

class Dense:

    def __init__(self, units, activation_func= ""):
        self.units = units
        self.size = units
        self.activation_type = activation_func # enum {relu,tanh, sigmoid, softmax, ...}

    def build(self, input_shape):
        random_values = np.random.normal(0, 1, size=input_shape*self.units) # Gaussian initialization
        self.w = random_values.reshape(input_shape, self.units)
        self.b = np.random.normal(0, 1, size=self.units).reshape(1, self.units)
        self.input_size = input_shape

    def call_act(self, inputs):
        return np.array(self.activation(np.matmul(inputs, self.w) + self.b)) # y=f(s)=h
    
    def call(self, inputs):
        return np.array(np.matmul(inputs, self.w) + self.b) # s
        
    def activation(self, input):

        if self.activation_type == "relu":
            return np.maximum(np.zeros(input.size), input)
        elif self.activation_type == "sigmoid":
            return self.vec_sigmoid()(input)
        elif self.activation_type == "softmax":
            return self.softmax(input)

    def activation_deriv(self, input):

        if self.activation_type == "relu":
            return np.ones(input.size)
        elif self.activation_type =="sigmoid":
            return self.vec_sigmoid_deriv()(input)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def sigmoid_deriv(self, x):
        return (1 / (1 + math.exp(-x)))*(1-(1 / (1 + math.exp(-x))))

    def vec_sigmoid(self):
        return np.vectorize(self.sigmoid)

    def vec_sigmoid_deriv(self):
        return np.vectorize(self.sigmoid_deriv)

    def softmax(self, x):                           # interesting overflow caused by exp
        x[x > 1e2] = 1e2
        a = np.array([np.exp(y) for y in x])
        return a/(np.matmul(np.ones(a.size), np.transpose(a)))


