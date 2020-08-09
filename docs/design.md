# Ulang Design

## Block declarations

All block declarations will be done with curly braces.

Ex:

```text
if/class/etc. {

}
```

## Variables

Python-style variable declaration (no `let`, `var`, `const`, etc.)

Ex:

```text
my_var = 2
```

## Functions

Similar to Python function declarations, with the key difference that there are no non-keyword arguments.

Ex:

```text
func my_cool_function(a, b, c, d) {
    // Func body here
}
```

## Classes

Similar to Python function declarations, with the difference that declaration of the parent classes list is mandatory, even if there are no parent classes. Multiple inheritance will be supported, assuming it's not technically difficult.

Ex:

```text
class MyCoolClass() {

}

class ChildClass(MyCoolClass) {

}
```
