def cal_state_of_health(present_capacity,RATED_CAPACITY=120):
   return 100*(present_capacity/RATED_CAPACITY)


def count_batteries_by_health(present_capacities):
  counts={"healthy": 0,"exchange": 0,"failed": 0}
  for present_capacity in present_capacities:
     state_of_health=cal_state_of_health(present_capacity,RATED_CAPACITY)
     if state_of_health > 88:
        counts["healthy"]+=1
     elif state_of_health >67:
        counts["exchange"]+=1
     else:
       counts["failed"]+=1
  return counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
