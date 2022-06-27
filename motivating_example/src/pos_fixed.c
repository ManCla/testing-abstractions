#include <inttypes.h>

#define n 13
#define f11 6143 /* Q2.13 correct: 8143 faulty: 6143 */
#define f21 2042 /* Q2.13 */
#define g1 919   /* Q2.13 */
#define g2 115   /* Q2.13 */
#define l1 26950 /* Q2.13 */
#define l2 14607 /* Q2.13 */
#define k1 16680 /* Q2.13 */
#define k2 10191 /* Q2.13 */
#define kv 26293 /* Q2.13 */



int16_t pos_fixed(int16_t r, int16_t y){
    static int16_t x1 = 0.0, x2 = 0.0, v = 0.0;
	int32_t u,e;
    
    u = (int16_t)(((int32_t)l2*(r-x2) - (int32_t)l1*x1) >> n) - v;
    
    if (u > 511) 
        u = 511;
    else if (u < -512) 
        u = -512;
    //writeOutput(u);
    
    e = y - x2;
    x2 = x2 + (int16_t) (((int32_t)f21*x1 + (int32_t)g2*(u+v) + (int32_t)k2*e) >> n);
    x1 = (int16_t) (((int32_t)f11*x1 + (int32_t)g1*(u+v) + (int32_t)k1*e) >> n);
    v = v + (int16_t)(((int32_t)kv*e) >> n);

	return u; //FIX ME
}