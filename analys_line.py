def LineAnalysis(line: str) -> bool:
  split_line = line.split("*")[1:-1]
  if split_line:
    return split_line.count(split_line[0]) == len(split_line)
  else:
    return True