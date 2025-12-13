# Madlibs

# Madlibs is a simple game where you create a story template with "blanks" for words. 
# You, or another player, then construct a list of words and place them into the story, 
# creating an often silly or funny story as a result.

# Create a simple madlib program that prompts for a noun,
#  a verb, an adverb, and an adjective, and injects them into a story that you create.

# Example
# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly
# Expected Output
# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.


def prompt(user):
    print(f'==> {user}')


prompt('Enter a noun:')
noun = input()
prompt('Enter a verb:')
verb = input()
prompt('Enter an adjective:')
adjective = input()
prompt('Enter an adverb:')
adverb = input()

print(f"\nDo you {verb} the {noun}? BEFORE you {verb} the {noun},")
print(f"you must {adverb} understand the {adjective} fundamentals!")

# noun: code
# verb: refactor
# adjective: syntactic
# adverb: deeply

# Do you refactor the code? BEFORE you refactor the code,
# you must deeply understand the syntactic fundamentals!

# noun: function
# verb: debug
# adjective: elegant
# adverb: masterfully


# Do you debug the function? BEFORE you debug the function,
# you must masterfully understand the elegant fundamentals!


# noun: loop
# verb: write
# adjective: Pythonic
# adverb: carefully


# Do you write the loop? BEFORE you write the loop,
# you must carefully understand the Pythonic fundamentals!