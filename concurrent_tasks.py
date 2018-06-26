#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue June 26th, 2018

@author: Frank Besson
"""

import concurrent.futures

# Task function converts a name string into an email address
def task_function(name):
	email = name + '@gmail.com'
	return email
	
# Run a task concurrently with a specified amont of threads
def concurrent_task(list_of_names, threads):

    list_of_emails = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        
        # Start the operations and mark each future with its task
        future_to_Collect = {executor.submit(task_function, name): name for name in list_of_names}

        # Receive results and create a stock info list
        for i, future in enumerate(concurrent.futures.as_completed(future_to_Collect)):
            ticker = future_to_Collect[future]
            try:
                data = future.result()
            except Exception as exc:
                print('error collecting data from future')
                pass
            else:
                try:
                    list_of_emails.append(data)
                except Exception as exc:
                    print('error appending email to list')
                    print(exc)
                    continue
                    
    return list_of_emails

list_of_names = ['Frank', 'Veronica', 'Earl', 'Chad', 'Megan']
list_of_emails = concurrent_task(list_of_names, 2)
print(list_of_emails)
