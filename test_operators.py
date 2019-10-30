import unittest

from drones import Drone, DroneStore
from operators import Operator, OperatorStore, OperatorAction
from datetime import date


class OperatorTest(unittest.TestCase):


    def test_operator_validation(self):
        #Arrange
        op = Operator()
        op.first_name = "Afzal"
        op.family_name = "Rahim"
        dob = date(1974, 9, 12)
        op.date_of_birth = dob
        op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 6
        store = OperatorStore()
        
        #Act
        act = store.add(op)
        
        #Assert
        if act.is_valid():
            act.commit()
        #print(act.messages)
        #print(store._operators)    
        self.assertTrue(act.is_valid())

        
    def test_nameError(self):
        #Arrange
        op = Operator()
        #op.first_name = "Afzal"
        op.family_name = "Rahim"
        dob = date(1974, 9, 12)
        op.date_of_birth = dob
        op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 6
        store = OperatorStore()
        #action = OperatorAction(op, store._add(op))
        
        #Act
        act = store.add(op)
        
        #Assert
        if act.is_valid():
            act.commit()
        else:
            #self.assertEqual(self.assertIn('First name is required', act.messages), False, 'First name is required')
            self.assertEqual('First name is required' in act.messages, False, 'First name is required.')

    def test_dobError(self):
        #Arrange
        op = Operator()
        op.first_name = "Afzal"
        op.family_name = "Rahim"
        #dob = date(1974, 9, 12)
        #op.date_of_birth = dob
        op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 6
        store = OperatorStore()
        #action = OperatorAction(op, store._add(op))
    
        #Act
        act = store.add(op)
        
        #Assert
        if act.is_valid():
            act.commit()
        else:
            #self.assertIn('Date of birth is required', act.messages)
            self.assertEqual('Date of birth is required' in act.messages, False, 'Date of birth is required.')

    def test_droneLicenceError(self):
        #Arrange
        op = Operator()
        op.first_name = "Afzal"
        op.family_name = "Rahim"
        dob = date(1974, 9, 12)
        op.date_of_birth = dob
        #op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 6
        store = OperatorStore()
        #action = OperatorAction(op, store._add(op))
        
        #Act
        act = store.add(op)
        
        #Assert
        if act.is_valid():
            act.commit()
        else:
            #self.assertFalse(act.is_valid())
            #self.assertTrue("Drone license is required" in act.messages)
            self.assertEqual('Drone license is required' in act.messages, False, 'Drone license is required.')

            
    def test_droneLicence_validity(self):
        #Arrange
        op = Operator()
        op.first_name = "Afzal"
        op.family_name = "Rahim"
        dob = date(2017, 9, 12)
        op.date_of_birth = dob
        op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 6
        store = OperatorStore()
        #action = OperatorAction(op, store._add(op))
        
        #Act
        act = store.add(op)
        
        #Assert
        if act.is_valid():
            act.commit()
        else:
            #self.assertIn('Operator should be at least twenty to hold a class 2 license', act.messages)
            self.assertEqual('Operator should be at least twenty to hold a class 2 license' in act.messages, False, 'Operator should be at least twenty to hold a class 2 license')

    def test_rescueEndorsement_validity(self):
        #Arrange
        op = Operator()
        op.first_name = "Afzal"
        op.family_name = "Rahim"
        dob = date(1974, 9, 12)
        op.date_of_birth = dob
        op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 2
        store = OperatorStore()
        #action = OperatorAction(op, store._add(op))
        
        #Act
        act = store.add(op)
        
        #Assert
        if act.is_valid():
            act.commit()
        else:
            #self.assertIn('The operator must have been involved in five prior rescue operations.', act.messages)
            self.assertEqual('The operator must have been involved in five prior rescue operations' in act.messages, False, 'The operator must have been involved in five prior rescue operations.')

    def test_operatorStore_added_successfully(self):
        #Arrange
        op = Operator()
        op.first_name = "Afzal"
        op.family_name = "Rahim"
        dob = date(1974, 9, 12)
        op.date_of_birth = dob
        op.drone_license = 2
        op.rescue_endorsement = True
        op.operations = 6
        store = OperatorStore()
        
        #Act
        act = store.add(op)
        
        if act.is_valid():
            act.commit()
        #Assert
        #self.assertTrue(store.get(op.id), True, "Operator has not been added successfully")
        self.assertTrue(store.get(op.id))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()