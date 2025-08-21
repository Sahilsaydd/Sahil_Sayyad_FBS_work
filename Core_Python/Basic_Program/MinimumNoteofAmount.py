num = int(input("Enter a Amount :"))
note_2000 = num //2000
num = num%2000
print(f"Number of 2000 notes : {note_2000}")
note_500 = num //500
num = num%500
print(f"Number of 500 notes : {note_500}")

note_200 = num//200
num=num%200
print(f"Number of 200 notes : {note_200}")