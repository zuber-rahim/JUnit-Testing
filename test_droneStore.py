import unittest
from drones import Drone, DroneStore
from operators import Operator

class DronestoreTest(unittest.TestCase):


    def test_DroneStore_add(self):
        #Arrange
        dr = Drone("Test Drone")
        store = DroneStore()
        
        #Act
        act = store.add(dr)
        #print(dr.id in store.list_all()) used to test output
    
        #Assert 
        self.assertEqual(dr.id in store.list_all(), True, "Drone has not been added successfully")
        
    def test_DroneStore_remove(self):
        #Arrange
        dr = Drone("Test Drone")
        store = DroneStore()
        
        #Act
        act = store.add(dr)
        act2 = store.remove(dr)
        #print(dr.id in store.list_all()) used to test output
    
        #Assert 
        self.assertEqual(dr.id in store.list_all(), False, "Drone has not been removed successfully")
            
    def test_DroneStore_add_error(self):
        #Arrange
        dr = Drone("Test Drone")
        store = DroneStore()
        
        #Act
        act = store.add(dr)
    
        #Assert 
        with self.assertRaises(Exception):store.add(dr)
        
    def test_DroneStore_remove_error(self):
        dr = Drone("Test Drone")
        store = DroneStore()
        
        #Act
        #act = store.remove(dr)
        
        #Assert
        with self.assertRaises(Exception) as context:
            store.remove(dr)
        self.assertEqual("Drone does not exist in store", str(context.exception))
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()