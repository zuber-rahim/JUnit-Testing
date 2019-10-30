class Drone(object):
    """ Stores details on a drone. """

    def __init__(self, name, class_type=1, rescue=False):
        self.id = 0
        self.name = name
        self.class_type = class_type
        self.rescue = rescue
        self.operator = None

class DroneAction(object):
    """ A pending action on the DroneStore. """

    def __init__(self, drone, operator, commit_action):
        self.drone = drone
        self.operator = operator
        self.messages = []
        self._commit_action = commit_action
        self._committed = False


    def add_message(self, message):
        """ Adds a message to the action. """
        self.messages.append(message)

    def is_valid(self):
        """ Returns True if the action is valid, False otherwise. """
        return len(self.messages) == 0

    def commit(self):
        """ Commits (performs) this action. """
        if self._committed:
            raise Exception("Action has already been committed")

        self._commit_action(self.drone, self.operator)
        self._committed = True


class DroneStore(object):
    """ DroneStore stores all the drones for DALSys. """

    def __init__(self, conn=None):
        self._drones = {}
        self._last_id = 0
        self._conn = conn

    def add(self, drone):
        """ Adds a new drone to the store. """
        if drone.id in self._drones:
            raise Exception('Drone already exists in store')
        else:
            self._last_id += 1
            drone.id = self._last_id
            self._drones[drone.id] = drone

    def remove(self, drone):
        """ Removes a drone from the store. """
        if not drone.id in self._drones:
            raise Exception('Drone does not exist in store')
        else:
            del self._drones[drone.id]

    def get(self, id):
        """ Retrieves a drone from the store by its ID. """
        if not id in self._drones:
            return None
        else:
            return self._drones[id]

    def list_all(self):
        """ Lists all the drones in the system. """
        for drone in self._drones:
            yield drone

    def allocate(self, drone, operator):
        """ Starts the allocation of a drone to an operator. """
        action = DroneAction(drone, operator, self._allocate)
        if operator.drone is not None: 
            action.add_message("Operator can only control one drone")
        if drone.class_type != operator.drone_license:
            action.add_message("Operator does not have correct drone license")
        if drone.rescue == True and operator.rescue_endorsement != True:
            action.add_message("Operator does not have rescue endorsement")
            
        return action

    def _allocate(self, drone, operator):
        """ Performs the actual allocation of the operator to the drone. """
        if operator.drone is not None:
            # If the operator had a drone previously, we need to clean it so it does not
            # hold an incorrect reference
            operator.drone.operator = None
            
        operator.drone = drone
        drone.operator = operator
            
        #if operator.drone_license == 1 or operator.drone_license == 2:

        self.save(drone)

    def save(self, drone):
        """ Saves the drone to the database. """
        pass    # TODO: we don't have a database yet
