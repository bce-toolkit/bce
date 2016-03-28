BCE
===================

The main function of this program is to **balance chemical equations** and help you **deal with complex chemical equations**.

It can also be used as a library, so that you can integrate it to your own product.

Features
-------------

 - Balance chemical equations (includes ionic equations, equations with multi-solutions, equations with SRU, equations with hydrates, electronic transferring equations, equations with abbreviations and indefinite equations).
 - Auto-correction (includes wrong side correction, useless substance detection and wrong balanced coefficient correction).
 - Common abbreviations (customizable).
 - Substitute unknown symbols in chemical equations.
 - Humanity error message.
 - High precision calculation.
 - Cross platform.
 - Multi languages support.
 - A set of APIs that can help you integrate this library to your own application.
 - Show output in both text and MathML format.

Dependencies
-------------

| Name   | Version    | Official Website                                   |
|--------|------------|----------------------------------------------------|
| Python | &gt;=2.7   | [https://www.python.org/](https://www.python.org/) |
| SymPy  | &gt;=0.7.3 | [https://www.sympy.org/](https://www.sympy.org/)   |

Installation
-------------

### Acknowledgement

Before installation, we assume that you have an operating system that supports Python and have installed Python.

Typically, a modern Linux/UNIX distribution has already bundled Python. But you have to check its version.

If you are using Microsoft Windows, you have to download Python from its [official website](https://www.python.org/downloads/windows/) and install it manually.

### From PyPI

Typically, you can use "pip" command to install the lastest release. Open the terminal and type following command:

```
pip install bce
```

Or if you use Python 3, type following command instead:

```
pip3 install bce
```

If you are using Linux/UNIX, please run these commands in root privilege. Typically, you can use command **su** or **sudo**.

### From source

Before installing from the source code, please make sure that you have installed all dependencies listed in the "Dependencies" chapter.

Type following commands in your terminal to install BCE:

```
python setup.py build
python setup.py install
```

If you are using Linux/UNIX, please run these commands in root privilege. Typically, you can use command **su** or **sudo**.

Usage
-------------

### Start the console

After installation, you can run BCE in your terminal by typing following command:

```
bce-console
```

Now you will see a prompt (the version numbers may be different):

```
BCE V4.7.9614
Copyright (C) 2014 - 2015 The BCE Authors. All rights reserved.
>> 
```

Now you can type chemical equation that you want to balance after the "&gt;&gt;" prompt. Type "Enter" key and then the program will give you the result or error messages. For example:

```
>> Fe2(SO4)3+Cu=Fe+CuSO4
Fe2(SO4)3+3Cu=2Fe+3CuSO4
>> Cu-<e->=Cu<2e+>
Cu-2<e->=Cu<2e+>
```

For more syntax information, please refers to the "Syntax (and examples)" chapter.

To exit this program, just type (press) "Ctrl+C" on your keyboard. Or if you are using Microsoft Windows operating system, you can simply close the window.

### Command line

"bce-console" has following arguments:

| Argument                        | Description                           |
|---------------------------------|---------------------------------------|
| -h, --help                      | Show help message and exit.           |
| --output-mathml                 | Show output in MathML format.         |
| --disable-banner                | Disable the start-up banner.          |
| --disable-bundled-abbreviations | Disable bundled abbreviations.        |
| --disable-error-correction      | Disable the error-correction feature. |
| --disable-auto-arranging        | Disable the auto-arranging feature.   |
| --unknown-header                | Set the header of unknown symbols.    |
| --load-abbreviations-file       | Load extra abbreviations from file.   |
| --language                      | Set the software language.            |
| --version                       | Show the software version.            |

### Custom software language

The program use your system language by default. If your system language is not supported, the program will use English(US).

If you don't want to use the default language, you can use "--language" command line to specify the displaying language.

For example, if you want to use Chinese(Simplified) as the displaying language, just type:

```
bce-console --language zh_cn
```

In this example, "zh_cn" is the language code. Currently, following languages are supported:

| Language             | Code           |
|----------------------|----------------|
| English (US)         | en, en_US      |
| Chinese (Simplified) | zh_cn, zh_hans |

### Abbreviation Definition File

You can customize your own abbreviations by writing a abbreviation definition file in JSON format.

For example:

```
{
    "AcOH": "CH3COOH",
    "PhOH": "[Ph]OH"
}
```

Save it so "custom.json" and run BCE with command line "--load-abbreviations-file" like following:

```
bce-console --load-abbreviations-file custom.json
```

Now you can use your customized abbreviations now. For example:

```
>> [PhOH]+O2=CO2+H2O
[PhOH]+7O2=6CO2+3H2O
```

### Custom Unknown Header

In order to handle chemical equations that have multiple balanced coefficients, the program has to generate a set of unknowns to represent the coefficients.

For example:

```
>> KI+O3=KIO3+O2
{3*Xa}KI+{3*Xa+2*Xb}O3={3*Xa}KIO3+{3*Xb}O2
```

In this example, "Xa" and "Xb" are generated by the program. In order to distinguish them from other unknowns, the program will add a header (such as "X") to each generated unknown.

You can customize the unknown header with command line "–unknown-header".

For example:

```
bce-console --unknown-header Y
```

Now type the example above again. You will see a different solution:

```
>> KI+O3=KIO3+O2
{3*Ya}KI+{3*Ya+2*Yb}O3={3*Ya}KIO3+{3*Yb}O2
```

Another thing you may pay attention to is that unknowns start with the header are reserved (protected) by the program. You can't use unknowns start with the header. Otherwise, you will got an error raised by the program like following:

```
>> C{Y}H{2Y+2}+O2=CO2+H2O
A parser error occurred (Code: PE.MEXP.USE_PROTECTED_HEADER):

Description:

    Used protected header.

Traceback:

    C{Y}H{2Y+2}+O2=CO2+H2O
    ^^^^^^^^^^^
    An error occurred when parsing the molecule.

    C{Y}H{2Y+2}
     ^^^
     An error occurred when parsing and evaluating this math expression.

    {Y}
     ^
     This symbol begins with the protected symbol header 'Y'.
```

Syntax (and examples)
-------------

### Basic syntax

The BCE syntax is simple and just like the hand-writing style. For example:

```
>> Na2CO3+HCl=NaCl+H2O+CO2
Na2CO3+2HCl=2NaCl+H2O+CO2
```

Here are the basic rules:

> 1. Use '=' to separate the reactants and the products.
> 2. Use '+' to connect each substance.
> 3. The syntax of the atom symbol is case-sensitive. The first letter of one atom symbol must be upper-case and others must be lower-case. 

In one molecule, you can specify the charge by adding "<{n}e+>" or "<{n}e->" at the end. {n} is a variable and it can be ignored if {n} equals to 1. For example:

```
>> Cl2+<e->=Cl<e->
Cl2+2<e->=2Cl<e->
>> Cu+Fe<3e+>=Cu<2e+>+Fe<2e+>
Cu+2Fe<3e+>=Cu<2e+>+2Fe<2e+>
```

Equations with multi-solutions are also supported. For example:

```
>> C+O2=CO+CO2
{2*Xa+2*Xb}C+{Xa+2*Xb}O2={2*Xa}CO+{2*Xb}CO2
>> Cu+HNO3=Cu(NO3)2+NO+NO2+H2O
{-Xa+3*Xb}Cu+{8*Xb}HNO3={-Xa+3*Xb}Cu(NO3)2+{-2*Xa+2*Xb}NO+{4*Xa}NO2+{4*Xb}H2O
```

In this example, 'Xa' and 'Xb' are variables. You can do substitution by assigning values to them.

### Hydrates

Hydrate molecules are supported. Use "." to describe hydrate dots. For example:

```
>> CuSO4.5H2O=CuSO4+H2O
CuSO4.5H2O=CuSO4+5H2O
>> LiOH+H2O2+H2O=Li2O2.H2O2.3H2O
2LiOH+2H2O2+H2O=Li2O2.H2O2.3H2O
```

### Abbreviations

In hand writing, we always use abbreviations such as Et, Ph and Ac. In BCE, you can also use abbreviations. Just surround the abbreviation with "[" and "]". For example:

```
>> [Et]OH+O2=CO2+H2O
[Et]OH+3O2=2CO2+3H2O
```

For all supported abbreviations, please open "docs/abbreviations/arv_reference.pdf".

### Variables and expressions

You can use expressions and variables in your chemical equation. For example:

```
>> C{n}H{2n+2}+O2=CO2+H2O
{(n+1)^(-1)}C{n}H{2*n+2}+{(1/2)*(3*n+1)/(n+1)}O2={n/(n+1)}CO2+H2O
>> CH3(CHCH){n}CH3+Cl2=CH3(CHClCHCl){n}CH3
CH3(CHCH){n}CH3+{n}Cl2=CH3(CHClCHCl){n}CH3
>> X-<e->=X<{n}e+>
X-{n}<e->=X<{n}e+>
```

One thing that you may need to pay attention to is that the first letter of the variables you use can't be 'X'. Variables start with 'X' are reserved by the program.

In one expression, you can use operators "+", "-", "*", "/" and "^" ("^" means power, such as 2^3=8). You can also use functions listed in following table:

| Function | Description                      |
|----------|----------------------------------|
| sqrt(x)  | The square root of variable 'x'. |
| pow(x,y) | Equals to x^y.                   |

### Automatic side arranging

If you get several substances and you don't know which are reactants and which are products, you can use ";" to separate each substance and type them to BCE. The program will help you decide the reactants and the products. For example:

```
>> NH4Cl;K2(HgI4);KCl;KI;H2O;Hg2NH2OI;KOH
NH4Cl+2K2(HgI4)+4KOH=KCl+7KI+3H2O+Hg2NH2OI
```

We have to acknowledge that the solving algorithm has some limitations. Currently, the algorithm can't decide the reaction direction precisely. You may have to decide it yourself. For example:

```
>> CH4;HCN;NH3;O2;H2O
2HCN+6H2O=2CH4+2NH3+3O2
```

The correction result should be:

```
2CH4+2NH3+3O2=2HCN+6H2O
```

To avoid this condition, you can specify the status of each substance by adding "(g)", "(l)", "(s)", "(aq)" at the end to let the program guess the reaction direction. For example.

```
>> CH4(g);HCN(g);NH3(g);O2(g);H2O(g)
2CH4(g)+2NH3(g)+3O2(g)=2HCN(g)+6H2O(g)
```

It is correct now.

Also, the program can't balance the equation if it has multi solutions. The program will report a logic error in such condition. For example:

```
>> C;CO2;CO;O2
A logic error occurred (Code: LE.BCE.SIDE_ELIMINATED):

Description:

    Can't balance chemical equations (with auto-correction form) that have multiple answers.
```

Service
-------------

It is our proud to provide service to you and improve our product. If you have questions about this program, please [send a mail](mailto://bcepy.service@gmail.com) to us.

All services are free of charge.

