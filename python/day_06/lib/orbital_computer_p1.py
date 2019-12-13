#! /usr/bin/env python3

class OrbitalComputer:
    def __init__(self, orbits = [[],[]]):   # Hint: Orbits are a list of lists
        self.orbits = orbits

    def orbit_count(self):      # Count all of the Orbitals children
        count = 0
        for v in self.orbital_map().values():
            count += len(v)     # Tally the amount of orbits

        return count

    def orbital_map(self):  # Map out All Orbitals and their children
        o_map = {}

        for path in self.orbits:        # For each Orbital path
            for p in path:              # For each Orbital and Child
                if p not in o_map: 
                    o_map[p] = self.orbital_children(p) # Set Orbital with orbital children

        return o_map

    def orbital_children(self,parent):  # Find Children of Orbital
        children = set([])              # Set avoids Duplicates
        for path in self.orbits:        # For each Orbital path
            if path[0] == parent:       # Find Chilren or Orbial
                children.add(path[1])   # Add child
                children.update(self.orbital_children(path[1])) # Look for children of the child
        return children