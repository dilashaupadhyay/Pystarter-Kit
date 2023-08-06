def madlibs_story():
    # The Madlibs template with placeholders for user inputs
    template = "Once upon a time, in a {adjective} kingdom, there was a {noun}. " \
               "It had {number} {plural_noun} and a {adjective2} {animal}. " \
               "One day, the {noun} decided to go on a journey to find {adjective3} {plural_noun2}. " \
               "On the way, it met a {adjective4} fairy who granted it {number2} wishes. " \
               "The {noun} was overjoyed and used its wishes wisely. " \
               "Finally, after a long adventure, the {noun} returned to its kingdom as a hero."

    # Collecting user inputs for the placeholders
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    number = input("Enter a number: ")
    plural_noun = input("Enter a plural noun: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    adjective3 = input("Enter one more adjective: ")
    plural_noun2 = input("Enter another plural noun: ")
    adjective4 = input("Enter the last adjective: ")
    number2 = input("Enter another number: ")

    # Filling the template with user inputs
    story = template.format(
        adjective=adjective,
        noun=noun,
        number=number,
        plural_noun=plural_noun,
        adjective2=adjective2,
        animal=animal,
        adjective3=adjective3,
        plural_noun2=plural_noun2,
        adjective4=adjective4,
        number2=number2
    )

    return story


if __name__ == "__main__":
    print("Welcome to the Madlibs Story Generator!")
    story = madlibs_story()
    print("\nYour Madlibs Story:\n")
    print(story)
