def main(*args):
  return sorted(args)
print (main(2,5,3,9,96))



if __name__ == '__main__':
  assert main(3, 2, 1, 49, 0) == [0, 1, 2, 3, 49], "Сортировка удалась"
  assert main(10, 20, 15, 9, 7) == [0, 1, 2, 3, 49], "Сортировка удалась"
  assert main(81, 4, 77, 86, 12) == [0, 1, 2, 3, 49], "Сортировка удалась"