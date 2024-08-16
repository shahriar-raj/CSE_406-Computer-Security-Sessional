import importlib

task_2 = importlib.import_module("1905105_task2_helper")

fi_t = [0,0,0]
se_t = [0,0,0]
th_t = [0,0,0]
count = 0
while count < 5:
    calculate_t = task_2.main(128)
    fi_t[0] += calculate_t[0]
    fi_t[1] += calculate_t[1]
    fi_t[2] += calculate_t[2]
    calculate_t = task_2.main(192)
    se_t[0] += calculate_t[0]
    se_t[1] += calculate_t[1]
    se_t[2] += calculate_t[2]   
    calculate_t = task_2.main(256)
    th_t[0] += calculate_t[0]
    th_t[1] += calculate_t[1]
    th_t[2] += calculate_t[2]
    count+=1

print("k \t\t\t\t\t\t Computation Time for")
print(" \t\t\t\t\t    A \t\t    B \t\t    R")
print(f"128 \t\t\t\t\t {fi_t[0]/5:.4f}ms \t {fi_t[1]/5:.4f}ms \t {fi_t[2]/5:.4f}ms")
print(f"192 \t\t\t\t\t {se_t[0]/5:.4f}ms \t {se_t[1]/5:.4f}ms \t {se_t[2]/5:.4f}ms")
print(f"256 \t\t\t\t\t {th_t[0]/5:.4f}ms \t {th_t[1]/5:.4f}ms \t {th_t[2]/5:.4f}ms")