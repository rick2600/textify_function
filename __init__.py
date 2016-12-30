from binaryninja import *


def textify_function(bv, function):
    output = ''    
    basic_blocks = sorted(function.basic_blocks, key=lambda bb: bb.start)
    
    for basic_block in basic_blocks:
        for inst in basic_block.get_disassembly_text():
            if str(inst.tokens[0]) == function.name: continue
            
            addr = hex(inst.address).replace("L", "")
            offset = inst.address - function.start
            output += "%s <%s+%d>:    %s\n" %\
            (addr, function.name, offset, str(inst))
            
    show_plain_text_report("Text Disasm", output)

# From @josh
def textify_function2(bv, function):
    output = ''
    output += bv.get_disassembly(function.start)
    while bv.get_basic_blocks_at(bv.next_address)[0].function.start == function.start:
        output += bv.get_next_disassembly() + "\n"
    show_plain_text_report("Text Disasm", output)

PluginCommand.register_for_function("Textify Function", "", textify_function)



