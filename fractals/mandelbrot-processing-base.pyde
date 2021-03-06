//https://www.youtube.com/watch?v=fb2T8KGG_Zg

size(360, 360); 
smooth();
frameRate(60);
 
float z = 0; 
int n = 0; 
int h = 100;
int s = 100;
int v = 100;
float a = 0;
float b2 = 0; //new b
float a2 = 0; //new a
float b3 = 0; //original b
float a3 = 0; //original a
int bright = 255; 
float zoom = 5;
int xoff = -1.5;
float speedup = 0;
float speedTarget = 2;
 
//f(z) = z^2 + c
//a^2-b^2 + 2abi
 
void setup() {  // this is run once.   
    background(200,100,100);
    colorMode(HSB, 100);
} 
 
void draw() {
    zoom = zoom/((speedup/100)+1); 
    speedup = ((speedup*10)+speedTarget)/11
    loadPixels();
    for(int i=0; i<width; i++){
        for(int j=0; j<height; j++){
            a = map(i,0,width,-zoom+xoff,zoom+xoff); 
            b = map(j,0,height,-zoom,zoom);
            
            n = 0; 
            z = 0;
            
            a3 = a;
            b3 = b;
            
            while(n < 100){
                a2 = (a*a) - (b*b); 
                b2 = 2*a*b; 
                a = a2 + a3; 
                b = b2 + b3; 
                if(abs(a2 + b2) > 16){
                    break; 
                }
                n++; 
            }
            
            bright = map(n,0,100,0,1); 
            bright = map((sqrt(bright)+(bright*20))/21,0,1,0,255); 
            if(n == 100){
                bright = 0; 
            }
            
            h = bright;
            s = 250-bright;
            v = bright;
            pixels[i + (j*width)] = color(h,s,v); 
        }
    }
    updatePixels();
    //noloop(); 
}
