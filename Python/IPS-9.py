'''
You are given few sentences. You sequence of tasks is as follows:

First, remove all the special characters and change it to a full stop. This does not apply to already existing full stops.

Next, change all the uppercase letter with a lowercase letter.

After that, find the number of characters occurring contiguously for two times(e.g. rr, ll, mm) and print them along with their count of occurrences.

Input Format:

Take the sentences in English in a contiguous manner line by line.

Output Format:

In each line print the characters occurring contiguously for two times.

Print the total count of such occurrences.

Sample Input 1:

Surat-Based Sweet Shop Introduces 'Gold' Sweet @ Rs. 9,000/kg. As per a report in ANI, this sweet was launched ahead of Chandi Padvo, a Gujarati festival that falls a day after Sharad Purnima.

//It will change to:

surat.based sweet shop introduces .gold. sweet . rs. 9000.kg. as per a report in ani. this sweet was launched ahead of chandi padvo. a gujarati festival that falls a day after sharad purnima.

Sample Output 1:

ee

ee

ee

ll

4
oo

oo

ll

rr

aa

bb

6
'''
#Code Author : Pranav Viswanathan
inputString = input()
for character in inputString:
    if character.isalpha() == False and character.isnumeric() == False and character != ' ':
        inputString = inputString.replace(character, '.')
inputString = inputString.lower()
listOfWords = inputString.split(' ')
for word in listOfWords:
    i = 0
    while i < len(word)-1:
        if (word[i] == word[i + 1]) and word[i].isnumeric() == False: 
            print(word[i] + word[i + 1])
            cnt = cnt + 1
            i=i + 1
        i=i + 1
print(cnt)
