# recursive-dict lib

![fluxo de trabalho de exemplo](https://github.com/davidmorosini/recursive_dict/actions/workflows/qas.yml/badge.svg)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=bugs)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=code_smells)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=alert_status)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=coverage)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=security_rating)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)

This library is a simple way to work with complex python dictionaries. The resources in your dictionary can be obtained through accesses indexed in the structure, we can then imagine these accesses as an operating system path. For example the resource `/home/usr/user/Documents/file.txt`.

```python
dict_ = {
    "simple_key": "simple_value",
    "array": [1, 2, 3, 4],
    "dict": {
        "foo": "bar",
        "vect": ["a", 1],
        "sub": {
            "foo": "bar"
        }
    },
    "complex": [
        "value",
        245,
        {
            "sub_vect": [{"foo": "bar"}]
        }
    ],
    "56": 34
}
```

For example, the access:

```python
dict_["dict"]["sub"]["foo"]
# Returns the value "bar"
```

Think of this access as a path, we get `/dict/sub/foo`. **What about array indices? Is this a path?** No, but we can use it anyway because arrays also support indexed access.

```python
dict_["complex"][2]["sub_vect"][0]["foo"]
# Returns the value "bar"
```

We can translate this for `complex/2/sub_vect/0/foo`

:warning: In cases like the last key (`"56": 34`) we need to use a especial character to identify the number with dictionary key and don't like a array index. We use in this case `'`, for example `/'56'`.

---

## Resources

```python
from rdict import Rdict as rd

rd_ = rd(dict_, sep="/", use_copy=True)
```

### get

```python
rd_.get("complex/2/sub_vect/0/foo")
# Returns the value "bar"
```

With default value, if the path don't exists the function returns default value.

```python
rd_.get("this/path/do/not/exists", default="bar")
# Returns the default value "bar"
```

If you need an exception will be raised, use flag the `raise_error`. The type of exception is the same one thrown if you try to access the indexes normally in the original dictionary.

```python
rd_.get("this/path/do/not/exists", default="bar", raise_error=True)
# Raise "KeyError: 'this'"
```
