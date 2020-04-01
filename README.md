# Python workshop
Python workshop for AFRY, where we will go through some helpfull things that might be new for some and old news for some.

## Content
This is a list of what the python workshop contains. It is some popular modules and some tips and trix.
- NumPy
- Matplotlib
- Generators
- Lambda functiones
- RegEx
- Args, argv, kwargs, named arguments
- Decorators
- Data model methods
- API-requests/JSON

## Running virtual environment
It is not mandatory to use a virtual environment, but it is suggested in order to not screw up the systems python environment.

In the folder where you would like to create your virtual environment:

```> python -m venv .venv```

This will create the environment, ".venv" is the location of the virtual environment.
In order to use it, it needs to be activated. Or it is not needed but it will make your life easier. Otherwise you would like to use the complete path to the virtual environments scripts.
To activate the environment:

```> .venv\Scripts\activate.bat   (cmd)```
```> .venv\Scripts\Activate.ps1   (PowerShell)```

You are now using the virtual environments python interpreter.
So running:

```> pip list```

Should show you a rather short list, with only pip and setuptools.
Now install the modules that we eill use by:

```> pip install -r requirements.txt```

This will take a list of modules, from requirements.txt, and install them.
It should now be possible to use the modules in your python script.
Since you have activated your virtual environment you run your python script with

```> python example.py```

When finished and you want to go back to the sysmte wide python use:

```> deactivate```
