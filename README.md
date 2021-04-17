# recursive dict lib

![fluxo de trabalho de exemplo](https://github.com/davidmorosini/recursive_dict/actions/workflows/workflow.yml/badge.svg)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=bugs)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=code_smells)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=alert_status)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=coverage)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=davidmorosini_recursive_dict&metric=security_rating)](https://sonarcloud.io/dashboard?id=davidmorosini_recursive_dict)

A simple library for working with complex data structures (`dict`) in python. The operations are based on the organization of directories of an operating system, or simply as a tree using recursive algorithms to maintain the performance of indexed accesses.

- Only built in python libraries are used

## Overview

Imagine that a json structure is an OS path, so we can mount a resource path like any directory on your computer.

Example

```json
{
    "key_1": [1, 2],
    "key_2": {
        "key_3": {
            "key_4": {
                "key_5": 4,
                "key_6": 7
            },
            "key_7": [
                {
                    "key_index_0": true
                },
                {
                    "key_index_1": false
                },
                {
                    "key_index_2": true
                }
            ]
        }
    }
}
```

To access the `key_7` resource, we can then use the following path

```sh
key_2/key_3/key_7
```

To access the `key_5` resource, we can then use the following path

```sh
key_2/key_3/key_4/key_5
```

To support arrays within structures, we can use the element's own index value to compose the path

To access the `key_index_1` resource, we can then use the following path

```sh
key_2/key_3/key_7/1/key_index_1
```

## Dict Class

```python
from recursive_dict import Dict
```

### Objects

- `_dict` [dict or list]

    Internal data structure

- `_sep` [str]

    Path separator, default is `"/"`

- `_use_copy` [bool]

    Flag that indicates whether the class should use a copy of the passed structure or use from the structure reference itself, default is `True`