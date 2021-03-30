import pandas as pd
import matplotlib.pyplot as plt


def main():
	data = pd.read_csv('titanic_data/train.csv')
	print(data.head(6))
	print (data.count())
	plt.figure(figsize=(14,7))
	#################################

	plt.subplot2grid((3,4), (0, 0))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar')   # normalize=True 讓數字變成百分比
	plt.title('Survived')                             # plt.title('')      給圖片+title

	plt.subplot2grid((3,4), (0, 1))
	data.Sex.value_counts(normalize=True).sort_index().plot(kind='bar',color='Aquamarine')   # .sort_index() 按照data的順序去印
	plt.title('Sex')

	plt.subplot2grid((3,4), (0, 2))
	data.Pclass.value_counts(normalize=True).sort_index().plot(kind='line')      # value_counts 讀取資料中的數字
	plt.title('Pclass')

	plt.subplot2grid((3,4), (0, 3))
	data.Embarked.value_counts(normalize=True).sort_index().plot(kind='area')
	plt.title('Embarked')

	plt.subplot2grid((3,4), (1, 0))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Men Survived')

	plt.subplot2grid((3,4), (1, 1))
	data.Survived[data.Sex == 'female'].value_counts(normalize=True).sort_index().plot(kind='bar',color='Beige')
	plt.title('Women Survived')

	plt.subplot2grid((3,4), (1, 2))
	data.Survived[data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Pclass1 Survived')

	plt.subplot2grid((3,4), (1, 3))
	data.Survived[data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Pclass3 Survived')

	plt.subplot2grid((3,4), (2, 0))
	data.Survived[(data.Sex == 'female') & (data.Pclass == 3)].value_counts(normalize=True).sort_index().plot(kind='bar',
																										  color='red')
	plt.title('Women in Pclass3 Survived')

	plt.subplot2grid((3,4), (2, 1))
	data.Survived[(data.Sex == 'female') & (data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(kind='bar',
																											  color='Olive')
	plt.title('Women in Pclass1 Survived')

	plt.subplot2grid((3, 4), (2, 2))
	data.Survived[(data.Sex == 'male') & (data.Pclass == 3)].value_counts(normalize=True).sort_index().plot(
		kind='bar',
		color='red')
	plt.title('men in Pclass3 Survived')

	plt.subplot2grid((3, 4), (2, 3))
	data.Survived[(data.Sex == 'male') & (data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(
		kind='bar',
		color='Olive')
	plt.title('men in Pclass1 Survived')

#################################
	plt.show()
	#& (data.Pclass == 3)

if __name__ == '__main__':
	main()