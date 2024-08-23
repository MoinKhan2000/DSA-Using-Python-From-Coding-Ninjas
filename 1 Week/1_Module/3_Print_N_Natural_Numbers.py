# def print_N_Natural_Numbers_Increasing_Order(n):
#     if n==0:
#         return;
#     else:
#         print_N_Natural_Numbers_Increasing_Order(n-1)
#         print(n, end=" ");
#         # return
# def print_N_Natural_Numbers_Decreasing_Order(n):
#     if n==0:
#         return;
#     else:
#         print_N_Natural_Numbers_Decreasing_Order(n-1)
#         print(n, end=" ");
#         # return    Working well
# num=int(input())
# print_N_Natural_Numbers_Increasing_Order(num)
# print()
# print_N_Natural_Numbers_Decreasing_Order(num)


def print_n_to_1(n):
    if n==0:
        return
    print(n)
    print_n_to_1(n-1);

print_n_to_1(5)