import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01
adwentures_of_tom_sawer1= adwentures_of_tom_sawer.replace("\n", " ")
print(f"Result: {adwentures_of_tom_sawer1}")

# task 02
adwentures_of_tom_sawer2 = adwentures_of_tom_sawer1.replace("....", " ")
print(f"Result after replaced dots: {adwentures_of_tom_sawer2}")

# task 03
adwentures_of_tom_sawer3 = re.sub(r'\s+', ' ', adwentures_of_tom_sawer2).strip()
print(f"Result with correct spaces: {adwentures_of_tom_sawer3}")

# task 04
character_counter = 0
for character in adwentures_of_tom_sawer:
    if character == "h" or character == "H":
        character_counter += 1
print(f" Total count of letter 'h' is: {character_counter}")

# task 05
upper_word_counter = 0
for word in adwentures_of_tom_sawer.split():
    if word[0].isupper():
        upper_word_counter += 1
print(f" Words started with upper case: {upper_word_counter}")

# task 06
first_time = adwentures_of_tom_sawer.find("Tom")
second_time = adwentures_of_tom_sawer.find("Tom", first_time + 1)
print(f"Position is: {second_time}")

# task 07
adwentures_of_tom_sawer_sentences = re.split(r'[.!?][\"\'”’]*\s*', adwentures_of_tom_sawer3)
adwentures_of_tom_sawer_sentences = [s.strip() for s in adwentures_of_tom_sawer_sentences if s.strip()]
print(f"Saved: {adwentures_of_tom_sawer_sentences}")

# task 08
fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(f"Fourth sentence is: {fourth_sentence}")

# task 09
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print(f"Found: {sentence}")

# task 10
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print(f"Words in the last sentence: {word_count}")