import torch
from torch.utils import benchmark

typ = torch.float32
n = 1024 * 16
a = torch.randn(n, n).type(typ).cuda()
b = torch.randn(n, n).type(typ).cuda()
t = benchmark.Timer(stmt='a @ b', globals={'a': a, 'b': b})
x = t.timeit(10)
print("\nfloat32:")
print(x)

typ = torch.float16
n = 1024 * 16
a = torch.randn(n, n).type(typ).cuda()
b = torch.randn(n, n).type(typ).cuda()
t = benchmark.Timer(stmt='a @ b', globals={'a': a, 'b': b})
x = t.timeit(10)
print("\nfloat16:")
print(x)

typ = torch.bfloat16
n = 1024 * 16
a = torch.randn(n, n).type(typ).cuda()
b = torch.randn(n, n).type(typ).cuda()
t = benchmark.Timer(stmt='a @ b', globals={'a': a, 'b': b})
x = t.timeit(10)
print("\nbfloat16:")
print(x)