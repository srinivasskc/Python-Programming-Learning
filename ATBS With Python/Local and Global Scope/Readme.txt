The benefit that local scopes provide is that they separate a function's code from the rest of the program.

If something is going wrong because a variable has some bad value there's only a limited area of the program you have to check for this bug.

If something is going wrong in the global scope because of a bad variable value you only have to check the code in the global scope and if something is going wrong in sight of a function because of a bad variable you only have to check the code inside the function.

The code in the global scope Or a different functions local scope can't directly affect that functions local variables local scopes.
