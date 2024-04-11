from tree import BinarySearchTree


class GardenPlantTracker(BinarySearchTree):

    def add_plant(self, plant_id):
        # Use the existing insert method to add a new plant
        self.insert(plant_id)
        print(f"Plant {plant_id} added to the garden.")

    def search_plant(self, plant_id):
        # Use the existing search method to find a plant
        if self.search(plant_id):
            print(f"Plant {plant_id} is in the garden.")
        else:
            print(f"Plant {plant_id} is not found in the garden.")

    def remove_plant(self, plant_id):
        # Use the existing delete method to remove a plant
        self.delete(plant_id)
        print(f"Plant {plant_id} has been removed from the garden.")


# Implement the Garden Plant Tracker.
garden_tracker = GardenPlantTracker()

# Adding plants
garden_tracker.add_plant(10)
garden_tracker.add_plant(5)

# Searching for a plant
garden_tracker.search_plant(10)
garden_tracker.search_plant(7)  # This plant does not exist

# Removing a plant
garden_tracker.remove_plant(5)
garden_tracker.search_plant(5)  # This should confirm the plant is removed
