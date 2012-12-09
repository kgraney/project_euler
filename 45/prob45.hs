import Data.List

triangle n = n*(n+1)/2
pentagonal n = n*(3*n-1)/2
hexagonal n = n*(2*n-1)

numbers = [1..]

t = [triangle x | x <- numbers]
p = [pentagonal x | x <- numbers]
h = [hexagonal x | x <- numbers]

i = intersect t p
i2 = intersect i h
