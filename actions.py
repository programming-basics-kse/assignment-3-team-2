import medals as medals_action
import total as total_action
import overall as overall_action
import interactive as interactive_action

def medals(options):
    return medals_action.process(options)

def total(options):
    return total_action.process(options)

def overall(options):
    return overall_action.process(options)

def interactive(options):
    return interactive_action.process(options)
