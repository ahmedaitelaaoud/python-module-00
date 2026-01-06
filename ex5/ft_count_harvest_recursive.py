def ft_count_harvest_recursive(current_day=1, N=None):
    if N is None:
        N = int(input("Days until harvest: "))
    if current_day > N:
        print("Harvest time!")
        return
    print("Day", current_day)
    ft_count_harvest_recursive(current_day + 1, N)
