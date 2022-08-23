# The code

```python
for i in tqdm(range(ngs[0] - 1)):
    for j in range(ngs[1] - 1):
        for k in range(ngs[2] - 1):
            if np.absolute(efield[i,j,k] - efield[i+1, j+1, k+1]) <= cv:
                # if efield[i,j,k] - efield[i + 1, j + 1, k + 1] <= cv:
                vacuum.append(efield[i,j,k])
                v += 1
            else:
                non_vacuum.append(efield[i,j,k])
                nvac_ijk.append([i, j, k])
                n += 1
            if (n+v) == 1:
                surface.append(efield[i,j,k])
                surf_ijk.append([i, j, k])
                sarea += mk
            elif v == 2 or n == 2:
                v = 0
                n = 0
```



---

# First `if` condition

```python

if np.absolute(efield[i,j,k] - efield[i+1, j+1, k+1]) <= cv:

```

* `efield` contains the total magnitude of the gradient of the electric field at each voxel.
* Go through every index, `efield[i, j, k]` and compare to `efield[i+1, j+1, k+1]`. Check if difference between these values is smaller than `cv`. This implies the electric field is at vacuum level, because the change in gradient is sufficiently small.
* Note that the last index of `efield[i, j, k]` is not compared to anything, but we *could*, in theory compare it to 0 so that we do not reduce the shape of the `efield` matrix.

---

# First `if` condition

Can can do this comparison element wise

```python
import numpy as np
a = np.arange(49)
a.resize((7, 7))
print('array a\n', a, end='\n\n')

# We can do a view of only some of the data
view_a = a[:-1, :-1]
print('view_a\n', view_a, end='\n\n')

# And a second view that is has the shifted view of the data
view_b = a[1:, 1:]
print('view_b\n', view_b, end='\n\n')
```
