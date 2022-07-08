class PartyAnimal:
    x = 0
    some_text = 'just some text'

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def Heitor(self):
        print('Heitor is the most handsome animal in the world')

    def count_to(self, num):
        count = 1
        while count <= num:
            print(count)
            count += 1

PartyAnimal().party()
animal = PartyAnimal()
print(animal.x)
print(animal.some_text)
animal.Heitor()
animal.count_to(20)

print('#############################################')

count = 0
while count < 5:
    count += 1
    animal.party()

print('#############################################')

print(type(PartyAnimal))

print('#############################################')

print(dir(PartyAnimal)) # dir(element) shows the capabilities of an element
