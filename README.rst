Keedi, keyboard usage stats for words
-------------------------------------

Keedi quantifies how words are typed on a keyboard. People type and text a lot
these days. Wouldn't it be interesting to know about which words are most
difficult to type?

.. image:: http://i.imgur.com/QYky3GU.png
    :alt: Google Keyboard layout
    :height: 450
    :width: 200
    :align: center

.. code-block:: bash

    $ keedi --word easier
    #total distance    distance per letter    word
     397.75204731      79.550409462           easier

The scope right now of Keedi is focused on texting, specifically with
`Swype-like phone keyboards <http://www.swype.com/>`_. A Swype-like keyboard is
special because the letters of a word are progressively traced over the keyboard
in a continuous line by the typist.

The first goal of Keedi is to quantify the "distance" of words. Two
important metrics can be produced for a word:

* **word distance**: the length of the line a typist traces while typing a word
* **word distance rate**: word distance divided by the number of letters in a word

Keyboards
=========

The concept of distance to Keedi corresponds to the pixel coordinate systems
of an image of a particular keyboard. To define a keyboard, a path to an
image is specified as well as some coordinate data about some keys. Keedi 
comes built-in with the Google Keyboard.


Keedi defines a base unit as the distance between the centers of two 
left/right adjacent keys. Think the distance between `Q` and `W`, for example.
This distance is outputted by Keedi to express distance proportional to
the size of the keyboard.

Usage
=====

Let's take a look at some output!

.. code-block:: bash

    $ keedi --help
    ...

    $ keedi --word hello
    319.105810046	79.7764525114	hello

    $ tr '[:upper:]' '[:lower:]' </usr/share/dict/words | sort | uniq | keedi
    388.41331115	77.6826622299	aachen
    586.975785168	97.829297528	aaliyah
    483.160865148	69.0229807355	aardvark
    ...
    471.527348609	78.5878914349	zygotes
    343.306077333	68.6612154666	zyrtec
    693.449859231	99.0642656044	zyuganov


*The last command reads a line-separated file of words, transforms
everything to lowercase, sorts, and dedupes for efficiency,
and then feeds it into Keedi on standard input.*

To keep things simple, Keedi only recognizes words made up of the 26 letters
in the English alphabet, case-insensitive.

Installation
============

.. code-block:: bash

    $ git clone https://github.com/t-mart/keedi.git

    $ pip install --editable keedi
    

Plans
=====

In the future, there may be some additional features of Keedi:

* More metrics such as:
    * the diversity in angles used to type the letters in a word
    * which words have similar trace shapes (and are therefore difficult to determine with tracing!)
* Visualizations