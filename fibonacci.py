#import sys
#sys.stdin = open('input.in','r')

mod=1000000007

def powFinder(n):#Find lowest power index of 2 just above the number
	if(n==0):
		return -1
	i=0
	while(2**i<=n):
		i+=1
	return i

def multiplier(n):#Convert the number into multiplications of powers of 2
	multiplier=[]
	i=powFinder(n)-1
	while(i>=0):
		n-=2**i
		multiplier.append(i)
		i=powFinder(n)-1
	return multiplier

def sqMat(matrix):#Square a matrix
	global mod
	matrix2=[[1,1],[1,1]]
	for i in range(2):
		matrix2[0][0]=((matrix[0][0]*matrix[0][0])%mod+(matrix[0][1]*matrix[1][0])%mod)%mod
		matrix2[0][1]=((matrix[0][0]*matrix[0][1])%mod+(matrix[0][1]*matrix[1][1])%mod)%mod
		matrix2[1][0]=((matrix[1][0]*matrix[0][0])%mod+(matrix[1][1]*matrix[1][0])%mod)%mod
		matrix2[1][1]=((matrix[1][0]*matrix[0][1])%mod+(matrix[1][1]*matrix[1][1])%mod)%mod
	return matrix2

def matMul(matrix,matrix2):#Multiply 2 matrices
	matrix3=[[1,1],[1,1]]
	matrix3[0][0]=((matrix[0][0]*matrix2[0][0])%mod+(matrix[0][1]*matrix2[1][0])%mod)%mod
	matrix3[0][1]=((matrix[0][0]*matrix2[0][1])%mod+(matrix[0][1]*matrix2[1][1])%mod)%mod
	matrix3[1][0]=((matrix[1][0]*matrix2[0][0])%mod+(matrix[1][1]*matrix2[1][0])%mod)%mod
	matrix3[1][1]=((matrix[1][0]*matrix2[0][1])%mod+(matrix[1][1]*matrix2[1][1])%mod)%mod
	return matrix3

def matrixPow(matrix,multiplier):#Raise the matrix to a power
	remaining=[]
	for item in multiplier:
		matrix2=matrix[:]
		for i in range(0,item+1):
			if(i==0):
				pass
			else:
				matrix2=sqMat(matrix2)
		remaining.append(matrix2)
	return remaining

def intMatrixMul(remaining):#Multiplications of matrices resulted from raising qMat to powers of 2
	matrix=[[1,1],[1,1]]
	for item in remaining:
		matrix=matMul(item,matrix)
	return matrix

def main():
	qMat=[[1,1],[1,0]]
	for i in range(int(input())):
		n=int(input())
		powMultiplier=multiplier(n)
		remaining=matrixPow(qMat,powMultiplier)
		ans=intMatrixMul(remaining)
		print(ans[0][0])


if __name__ == '__main__':
	main()