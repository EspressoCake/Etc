from immlib import *

class hooking(Break):
    def __init__(self):
        Break.__init__(self)
        self.imm = Debugger()

    def run(self, regs):
        self.imm.log("%08x" % regs['EIP'], regs['EIP'])
        self.imm.deleteBreakpoint(regs['EIP'])

def main(args):
    imm = Debugger()
    calc_Example = imm.getModule("calc.exe")
    imm.analyseCode(calc_Example.getCodebase())
    functions = imm.getAllFunctions(calc_Example.getCodebase())
    hooker = hooking()
    for function in functions:
        hooker.add("%08x" % function, function)
    return "%d functions." % len(functions)
