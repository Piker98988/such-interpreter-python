# The Such. specification

_Such._ is composed of [headers](#headers) and [definitions](#definitions).
For clear-like-water explanations, I will compare it to JSON.

## General overview

_Such._ is a language which embraces type annotations. Everything is type safe when working with _Such._ 
This makes it a language worth giving a try, because it revolutionizes this aspect by making stored data type-safe.

This language has a heavy reliance on semicolons. 
Semicolons define the end of a [Statement](#statements), which can be a [Header](#statements) or a [Definition](#definitions).
This makes *Such.* a **very explicit** language.

## Root

The root object in any JSON file may either be none, a keymap or a vector. In *Such.* this root
object is always a keymap, and is defined by the language. Any such file starts with

## Comments

Comments in such are defined by two types, commonly reffered as:

- [Single line comments](#single-line-comments)
- [Multi line comments](#multi-line-comments)

### Single line comments

To create a single line comment in _Such._, you would use the double slash (`//`):

````such
RELH{BOO/STR/NU?/INT} employee0; // This employee is the first (obviously)
      STR id = "6eae573f-7be8-4b11-a0f7-e56793a25472"; // Unique UUID4
      STR name = "Julie Patrick"; // Full name
      STR email = "sheajessica@example.org";
      STR address = "68099 Joseph Dam Suite 024\nSouth Maryside, MH 82474"; // Full adress
      STR phone_number = "630-688-3830"; 
      STR job = "Passenger transport manager";
      STR company = "Torres, Murphy and Wright";
      STR birthdate = "2024-12-26";
      STR created_at = "2024-02-17T08:29:13";
      BOO is_active = false; // Whether our user is active on a weekly basis
      INT age = 60; // That's actually a pretty high number
      NU? car = none; // No one has a car
 // Another comment, just if you didn't know how to use them
````

### Multi-line comments

These comments are defined with an HTML-like syntax, they can be multiple lines long, and contain anything:

````such
RELH{BOO/STR/NU?/INT} employee0;
   STR id = "a7d33531-3038-4642-8151-96227eb3304c";
   STR name = "Patrick Greene";
   STR email = "jmiller@example.org";
   STR address = "42866 Arias Club Suite 283\nPort Robin, NH 23996";
   STR phone_number = "638-494-1154x1977";
   STR job = "Geochemist";
   STR company = "Walker LLC";
   STR birthdate = "1943-01-14"; <!--
   STR created_at = "2020-05-17T10:25:19";
   BOO is_active = true; this entire section
   INT age = 42; is commented, it will be ommited by Such.
   NU? car = none; -->
<!-- 
A multi
line
comment
asdjhafjhadkjf
JDSHLaksLKJHFL
FKHalsjflkasjflKF
sfjfLKFLKhflkjDF
-->
````

## Statements

Statements are the building blocks of _Such._ they represent either a definition or a header, which has child objects.
This statements start with a type, and ended with a semicolon. They can be either of two:

- [Headers](#headers)
- [Definitions](#definitions)

### Definitions

Definitions are the most important statements in *Such.* these define "properties" as commonly known or more like
**variables.** To make a definition, we have several attributes to fill:

- Type - The type of our variable, this will be checked when parsing your *Such.* files. This types can only be on upper case.
  - ``NU?``  -  The `null` type. This is a special one, because a null typed variable will only be able to store one type: `null`.
  - ``INT``  -  The integer type. This type houses any natural number (yet).
  - ``BOO``  -  Boolean type. Houses two values: `true` or `false`.
  - ``STR``  -  String type. Any string of text surrounded by single (`'`) or double (`"`) quotes.
- Reference  -  The name of the definition, how will it will be referred as when parsing
- Value  -  The value which the definition will store, according to the type.

> [!TIP]
> The ``NU?`` type can house three values: 
> - Empty string, either with single or double quotes
> - ``none`` literal
> - ``null`` literal
> 
> Even though they may be written different, they all represent the same, the abscence of a value.
<!--
TODO: Add the actual Integer type. It only houses Natural numbers (yet) 
-->

Each of those fields will determine how the definition is interpreted. To actually create a definition, we have to arrange the fields in
a variable-declaration style, like this:

````such
TYPE reference = value; 
````

So, to make our first definition, we can make something like this:

````such
INT definition1 = 22;
````

And so, that code would translate to JSON as:

````json
{
  "definition1": 22
}
````

### Headers

Headers are what define an "object" in JSON. These house information in a key: value style
or in a more vectorial approach with arrays. Headers when opened by a statement will not be closed until
a new header of the same or superior level is closed. To define header
Headers are defined by:

- Main type: This type will define the header and how it treats the data inside it.
  - ``RELH`` - Relational header, with a key: value style
  - ``VECH`` - Vectorial header, with anonymous children 
- Subtype(s): The type(s) for the header's element(s), separated by slash (`/`)
  - ``INT`` - Any natural number (yet)
  - ``STR`` - A string of characters enclosed by double quotes (`"`) or single quotes (`'`)
  - ``BOO`` - A boolean type, either `true` or `false`.
  - ``NU?`` - Null type, represents the abscence of a value and is defined by several expressions
    - ``none`` like Python's syntax
    - ``null`` like JSON
    - ``""`` or ``''`` as an empty string
  - ``RELH``  -  In case it has a header child
  - ``VECH``  -  The same goes
- Name: this is the name of the header or its reference.
  - In case it is a nested header, the parent name will be indicated by a double colon:`` parent_header::child_header``

> [!IMPORTANT]
> Vectorial headers have not yet been fully implemented into _Such._ expect errors.

> [!WARNING]
> When using subtypes for headers, if one of the subtypes is a header type, be it either ``RELH`` or ``VECH``, 
> it **ALWAYS** has to go first, no matter what: 
> ``RELH{RELH/INT} header_with_child_header;``

Given that information, we can define our first header:

```such
RELH{INT/STR} header1;
```

And if we wanted it to contain more headers inside, we would change the subtype to ``RELH``:

```such
RELH{RELH/INT/STR} header1;
```

So, let's make a child of that header1:

```such
RELH{RELH/INT/STR} header1;
   RELH{BOO/STR} header1::header1_1;
```

Then, every [definition](#definition) that is done before the first header is a child of the ``root``:

```such
INT foo = 2; // This is part of the root
RELH{INT} header1; // This is part of the root too
    INT bar = 3; // This is now part of header1
```

and so, that *Such.* code would translate into JSON to: (without the comments)

````json
{ // This is the root
  "foo": 2, // Part of the root too
  "header1": { 
    "bar": 3 // Part of header1
  }
}
````