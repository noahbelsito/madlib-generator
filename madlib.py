class MadLib:
    story = []
    inputs = []
    required = []


piranha_river = MadLib()
piranha_river.story = "If you are traveling in %s and find yourself having to cross a piranha-filled river, " \
                      "here's how to do it %s: Piranhas are more %s during the day, so cross the river at night. " \
                      "Avoid areas with netted %s traps - piranhas may be %s there looking to %s them! When %s the " \
                      "river, swim %s. You don't want to wake them up and make them %s! Whatever you do, if you have " \
                      "an open wound, try to find another way to get back to the %s. Piranhas are attracted to fresh, " \
                      "%s and will most likely take a bite out of your %s if you %s in the water! "
piranha_river.required = ["foreign country", "adverb", "adjective", "animal", "verb ending in -ing",
                          "verb", "verb ending in -ing", "adverb", "adjective", "place",
                          "type of liquid", "part of the body", "verb"]
