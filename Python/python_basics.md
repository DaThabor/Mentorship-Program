# Python Basics

This notebook walks through the basics of Python programming. After understanding the basic syntax and coding principles, the examples are given for executing Data Analysis.

## Python Packages

Most of the code that you use in Python is either based on the base Python package (as pre-loaded when Python is installed). All other code is coming from so called Python packages, containing specific **functions** that can be called to execute a specific code.

The common packages used for Data Analysis are *pandas* and *numpy*.

For plotting of visuals the package that is mostly used is *matplotlib*.

### Install Packages

To use the packages we first need to install them in our environment to make sure that the package is available. There are many ways of installing Python packages, and they differ per type of environment to install them. E.g. A standard way of installing packages is like:

```python
python.exe -m pip install pandas
```

- 'python.exe' is used to indicate python is used for the packages
- '-m' is indicating 'Module'
- 'pip' is the pacakge that is used to install packages
- 'install' is the function in the pip package to install packages
- 'pandas' is an example of a package name

### Import packages

Once a package is installed (in many tools the common packages are already pre-loaded), you need to import the package in your python script (or Notebook). Importing a package can be done in three ways:

1. Import package as is

```python
import pandas
```

2. Import package with an abbrevation*

```python
import pandas as pd
```

3. Import a specific function from a package

```python
from pandas import read_csv
```

*Giving the package an abbreviated name makes it easier to use the package in your code, as you don't need to write the whole name again and again. For the common packages the abbreviations are also known in the community, e.g.

Common abbreviations used in the community are:
- pandas as pd
- numpy as np
- plotly as plt

Then when you add this to your import statement it will look like this:

```python
import pandas as pd # use abbrevation

#Use pd here as abbreviation of pandas package
df = pd.DataFrame() 
```

The idea is to use the abbreviation mostly for common packages (as others will recognize which package you're using) or use it for long package names. Just make sure that you use the same abbreviations throughout.

## Basic Python Syntax

In Python the following items are important to keep in mind when creating python code:

### Indentation

When you write code, Python requires indentation of the code when code blocks are part of each other. A single line of code can be written as is, but for cases as IF statements, FOR loops, etc. the indentation is important. When using the TAB you can create the appropriate indentation.

Example:

```python
if (x>y):
print(5)
```

This is the wrong syntax and will result in an error (run the next line of code to see the error).

```python
x=10
y=5

if (x>y):
print(5)
```

it will give a proper error message about the indentation.

Correct the code and run the cell below to see the correct output:

```python
x=10
y=5

if (x>y):
  print(5) # see the indentation at the start of this line
```

### Indexing

Python uses an index starting from '0'. Keep this in mind when referring to any variables, columns or rows.

This means that the first column in a dataset has the index '0' and the first row also has the index of '0'

So the following example will refer to columns 2 and 3, while the index is '1' and '2':

```python
x = ("First","Second","Third")

# this statement will print index number 1 and 2 (all before 3)
print(x[1:3])
```

The output will then be:

```python
"Second", "Third"
```

Here we also see that to get the second and third column we can specify a range of values ('1:3' in this example). This means that we want to see each column starting from index 1 ("Second") and before index 3 ("Third").

The last part is important in Python to understand that referring to a range of values it's always from the starting index and before the next index.

