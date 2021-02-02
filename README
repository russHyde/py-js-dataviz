Working through "Data visualization with Python and JavaScript" by Kyran Dale

Doing this in Python3 with modern JavaScript libraries (eg, lodash instead of
underscore); rather than the tools recommended in the book.

Use conda env "pyjsviz"

Libraries / tools:

- [d3.js / jQuery / lodash] from a CDN:
    - `<script src="https://d3js.org/d3.v6.min.js"></script>`
    - `<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>`
    - `<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js"><\script>`
- [sqlite3] is already installed
- [mongodb] [TODO] can be installed via conda or as a docker container
- [ipython / jupyter] installed via conda (ipython7, jupyter-4.7)
- [pandas] 1.2.1 installed via conda
- [numpy] 1.19.5 installed via conda
- [npm] installed from apt: `sudo apt install npm`
- [eslint] installed from npm: `npm install eslint --save-dev` (for linting
  javascript files; this failed due to an error with npm; nodejs v4.5.2 was
  installed and was too early a version for eslint); therefore removed npm and
  eslint

# New things I learned

## Chapter 2

- CHROME: Ctrl-Shift-J to open the console
- PY: `python -m http.server <PORT>` to start a lightweight http server locally
  (the book uses the python2 equivalent: SimpleHTTPServer)
- JUPYTER: `jupyter qtconsole` to open a lightweight jupyter/ipython shell in
  qt
- JS `var`: variables declared outside of functions or missing the 'var'
  keyword are global (so may leach into other JS scripts)
- JS `use strict`: catches some typical JS errors
- PY: recommend using `logging` module instead of using `print`
- JS: variables are processed before other code, so declare variables at the
  top of each function
- JS: strings are UCS-2
- JS: only one numeric type - 64 bit doubles (with 'type'='number')
- JS: var x = {abc: 123}; here 'x' is a JS object (not a dict/hashmap)
- JS: can access elements of an object using either dot or key-string (x.abc
  === x["abc"])
- JS: two ways to define a function:
    - [function]  `function f(param){};`
    - [functionexpression]  `var f = function(param){};`
- JS: no default vals for function params in the parameter list (overwrite if
  undefined to achieve this) [js < ECMASCRIPT6]
- JS: no base method for iterating over k/v pairs in JS objects, use
  lodash/underscore instead
- JS: `this` == implicit reference to the 'calling context' of the function
- JS: `lodash` should be sourced (in index.html) before any `*.js` scripts that
  use it
- HTML: to add inline javascript to an .html file: <script>some_javascript;</script>
- HTML: to run code asynchronously: <script type="XYZ" src="some/path" async></script>
   but note that the order of console.logs (etc) will not be predictable
- JS: use `_.map(xs, "key")` instead of `_.pluck(xs, "key")` to pull out by
  keys from each entry in an array (pluck was removed in v4.0.0 of lodash)
- JS: use closures to allow for private variables
- JS: can also define public/private methods by returning a public api
- PY: use 'nonlocal' to define closures in python (but don't, just don't)
