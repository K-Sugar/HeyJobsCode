import plotext.plot as plx
import numpy as np
from datetime import datetime

test_time = datetime.now()
test_time = test_time.strftime('%H:%M')
print(test_time)

hour = int(test_time[:2])
print(hour)


y=[250, 123, 234, 457]
plx.scatter(y, line=True, point_marker='X', line_marker='.', line_color='red', point_color='red', spacing=15)
plx.show()
