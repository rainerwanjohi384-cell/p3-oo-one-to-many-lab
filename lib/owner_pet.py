class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of Pet instances owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of pets sorted by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None

        # If an owner is provided, assign them using add_pet to ensure type check
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            owner.add_pet(self)

        Pet.all.append(self)