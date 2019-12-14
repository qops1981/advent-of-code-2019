#! /usr/bin/env python3

class OrbitalComputer:
    def __init__(self, orbits = [[],[]]):   # Hint: Orbits are a list of lists
        self.orbits = orbits

    def orbit_count(self):      # Count all of the Orbitals children
        count = 0
        for v in self.orbital_map().values():
            count += len(v)     # Tally the amount of orbits

        return count

    def root_orbital(self, x,y = None): # The closest root orbital that had "You" & "Santa" in orbit
        root, count = None, 100000000   # Empty Root ID & Stupid large count to start
        searchers   = list(filter(None, [x,y]))                 # List of objects to search for, minus None
        for orbital, children in self.orbital_map().items():    # Find the closest root celestial body
            if all(o in children for o in searchers) and len(children) < count:
                root  = orbital         # Set the ID
                count = len(children)   # Reset the closest distance found

        return root

    def local_cluster(self, origin,destination):    # Orbitals of the Root, You, & Santa and those orbits inbetween
        cluster, orbitals = {}, self.orbital_map()  # The empty clustern and the mapped orbitals
        root_orbit        = orbitals[self.root_orbital(origin,destination)]
        origin_orbit      = orbitals[self.root_orbital(origin)]
        destination_orbit = orbitals[self.root_orbital(destination)]
        for orbit, children in orbitals.items():    # Filter the map for those orbits inbetween
            if orbit in root_orbit and any(o in children for o in [origin,destination]):    # must be in root and contain You & Santa
                cluster[orbit] = children   # Add Orbit

        return cluster

    def compute_orbital_transfers(self, origin,destination):
        return len(self.local_cluster(origin,destination))

    def orbital_map(self):  # Map out All Orbitals and their children
        o_map = {}

        for path in self.orbits:        # For each Orbital path
            for p in path:              # For each Orbital and Child
                if p not in o_map: 
                    o_map[p] = self.orbital_children(p) # Set Orbital with orbital children

        return o_map

    def orbital_children(self, parent): # Find Children of Orbital
        children = set([])              # Set avoids Duplicates
        for path in self.orbits:        # For each Orbital path
            if path[0] == parent:       # Find Chilren or Orbial
                children.add(path[1])   # Add child
                children.update(self.orbital_children(path[1])) # Look for children of the child
        return children