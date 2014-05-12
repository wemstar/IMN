#include <stdio.h>
#include <math.h>

void dokladne(float Vx,float Vy,float t,float g,float &x,float& y)
{
	x=Vx*t;
	y=Vy*t-g*t*t/2.0;
}
float energia(float Vx,float Vy,float y,float m,float g)
{
	return m*(pow(Vx,2)+pow(Vy,2))/2.0+m*g*y;
}

void jawnaEulera(float x0,float y0,float V0,float alpha,float dt,float Fx,float Fy,float m)
{
	float Vx0=V0*cos(alpha),Vy0=V0*sin(alpha);
	float E=0;
	float x=x0,y=y0+0.000000000001,Vx=Vx0,Vy=Vy0,t=0,dokX,dokY;	
	FILE* fp=fopen("jawnaEualera1.txt","w");
	while(y>0)
	{
		
		x=x+dt*Vx;
		y=y+dt*Vy;
		Vx=Vx+dt*Fx/m;
		Vy=Vy+dt*Fy/m;		
		t+=dt;
		dokladne(Vx0,Vy0,t,-Fy,dokX,dokY);
		E=energia(Vx,Vy,y,m,-Fy);
		fprintf(fp, "%f %f %f %f %f %f %f %f\n",x,y,Vx,Vy,dokX,dokY,t,E);

	}
	fclose(fp);
}
void RK2(float& x0,float y0,float V0,float alpha,float dt,float Fx,float Fy,float m,float& t)
{
	float Vx0=V0*cos(alpha),Vy0=V0*sin(alpha);
	float E=0;
	float x=x0,y=y0+0.000000000001,Vx=Vx0,Vy=Vy0,dokX,dokY;	
	FILE* fp=fopen("RK2.txt","w");
	while(y>0)
	{
		float K1vx=Fx;
		float K1vy=Fy;
		float K1x=Vx;
		float K1y=Vy;

		float K2vx=Fx;
		float K2vy=Fy;
		float K2x=Vx+K1vx*dt;
		float K2y=Vy+K1vy*dt;

		x=x+dt/2.0*(K1x+K2x);
		y=y+dt/2.0*(K1y+K2y);

		Vx=Vx+dt/2.0*(K1vx+K2vx);
		Vy=Vy+dt/2.0*(K1vy+K2vy);
		t+=dt;
		dokladne(Vx0,Vy0,t,-Fy,dokX,dokY);
		E=energia(Vx,Vy,y,m,-Fy);
		fprintf(fp, "%f %f %f %f %f %f %f %f\n",x,y,Vx,Vy,dokX,dokY,t,E);

	}
	x0=x;
	fclose(fp);
}

void RK2Opory(float& x0,float y0,float V0,float alpha,float dt,float Fx,float Fy,float m,float& t)
{
	float Vx0=V0*cos(alpha),Vy0=V0*sin(alpha);
	float E=0;
	float x=x0,y=y0+0.000000000001,Vx=Vx0,Vy=Vy0,dokX,dokY;	
	FILE* fp=fopen("RK2Opory.txt","w");
	while(y>0)
	{
		dokladne(Vx0,Vy0,t,-Fy,dokX,dokY);
		E=energia(Vx,Vy,y,m,-Fy);
		fprintf(fp, "%f %f %f %f %f %f %f %f\n",x,y,Vx,Vy,dokX,dokY,t,E);

		float K1vx=Fx-0.85*pow(0.1,2)*sqrt(pow(Vx,2)+pow(Vy,2))*Vx;
		float K1vy=Fy-0.85*pow(0.1,2)*sqrt(pow(Vy,2)+pow(Vx,2))*Vy;
		float K1x=Vx;
		float K1y=Vy;

		float K2vx=Fx;
		float K2vy=Fy;
		float K2x=Vx+K1vx*dt;
		float K2y=Vy+K1vy*dt;

		x=x+dt/2.0*(K1x+K2x);
		y=y+dt/2.0*(K1y+K2y);

		Vx=Vx+dt/2.0*(K1vx+K2vx);
		Vy=Vy+dt/2.0*(K1vy+K2vy);
		t+=dt;
		

	}
	x0=x;
	fclose(fp);
}
void zasieg(float alpha0,float alpha1,float dalpha)
{
	FILE *fp=fopen("Zasieg.txt","w");
	float x, t,alpha=alpha0;
	while(alpha<alpha1)
	{
		x=0.0;
		t=0.0;
		RK2(x,0,20,alpha,0.001,0,-9.98,1,t);
		fprintf(fp, "%f %f %f\n",alpha,x,t );
		alpha+=dalpha;
	}
	fclose(fp);
}

void zasieg2(float alpha0,float alpha1,float dalpha)
{
	FILE *fp=fopen("Zasieg2.txt","w");
	float x, t,alpha=alpha0;
	while(alpha<alpha1)
	{
		x=0.0;
		t=0.0;
		RK2Opory(x,0,200,alpha,0.001,0,-9.98,1,t);
		fprintf(fp, "%f %f %f\n",alpha,x,t );
		alpha+=dalpha;
	}
	fclose(fp);
}
void zasieg4()
{
	FILE *fp=fopen("Zasieg4.txt","w");
	float x, t,alpha=atan(1);
	for(int i=1;i<=4;i++)
	{
		x=0.0;
		t=0.0;
		RK2Opory(x,0,200,alpha,pow(0.1,i),0,-9.98,1,t);
		fprintf(fp, "%f %f %f\n",pow(0.1,i),x,t );

	}
	fclose(fp);

}

int main(int argc, char const *argv[])
{
	float x, t;
	x=0.0;
	t=0.0;
	zasieg(0.0,atan(1)*2,atan(1)/25.0);
	zasieg2(0.0,atan(1)*2,atan(1)/25.0);
	jawnaEulera(0,0,20,atan(1),0.25,0,-9.98,1);
	RK2(x,0,20,atan(1),0.25,0,-9.98,1,t);
	x=0.0;
	t=0.0;
	zasieg4();
	RK2Opory(x,0,200,atan(1),0.25,0,-9.98,1,t);
	
	
	return 0;
}