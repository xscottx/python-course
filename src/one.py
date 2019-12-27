def func():
  print('func() in one.py')

# run first
print('top level in one.py')

if __name__ == '__main__':
  # run second
  print('one.py is being run directly!')
else:
  print('one.py has been imported!')