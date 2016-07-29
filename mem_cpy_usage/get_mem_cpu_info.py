#import psycopg2
import psutil

def get_cpu_info():
    return psutil.cpu_times_percent(percpu=False)


def get_mem_info():
    return psutil.virtual_memory()


def main():
    cpu_info = get_cpu_info()
    mem_info = get_mem_info()
    print(cpu_info)
    print(mem_info)
    

if __name__ == '__main__':
    main()

