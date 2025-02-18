def func():
    var = 1
    def func2():
        nonlocal var
        var += 1
    
