from basic_parts import *

class Mux(Component):
	def __init__(self, num_inputs, input_size):
		bits = len(bin(num_inputs - 1)) - 2
		inputs = {"sel" : bits}
		outputs = {"out" : input_size}
		for i in range(num_inputs):
			inputs[i] = input_size
		Component.__init__(self, inputs, outputs)

	def update(self):
		sel = self.input_state["sel"]
		if sel == None:
			self["out"].set_value(None)
			return

		self["out"].set_value(self.input_state[sel])

class Demux(Component):
	def __init__(self, num_outputs, output_size):
		bits = len(bin(num_outputs - 1)) - 2
		inputs = {"sel" : bits, "in" : output_size}
		outputs = {}
		for i in range(num_outputs):
			outputs[i] = output_size
		Component.__init__(self, inputs, outputs)

	def update(self):
		sel = self.input_state["sel"]
		if sel is None:
			self["out"].set_value(None)
			return

		self[sel].set_value(self.input_state["in"])

class Splitter64Bit(Component):
	def __init__(self):
		Component.__init__(self, {"in" : 64}, {"lsb" : 32, "msb" : 32})

	def update(self):
		lsb = self.input_state["in"] & 0xffffffff
		msb = self.input_state["in"] >> 32
		self["lsb"].set_value(lsb)
		self["msb"].set_value(msb)

class Splitter8Bit(Component):
	def __init__(self):
		Component.__init__(self, {"in" : 8}, {0 : 1, 1 : 1, 2 : 1, 3 : 1, 4 : 1, 5 : 1, 6 : 1, 7 : 1})

	def update(self):
		for i in range(8):
			if self.input_state["in"] is not None:
				self[i].set_value((self.input_state["in"] >> i) & 1)
			else:
				self[i].set_value(None)

#class Decoder(Component):
#	def __init__(self):
#		inputs = { "A" : 1, "B" : 1}
#		outputs = { "C" : 1, "D" : 1, "E" : 1, "F" : 1}
#		Component.__init__(self, inputs, outputs)
#
#	def update(self):
#		if self.input_state["A"] == None and self.input_state["B"] == None:
#			self["C"].set_value(1) #This may not work, need to check the syntax of the component class
#		else:
#			result = self.input_state["A"] + self.input_state["B"] + self.input_state["Ci"]
#		self["S"].set_value(result)

class Decoder(Component):
    def __init__(self, num_outputs):
        bits = len(bin(num_outputs - 1)) - 2
        inputs = {"in" : bits}
        outputs = {}
        for i in range(num_outputs):
            outputs[i] = 1
        Component.__init__(self, inputs, outputs)

    def update(self):
        input_value = self.input_state["in"]
        if input_value is None:
            for i in range(len(self.outputs)):
                self[i].set_value(None)
        else:
            for i in range(len(self.outputs)):
                self[i].set_value(1 if i == input_value else 0)
