class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def count_atoms(formula: str) -> dict:
            stack = [defaultdict(int)]
            i = 0
            n = len(formula)
            
            while i < n:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    top = stack.pop()
                    i += 1
                    start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[start:i] or 1)
                    for atom, count in top.items():
                        stack[-1][atom] += count * multiplier
                else:
                    start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    atom = formula[start:i]
                    start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[start:i] or 1)
                    stack[-1][atom] += count
            
            return stack[-1]
        
        atom_count = count_atoms(formula)
        result = []
        for atom in sorted(atom_count.keys()):
            count = atom_count[atom]
            if count > 1:
                result.append(f"{atom}{count}")
            else:
                result.append(atom)
        return ''.join(result)