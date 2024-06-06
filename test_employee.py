from .employee import employee

def test_employeeNaming():
    employee1 = employee()
    employee1.setEmployeeName("Chris")
    assert employee1.getEmployeeName() == "Chris"