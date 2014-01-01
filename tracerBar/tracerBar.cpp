#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int alpha_slider;
const int alpha_slider_max = 100;

/** 
 *  @function on_trackbar
 *  @brief Callback for trackbar
 */
void on_trackbar(int, void*) 
{
    cout << "alpha_slider: " << alpha_slider << endl;
    cout << "alpha_slider_max: " << alpha_slider_max << endl;
}

int main(int argc, const char *argv[])
{
    // Initialize values
    alpha_slider = 10;

    namedWindow("Linear Blend", 1);
        
    createTrackbar("TEST", "Linear Blend", &alpha_slider, alpha_slider_max,
                    on_trackbar);
    waitKey(0);    
    return 0;
}
