#!/home/kalyb/Desktop/py/myscripts/virtualenvs/freefoodfinder/bin/python3.7
"""Find events on craigslist that offer free food.
"""

from craigslist import CraigslistEvents

def main():
    my_results = []
    cl_e = CraigslistEvents(site='kansascity', filters={'free': True, 'food': True})

    for result in cl_e.get_results(sort_by='newest', limit=5):
        my_results.append(result)

    for each_item in my_results:
        print(each_item)

if __name__ == '__main__':
    main()
