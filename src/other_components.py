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

class Decoder(Component):
    def __init__(self, input_size):
        num_outputs = 2 ** input_size
        inputs = {"in": input_size}
        outputs = {}
        for i in range(num_outputs):
            outputs[i] = 1
        Component.__init__(self, inputs, outputs)

    def update(self):
        input_val = self.input_state["in"]
        if input_val is None:
            for i in range(len(self.outputs)):
                self[i].set_value(None)
            return

        for i in range(len(self.outputs)):
            if input_val == i:
                self[i].set_value(1)
            else:
                self[i].set_value(0)

class Encoder(Component):
    def __init__(self, num_inputs):
        bits = len(bin(num_inputs - 1)) - 2
        inputs = {}
        for i in range(num_inputs):
            inputs[i] = 1
        outputs = {"out": bits}
        Component.__init__(self, inputs, outputs)

    def update(self):
        active_input = None
        for input_line, value in self.input_state.items():
            if value == 1:
                active_input = input_line
                break
        if active_input is None:
            self["out"].set_value(None)
        else:
            binary_representation = bin(active_input)[2:].zfill(len(self.outputs["out"]))
            self["out"].set_value(int(binary_representation))

