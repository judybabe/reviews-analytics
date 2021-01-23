data = []
count = 0
total = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
for length in data:
	total += len(length)
	print(total)

total = total/len(data)
print('留言平均長度為： ', total, '字')
print('檔案讀取完了, 總共有', len(data), '筆資料')

