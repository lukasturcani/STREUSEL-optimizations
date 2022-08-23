import numpy as np
import timeit
import textwrap


def grad_magnitude_one(gx, gy, gz):
    grad_mag = gx
    for i in range(gx.shape[0]):
        for j in range(gy.shape[1]):
            for k in range(gz.shape[2]):
                grad_mag[i,j,k] = np.sqrt(gx[i,j,k]**2+gy[i,j,k]**2+gz[i,j,k]**2)

    return grad_mag


def grad_magnitude_two(gx, gy, gz):
    np.square(gx, out=gx)
    gx += np.square(gy)
    gx += np.square(gz)
    return np.sqrt(gx, out=gx)


generator = np.random.RandomState(10)
size = 150
gx_one = generator.randn(size, size, size)
gy_one = generator.randn(size, size, size)
gz_one = generator.randn(size, size, size)

gx_two = np.array(gx_one)
gy_two = np.array(gy_one)
gz_two = np.array(gz_one)

one_result = timeit.timeit(
    stmt="grad_magnitude_one(gx_one, gy_one, gz_one)",
    number=1,
    globals=globals(),
)
print(one_result)

two_result = timeit.timeit(
    stmt="grad_magnitude_two(gx_two, gy_two, gz_two)",
    number=1,
    globals=globals(),
)
print(two_result)

assert np.allclose(
    a=grad_magnitude_one(
        gx=np.array(gx_one),
        gy=np.array(gy_one),
        gz=np.array(gz_one),
    ),
    b=grad_magnitude_two(
        gx=np.array(gx_one),
        gy=np.array(gy_one),
        gz=np.array(gz_one),
    ),
    atol=1e-8,
)
