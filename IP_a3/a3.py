import numpy as np
import matplotlib.pyplot as plt

class Shape:

	def __init__(self):
		self.T_s = None
		self.T_r = None
		self.T_t = None
	
	
	def translate(self, dx, dy):

		self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

	def scale(self, sx, sy):

		self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
		
	def rotate(self, deg):

		rad = deg*(np.pi/180)
		self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

		
	def plot(self, x_dim, y_dim):
		x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
		plt.plot((-x_dim, x_dim),[0,0],'k-')
		plt.plot([0,0],(-y_dim, y_dim),'k-')
		plt.xlim(-x_dim,x_dim)
		plt.ylim(-y_dim,y_dim)
		plt.grid()
		plt.show()

class Polygon(Shape):
	def __init__(self, A):
		self.polygon=A.transpose()
		self.og_polygon=self.polygon.copy()

	def translate(self, dx, dy):
		self.og_polygon=self.polygon.copy()
		super().translate(dx,dy)
		self.polygon = np.round(np.dot(self.T_t,self.polygon),2)
		rx=[]
		ry=[]
		rx.extend(self.polygon[0])
		ry.extend(self.polygon[1])
		return ((rx,ry))
	
	def scale(self, sx, sy):
		self.og_polygon=self.polygon.copy()
		super().scale(sx,sy)
		cx=sum(self.polygon[0])
		cy=sum(self.polygon[1])
		cx=cx/len(self.polygon[0])
		cy=cy/len(self.polygon[1])
		self.polygon[0]-=cx
		self.polygon[1]-=cy
		self.polygon = np.dot(self.T_s,self.polygon)
		self.polygon[0]+=cx
		self.polygon[1]+=cy
		rx=[]
		ry=[]
		rx.extend(np.round(self.polygon[0],2))
		ry.extend(np.round(self.polygon[1],2))
		return ((rx,ry))
 
	def rotate(self, deg, rx = 0, ry = 0):
		self.og_polygon=self.polygon.copy()     
		super().rotate(deg)
		if rx != 0 or ry != 0:
			self.translate(-rx,-ry)
			self.polygon = np.round(np.dot(self.T_r,self.polygon),2)
			self.translate(rx,ry)
			rx=[]
			ry=[]
			rx.extend(self.polygon[0])
			ry.extend(self.polygon[1])
			return ((rx,ry))            

		self.polygon = np.round(np.dot(self.T_r,self.polygon),2)
		rx=[]
		ry=[]
		rx.extend(self.polygon[0])
		ry.extend(self.polygon[1])
		return ((rx,ry))
	def plot(self):
		nc1=np.array([self.polygon[:,0]])
		nc2=np.array([self.og_polygon[:,0]])
		og=np.append(self.og_polygon, nc2.T,axis=1)
		nm=np.append(self.polygon, nc1.T,axis=1)
		plt.plot(og[0],og[1],'--')
		plt.plot(nm[0],nm[1])
		plt.axis("scaled")
		x_dim=max(max(self.polygon[0]),max(self.og_polygon[0]))
		y_dim=max(max(self.polygon[1]),max(self.og_polygon[1]))
		Shape.plot(self,x_dim,y_dim)

class Circle(Shape):

	def __init__(self, x=0, y=0, radius=5):
		self.centre=np.array([[x],[y],[1]])
		self.radius=radius
		self.og_centre=self.centre.copy()
		self.og_radius=self.radius
	def translate(self, dx, dy):
		self.og_centre=self.centre.copy()
		self.og_radius=self.radius
		super().translate(dx,dy)
		self.centre=np.round(np.dot(self.T_t,self.centre),2)
		rx=self.centre[0][0]
		ry=self.centre[1][0]
		return((rx,ry,self.radius))
		
	def scale(self, sx):
		self.og_centre=self.centre.copy()
		self.og_radius=self.radius
		self.radius*=sx
		rx=self.centre[0][0]
		ry=self.centre[1][0]
		return((rx,ry,self.radius))
	
	def rotate(self, deg, rx = 0, ry = 0):
		self.og_centre=self.centre.copy()
		self.og_radius=self.radius
		super().rotate(deg)
		if rx != 0 or ry != 0:
			self.translate(-rx,-ry)
			self.centre = np.round(np.dot(self.T_r,self.centre),2)
			self.translate(rx,ry)
			rx=self.centre[0][0]
			ry=self.centre[1][0]
			return((rx,ry,self.radius))
		self.centre = np.round(np.dot(self.T_r,self.centre),2)
		rx=self.centre[0][0]
		ry=self.centre[1][0]
		return((rx,ry,self.radius))
	
	def plot(self):
		x_dim=max(float(self.og_centre[0]),float(self.centre[0]))+max(self.og_radius,self.radius)
		y_dim=max(float(self.og_centre[1]),float(self.centre[1]))+max(self.og_radius,self.radius)
		cr1=plt.Circle((float(self.og_centre[0]),float(self.og_centre[1])),self.og_radius,linestyle='--')
		cr2=plt.Circle((float(self.centre[0]),float(self.centre[1])),self.radius)      
		cr1.set_fill(False) 
		cr2.set_fill(False) 
		mp=plt.gca()
		mp.add_patch(cr1)
		mp.add_patch(cr2)
		plt.axis("scaled")
		Shape.plot(self,x_dim,y_dim)
if __name__=="__main__":
	s=Shape()
	verbose=int(input("Enter 1 to plot otherwise enter 0: "))
	N=int(input("Enter the number of test cases: "))
	for j in range(N):
		st=int(input("Enter shape type (0 for polygon and 1 for Circle): "))
		if st==0:
			ns=int(input("Enter the number of sides: "))
			A=np.empty((0,3),float)
			print("Enter the coordinates in space seperated ways:")
			for k in range(ns):
				li=list(map(float,input().split()))
				li.append(1)
				cr=np.array([li])
				A=np.append(A,cr,axis=0)
			x=Polygon(A)
			Q=int(input("Enter the number of queries for the polygon: "))
			print("The query types are:")
			print('''a) R theta (rx) (ry)-> Rotation (theta: +ve -> clockwise, -ve -> anti-clockwise) about the origin by theta degrees
b) S sx (sy) -> Scale by a factor of x along x-axis and y along y-axis
c) T dx (dy) -> Translate by dx along x-axis and dy along y-axis
d) P -> Plot the shape (along with the shape just before the previous query).''')
			for l in range(Q):
				qt=input("Enter the query: ").split()
				if qt[0].lower()=='r':
					theta=qt[1]
					if len(qt)>2:
						rx=qt[2]
						ry=qt[3]
					if len(qt)==2:
						rx=0
						ry=0
					print(Polygon.rotate(x,float(theta),float(rx),float(ry)))
					if verbose==1:
						Polygon.plot(x)
				if qt[0].lower()=='s':
					sx=float(qt[1])
					sy=float(qt[2])
					print(Polygon.scale(x,sx,sy))
					if verbose==1:
						Polygon.plot(x)
				if qt[0].lower()=='t':
					dx=float(qt[1])
					dy=float(qt[2])
					print(Polygon.translate(x,dx,dy))
					if verbose==1:
						Polygon.plot(x)
				if qt[0].lower()=='p':
					Polygon.plot(x)
		if st==1:
			vals=list(map(float,input("Enter the coordinates of the center of the circle and radius: ").split()))
			x=Circle(vals[0],vals[1],vals[2])
			Q=int(input("Enter the number of queries for the circle: "))
			print("The query types are:")
			print('''a) R theta (rx) (ry) -> Rotation (theta: +ve -> clockwise, -ve -> anti-clockwise) about the origin by theta degrees.
b) S sr -> Scale by a factor of s along all the sides
c) T dx (dy) -> Translate by dx along x-axis and dy along y-axis
d) P -> Plot the shape (along with the shape just before the previous query).''')
			for k in range(Q):
				qt=input("Enter the query: ").split()
				if qt[0].lower()=='r':
					theta=float(qt[1])
					if len(qt)>2:
						rx=qt[2]
						ry=qt[3]
					if len(qt)==2:
						rx=0
						ry=0
					print(Circle.rotate(x,theta,rx,ry))
					if verbose==1:
						Circle.plot(x)
				if qt[0].lower()=='s':
					sr=float(qt[1])
					print(Circle.scale(x,sr))
					if verbose==1:
						Circle.plot(x)
				if qt[0].lower()=='t':
					dx=float(qt[1])
					dy=float(qt[2])
					print(Circle.translate(x,dx,dy))
					if verbose==1:
						Circle.plot(x)
				if qt[0].lower()=='p':
					Circle.plot(x)














