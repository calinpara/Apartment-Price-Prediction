import joblib
from sklearn.preprocessing import LabelEncoder

lbl_encoder = joblib.load('dict_label.pkl')


lst = [3, 432, 17, 1, 23, 1, 18, 0, 0]




				# ^  ^  	  ^   ^  ^  ^


# def function(param):

# def numberGenerator(n):
#      number = 0
#      while number < n:
#          yield number
#          number += 1

# g = numberGenerator(10)


# counter = 0
# while counter <= len(new_lst):
# 	print(next(g))
# 	counter += 1


new_lst = [lst[indx] for indx in range(2, len(lst))]
new_lst.pop(2)

print(new_lst)

 
indx = 0

for value in lbl_encoder.values():
	print(value, indx)
	print(value.inverse_transform([new_lst[indx]]))
	indx += 1
	


			

		# new_lst = [(item, list(value.classes_).index(item))  for item in (list(value.classes_))]
		

				
		

		# for item_2 in new_lst:
		# 	print(item_2)
