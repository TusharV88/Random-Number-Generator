# Generate random number

def rng(m=2**32, a=1103515245, c=12345): 
    rng.current = (a*rng.current + c) % m 
    return rng.current/m 
 
# setting the seed 
rng.current = 1

n_iter = 100
scale = 10   
center = 1
for i in range(n_iter): 
    pseudo_random = rng()*scale + center 
    print('Iteration {} gives the following {}'.format(i, pseudo_random))

