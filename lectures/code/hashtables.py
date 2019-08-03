from dataclasses import dataclass

@dataclass
class Account:
    id: int
    balance: int
    owners: list # of Customer

@dataclass
class Customer:
    name: str
    acct: Account

# global variables for the central data
all_acctsHT: dict = {}
all_acctsL: list = []

next_id: int = 1 # the next available id number

# -------- Lists version ----------------

def create_acctL(cust_name: str, init_bal: int) -> Account:
    """create new account and add to account list"""
    global next_id

    # create account datum with circular references
    a = Account(next_id, init_bal, [])
    c = Customer(cust_name, a)
    a.owners.append(c)

    # store account in data structure
    all_acctsL.append(a)

    # advance next_id
    next_id = next_id + 1
    return a

def lookup_acctL(acct_num : int) -> Account:
    for a in all_acctsL:
        if a.id == acct_num:
            return a

# this gets at the assumptions/invariants we want on our system ...
def close_acctL(acct_num : int) -> None:
    """remove acct with given id from list of accts"""
    a = lookup_acctL(acct_num)
    for o in a.owners:
        o.acct = None
    all_acctsL.remove(a)

def add_owner(name: str, acct_num : int):
    """add owner to acct with given id"""
    a = lookup_acctL(acct_num)
    c = Customer(name, a)
    a.owners.append(c)


def deposit(amt: int, to_acct: int) -> int:
    """deposit into acct with given id, returning new balance"""
    a = lookup_acctL(to_acct)
    a.balance = a.balance + amt
    return a.balance

# -------- Hashtable version ----------------

def create_acctHT(cust_name: str, init_bal: int) -> Account:
    """create new account and add to account hashtable"""

    global next_id

    # create account datum with circular references
    a = Account(next_id, init_bal, [])
    c = Customer(cust_name, a)
    a.owners.append(c)

    # store account in data structure
    all_acctsHT[next_id] = a

    # advance next_id
    next_id = next_id + 1

    return a

def lookup_acctHT(acct_num : int) -> Account:
    return all_acctsHT[acct_num]

def close_acctHT(acct_num : int) -> None:
    """remove acct with given id from hashtable of accts"""
    a = lookup_acctHT(acct_num)
    for o in a.owners:
        o.acct = None
    del all_acctsHT[a.id]

create_acctHT("Tina", 150)
create_acctHT("Maria", 250)
print(all_acctsHT)

# ------- Rooms and seats ----------

# a hashtable mapping classrooms to numbers of seats
room_capacity = {"CIT368": 63,
                 "BERT130": 200,
                 "FRDMN101": 48
                 }

# hashtable mapping seat ranges to classrooms
capacities = {"45-65": ["CIT368", "FRDMN101"],
              "65-100: [],"
              "150-200": ["BERT130"]}

print(capacities)
