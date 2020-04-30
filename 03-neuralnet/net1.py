from net import Net
net = Net()

x = net.variable(1)
y = net.variable(2)
o  = net.mul(x, y)

print('net.forward()=', net.forward())
print('net.backwward()')
net.backward()
print('x=', x, 'y=', y, 'o=', o)
print('gfx = x.g/o.g = ', x.g/o.g, 'gfy = y.g/o.g=', y.g/o.g)

net.gradient_descendent()