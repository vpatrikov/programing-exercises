def is_merge(s, part1, part2):
   merged_word = ''.join([a + b for a, b in zip(part1, part2)] + list(part1[len([part2]):] if len(part1) > len(part2) else part2[len(part1):]))
   
   return True if merged_word == s or part1 + part2 == s else False