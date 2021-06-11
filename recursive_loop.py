def print_n_times(name,n):
    print(name,":",n)
    if n == 0:
        return
    print_n_times(name,n-1)

print_n_times("Monirith",10)