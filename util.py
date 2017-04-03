import datetime

# Constants
MILLIONS = 1e6
KILOS = 1e3
TICKS_PER_SECOND = 40

# Formats a cost such as 1500 -> 1.5K
def cost_with_units(num):
    if num >= MILLIONS:
        return '{0:g}M'.format(num/MILLIONS)
    elif num >= KILOS:
        return '{0:g}K'.format(num/KILOS)
    else:
        return '{0:g}'.format(num)

def ticks_as_seconds(ticks):
    return ticks/TICKS_PER_SECOND

# Formats a time such as 3620 -> 1h20s
def seconds_with_units(secs):
    if secs < 1: return "0s"
    td = datetime.timedelta(seconds=secs)
    # Downcast to int to round to floor
    w, d, h, m, s = int(td.days/7), int((td.days/7)%7), int(td.seconds/3600), int((td.seconds/60)%60), int(td.seconds%60)
    # Time categories should be hidden if spurious
    str = ''
    if w >= 1: str += '{0:g}w'.format(w)
    if d >= 1: str += '{0:g}d'.format(d)
    if h >= 1: str += '{0:g}h'.format(h)
    if m >= 1: str += '{0:g}m'.format(m)
    if s >= 1: str += '{0:g}s'.format(s)
    return str

def ticks_with_units(ticks):
    return seconds_with_units(ticks_as_seconds(ticks))

def ticks_with_units_clarified(ticks):
    return "{1} ({0})".format(ticks_with_units(ticks), str(ticks))
