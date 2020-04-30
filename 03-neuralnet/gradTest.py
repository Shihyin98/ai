import nn

def f(p):
    [x,y] = p
    return x*x + y*y

p = [1.0, 3.0]
print('grad(f,p) = ', nn.grad(f, p))

# nn.gradientDescendent(f, p)
