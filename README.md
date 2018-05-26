# Slides

##### A thing I made for a single chemistry presentation

So I didn't feel like using OpenOffice, and thought my website looked slide-ish enough, so I turned it into this, and here we are.

Here's how it works:
```
# This is an example slide

~~~

# This is a second slide

- Here is a bullet point
- Here is another one
	- An inner bullet point

~~~

# Third slide

1. Ordered list
<i>random HTML can be put here</i>
```

Then just
```
$ python3 slides.py infile.md outfile.html