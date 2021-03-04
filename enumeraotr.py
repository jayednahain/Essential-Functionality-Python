import numpy as np


z = np.arange(36)


z_shaped=z.reshape(6,6)

print(z_shaped)

#enumerate(itarable,start)
"'the enumerate method adds cunstom counter to an iterable andreturn it'"

for i, row in enumerate(z_shaped):
    print("row ",i,"is ",row)
