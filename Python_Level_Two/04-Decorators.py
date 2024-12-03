import time

def measure_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time =time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken to execute: {elapsed_time:.4f} seconds")
    return wrapper  
  
@measure_time
def slow_func():
    time.sleep(4) #pause for 4 seconds
    print("Function completed")
 
slow_func()   
    
# decorated_func = measure_time(slow_func)
# decorated_func()  
    