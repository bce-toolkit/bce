API Reference
===================

Modules
-------------

The modules that you can get access to have been listed in following table:

| Package              | Description                            |
|----------------------|----------------------------------------|
| bce.option           | Options container.                     |
| bce.public.api       | Public accessible APIs.                |
| bce.public.database  | Bundled databases.                     |
| bce.public.exception | Exceptions.                            |
| bce.public.option    | Option wrappers for different modules. |
| bce.public.printer   | Printers.                              |

Options
-------------

### Container (bce.option.Option)

Options container is similar to a Python dictionary. It contains settings that is required by the program.

In order to keep our program clear, getting access to the container directly is prohibited. The only way to modify settings in a container is to use "wrappers" provided by different modules.

So the only work that you have to do is to create an option container instance before doing anything. For example:

```
import bce.option as _opt

#  Create an option container instance.
opt_container = _opt.Option()
```

### Wrapper for L10N module (bce.public.option.LocaleOptionWrapper)

If you want to modify localization settings, you can use the wrapper. To begin with, you have to wrap the option container with the wrapper. For example:

```
import bce.public.option as _opt_wrapper

#  Wrap the option container.
#  ('opt' variable is the option container.)
l10n_option = _opt_wrapper.LocaleOptionWrapper(opt)
```

Then you can do modification through the wrapper.

LocaleOptionWrapper class has following methods:

| Method                   | Description          | Arguments                       | Return           |
|--------------------------|----------------------|---------------------------------|------------------|
| get_language_id()        | Get the language ID. | None                            | The language ID. |
| set_language_id(lang_id) | Set the language ID. | lang_id (str): The language ID. | None             |

Here is an example:

```
#  Modify language to Chinese (Simplified).
l10n_option.set_language_id("zh_cn")
```

### Wrapper for balancer module (bce.public.option.BalancerOptionWrapper)

If you want to enable or disable the features of the balancer, you can use the wrapper. To begin with, you have to wrap the option container with the wrapper. For example:

```
import bce.public.option as _opt_wrapper

#  Wrap the option container.
#  ('opt' variable is the option container.)
bce_option = _opt_wrapper.BalancerOptionWrapper(opt)
```

Then you can do modification through the wrapper.

BalancerOptionWrapper class has following methods:

| Method                                           | Description                                          | Arguments                        | Return                 |
|--------------------------------------------------|------------------------------------------------------|----------------------------------|------------------------|
| enable_error_correction_feature(enabled=True)    | Enable / disable the error-correction feature.       | enabled (bool): True if enabled. | None                   |
| is_error_correction_feature_enabled()            | Get whether the error-correction feature is enabled. | None                             | bool: True if enabled. |
| enable_auto_side_arranging_feature(enabled=True) | Enable / disable the auto-arranging feature.         | enabled (bool): True if enabled. | None                   |
| is_auto_side_arranging_feature_enabled()         | Get whether the auto-arranging feature is enabled.   | None                             | bool: True if enabled. |

Here is an example:

```
#  Disable the error-correction feature.
bce_option.enable_error_correction_feature(False)

#  Disable the auto-arranging feature.
bce_option.enable_auto_side_arranging_feature(False)
```

### Wrapper for molecule parser module (bce.public.option.MoleculeParserOptionWrapper)


If you want to the settings of the molecule parser, you can use the wrapper. To begin with, you have to wrap the option container with the wrapper. For example:

```
import bce.public.option as _opt_wrapper

#  Wrap the option container.
#  ('opt' variable is the option container.)
mp_option = _opt_wrapper.MoleculeParserOptionWrapper(opt)
```

Then you can do modification through the wrapper.

MoleculeParserOptionWrapper class has following methods:

| Method                            | Description                   | Arguments                             | Return                        |
|-----------------------------------|-------------------------------|---------------------------------------|-------------------------------|
| get_abbreviation_mapping()        | Get the abbreviation mapping. | None                                  | dict: The abbreviation map. |
| set_abbreviation_mapping(mapping) | Set the abbreviation mapping. | mapping (dict): The abbreviation map. | None                          |

Here is an example:

```
#  Set the abbreviation map.
mp_option.set_abbreviation_mapping({
    "Test1": "C6H5OH",
    "Test2": "(CH3)2CHOOPF(CH3)"
})

#
#  Now you can use abbreviations "[Test1]" and "[Test2]".
#
```

Printers (bce.public.printer)
-------------

The program can generate output to both plain text and MathML format. Each output method is called a "printer". The balancer needs one of these printers to generate the output.

This module contains several constants (called "Printer ID") refer to different printers. See following table:

| Constant       | Printer                 |
|----------------|-------------------------|
| PRINTER_TEXT   | The plain text printer. |
| PRINTER_MATHML | The MathML printer.     |

APIs (bce.public.api)
-------------

### Balancer

To balancer a chemical equation, you can use **balance_chemical_equation()** method.

Here are the details of the parameters:

| ID | Parameter      | Type              | Description                                      | Is Optional |
|----|----------------|-------------------|--------------------------------------------------|-------------|
| 1  | expression     | str               | The chemical equation.                           | No          |
| 2  | option         | bce.option.Option | The options container.                           | No          |
| 3  | printer        | int               | The printer ID. (Default: PRINTER_TEXT)          | Yes         |
| 4  | unknown_header | str               | The header of generated unknowns. (Default: "X") | Yes         |

Here are the details of the return value:

| Type | Description          |
|------|----------------------|
| str  | The balanced result. |

Example:

```
import bce.option as _opt
import bce.public.api as _public_api
import bce.public.printer as _public_printer

#  Create an option instance.
opt = _opt.Option()

#  Balance.
print(_public_api.balance_chemical_equation(
    "Na2CO3+HCl=NaCl+H2O+CO2",
    opt,
    printer=_public_printer.PRINTER_TEXT,
    unknown_header="X"
))
print(_public_api.balance_chemical_equation(
    "Na2CO3+HCl=NaCl+H2O+CO2",
    opt,
    printer=_public_printer.PRINTER_MATHML,
    unknown_header="X"
))
print(_public_api.balance_chemical_equation(
    "Cu+HNO3=Cu(NO3)2+NO+NO2+H2O",
    opt,
    printer=_public_printer.PRINTER_TEXT,
    unknown_header="T"
))
```

The output of the first print() is:

```
Na2CO3+2HCl=2NaCl+H2O+CO2
```

The output of the second print() is:

```
<mrow>
    <mrow>
        <msub>
            <mtext>Na</mtext>
            <mn>2</mn>
        </msub>
        <mtext>C</mtext>
        <msub>
            <mtext>O</mtext>
            <mn>3</mn>
        </msub>
    </mrow>
    <mo>+</mo>
    <mrow>
        <mn>2</mn>
        <mtext>H</mtext>
        <mtext>Cl</mtext>
    </mrow>
    <mo>=</mo>
    <mrow>
        <mn>2</mn>
        <mtext>Na</mtext>
        <mtext>Cl</mtext>
    </mrow>
    <mo>+</mo>
    <mrow>
        <msub>
            <mtext>H</mtext>
            <mn>2</mn>
        </msub>
        <mtext>O</mtext>
    </mrow>
    <mo>+</mo>
    <mrow>
        <mtext>C</mtext>
        <msub>
            <mtext>O</mtext>
            <mn>2</mn>
        </msub>
    </mrow>
</mrow>
```

You can use [MathJax](https://www.mathjax.org/) or something else to render the MathML. Please pay attention, you have to use the &lt;math&gt; and the &lt;/math&gt; labels to wrap the output. Like following:

```
<math>
   (Paste the output here.)
</math>
```

The output of the third print() is:

```
{-Ta+3*Tb}Cu+{8*Tb}HNO3={-Ta+3*Tb}Cu(NO3)2+{-2*Ta+2*Tb}NO+{4*Ta}NO2+{4*Tb}H2O
```

### Substitution

A chemical equation may contains some unknowns. You can assign values to these unknowns through the **substitute_chemical_equation()** method.

Here are the details of the parameters:

| ID | Parameter      | Type              | Description                                                     | Is Optional |
|----|----------------|-------------------|-----------------------------------------------------------------|-------------|
| 1  | expression     | str               | The origin chemical equation.                                   | No          |
| 2  | substitute_map | dict              | The substitution map (from unknown symbols to assigned values). | No          |
| 3  | option         | bce.option.Option | The options container.                                          | No          |
| 4  | printer        | int               | The printer ID. (Default: PRINTER_TEXT)                         | Yes         |
| 5  | unknown_header | str               | The header of generated unknowns. (Default: "X")                | Yes         |

Moreover, the "unknown_header" parameter of this method only affects the MathML printer. If the printer is not MathML printer, the parameter has no effect.

Here are the details of the return value:

| Type | Description             |
|------|-------------------------|
| str  | The substituted result. |

Example:

```
import bce.option as _opt
import bce.public.api as _public_api
import bce.public.printer as _public_printer
import sympy as _sympy

#  Create an option instance.
opt = _opt.Option()

#  Substitute.
print(_public_api.substitute_chemical_equation(
    "{-Ta+3*Tb}Cu+{8*Tb}HNO3={-Ta+3*Tb}Cu(NO3)2+{-2*Ta+2*Tb}NO+{4*Ta}NO2+{4*Tb}H2O",
    {
        "Ta": _sympy.Integer(0),
        "Tb": _sympy.Integer(1)
    },
    opt,
    printer=_public_printer.PRINTER_TEXT
))
print(_public_api.substitute_chemical_equation(
    "{2*Xa+5*Xb}KClO3+{12*Xa+6*Xb}HCl={2*Xa+5*Xb}KCl+{6*Xa+3*Xb}H2O+{6*Xa}Cl2+{6*Xb}ClO2",
    {
        "Xa": _sympy.Integer(1)
    },
    opt,
    printer=_public_printer.PRINTER_MATHML,
    unknown_header="X"
))
```

The output of the first print() is:

```
3Cu+8HNO3=3Cu(NO3)2+2NO+4H2O
```

The output of the second print() is:

```
<mrow>
    <mrow>
        <mrow>
            <mo>(</mo>
            <mrow>
                <mrow>
                    <mn>5</mn>
                    <msub>
                        <mtext>x</mtext>
                        <mtext>b</mtext>
                    </msub>
                </mrow>
                <mo>+</mo>
                <mn>2</mn>
            </mrow>
            <mo>)</mo>
        </mrow>
        <mtext>K</mtext>
        <mtext>Cl</mtext>
        <msub>
            <mtext>O</mtext>
            <mn>3</mn>
        </msub>
    </mrow>
    <mo>+</mo>
    <mrow>
        <mrow>
            <mo>(</mo>
            <mrow>
                <mrow>
                    <mn>6</mn>
                    <msub>
                        <mtext>x</mtext>
                        <mtext>b</mtext>
                    </msub>
                </mrow>
                <mo>+</mo>
                <mn>12</mn>
            </mrow>
            <mo>)</mo>
        </mrow>
        <mtext>H</mtext>
        <mtext>Cl</mtext>
    </mrow>
    <mo>=</mo>
    <mrow>
        <mrow>
            <mo>(</mo>
            <mrow>
                <mrow>
                    <mn>5</mn>
                    <msub>
                        <mtext>x</mtext>
                        <mtext>b</mtext>
                    </msub>
                </mrow>
                <mo>+</mo>
                <mn>2</mn>
            </mrow>
            <mo>)</mo>
        </mrow>
        <mtext>K</mtext>
        <mtext>Cl</mtext>
    </mrow>
    <mo>+</mo>
    <mrow>
        <mrow>
            <mo>(</mo>
            <mrow>
                <mrow>
                    <mn>3</mn>
                    <msub>
                        <mtext>x</mtext>
                        <mtext>b</mtext>
                    </msub>
                </mrow>
                <mo>+</mo>
                <mn>6</mn>
            </mrow>
            <mo>)</mo>
        </mrow>
        <msub>
            <mtext>H</mtext>
            <mn>2</mn>
        </msub>
        <mtext>O</mtext>
    </mrow>
    <mo>+</mo>
    <mrow>
        <mn>6</mn>
        <msub>
            <mtext>Cl</mtext>
            <mn>2</mn>
        </msub>
    </mrow>
    <mo>+</mo>
    <mrow>
        <mrow>
            <mo>(</mo>
            <mrow>
                <mn>6</mn>
                <msub>
                    <mtext>x</mtext>
                    <mtext>b</mtext>
                </msub>
            </mrow>
            <mo>)</mo>
        </mrow>
        <mtext>Cl</mtext>
        <msub>
            <mtext>O</mtext>
            <mn>2</mn>
        </msub>
    </mrow>
</mrow>
```

### Checker

To check whether a chemical equation is balanced, you can use **is_chemical_equation_balanced()** method.

Here are the details of the parameters:

| ID | Parameter  | Type              | Description            | Is Optional |
|----|------------|-------------------|------------------------|-------------|
| 1  | expression | str               | The chemical equation. | No          |
| 2  | option     | bce.option.Option | The options container. | No          |

Here are the details of the return value:

| Type | Description       |
|------|-------------------|
| bool | True if balanced. |

Example:

```
import bce.option as _opt
import bce.public.api as _public_api

#  Create an option instance.
opt = _opt.Option()

#  Check.
print(_public_api.is_chemical_equation_balanced(
    "2NH3+2CH4+3O2=2HCN+6H2O",
    opt
))
print(_public_api.is_chemical_equation_balanced(
    "{-Xa+4*Xb}NH4<e+>+{3*Xa+8*Xb}NO2<e->+{4*Xa+4*Xb}H<e+>={-4*Xa+6*Xb}N2O+{10*Xa}NO+{10*Xb}H2O",
    opt
))
print(_public_api.is_chemical_equation_balanced(
    #  The correct one is "3NO2+H2O=2HNO3+NO".
    "2NO2+H2O=2HNO3+NO",
    opt
))
```

The output is:

```
True
True
False
```

Exceptions (bce.public.exception)
-------------

Following exceptions are provided in order to handle different errors:

| Class                     | Description                                            | Message                             |
|---------------------------|--------------------------------------------------------|-------------------------------------|
| ParserErrorWrapper        | Raise if an error occurred while parsing expressions.  | The detailed exception information. |
| LogicErrorWrapper         | Raise if an error occurred while do logic processing.  | The detailed exception information. |
| InvalidCharacterException | Raise if the expression contains invalid character(s). | None                                |
| SubstitutionErrorWrapper  | Raise if an error occurred while do substitution.      | None                                |

Example 1:

```
import bce.option as _opt
import bce.public.api as _public_api
import bce.public.exception as _public_exception
import bce.public.printer as _public_printer

#  Create an option instance.
opt = _opt.Option()

#  Test cases.
tests = [
    "Cu{x+2.5.0}+O2=CuO",
    "A2B=B2A",
    "#"
]

for expression in tests:
    #  Do balancing.
    try:
        print(_public_api.balance_chemical_equation(
            expression,
            opt,
            printer=_public_printer.PRINTER_TEXT,
            unknown_header="X"
        ))
    except _public_exception.ParserErrorWrapper as err:
        print(str(err))
    except _public_exception.LogicErrorWrapper as err:
        print(str(err))
    except _public_exception.InvalidCharacterException as err:
        print("Found invalid character(s).")

    #  Show a separator.
    print("")
    print("<--->")
    print("")
```

The output of "Example 1" is:

```
A parser error occurred (Code: PE.MEXP.DUPLICATED_DECIMAL_DOT):

Description:

    Duplicated decimal dot.

Traceback:

    Cu{x+2.5.0}+O2=CuO
    ^^^^^^^^^^^
    An error occurred when parsing the molecule.

    Cu{x+2.5.0}
      ^^^^^^^^^
      An error occurred when parsing and evaluating this math expression.

    {x+2.5.0}
        ^
        Here's the previous decimal dot.

    {x+2.5.0}
          ^
          Here's the duplicated decimal dot.

<--->

A logic error occurred (Code: LE.BCE.SIDE_ELIMINATED):

Description:

    All molecules in the chemical equation was eliminated.

<--->

Found invalid character(s).

<--->
```

Example 2:

```
import bce.option as _opt
import bce.public.api as _public_api
import bce.public.exception as _public_exception
import bce.public.printer as _public_printer
import sympy as _sympy

#  Create an option instance.
opt = _opt.Option()

#  Do substitution.
try:
    print(_public_api.substitute_chemical_equation(
        "{Xa+Xb}Cu+{4*Xb}HNO3={Xa+Xb}Cu(NO3)2+{-4*Xa+2*Xb}NO2+{2*Xa}NO+{2*Xb}H2O",
        {
            "Xa": _sympy.Integer(0),
            "Xb": _sympy.Integer(0)
        },
        opt,
        printer=_public_printer.PRINTER_TEXT
    ))
except _public_exception.SubstitutionErrorWrapper as err:
    print("Error: \"%s\"." % str(err))
```

The output of "Example 2" is:

```
Error: "Side(s) eliminated.".
```

Databases (bce.public.database)
-------------

Currently, we bundled following database(s) into the program:

| Name                          | Description                    |
|-------------------------------|--------------------------------|
| BUNDLED_ABBREVIATION_DATABASE | The default abbreviations map. |
