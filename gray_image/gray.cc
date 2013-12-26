#include <opencv2/core/core.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, const char *argv[])
{
    if (argc != 2) {
        cout<< "xxx" << endl;
        return -1;
    }    

    Mat image;
    image = imread(argv[1], CV_LOAD_IMAGE_COLOR);

    if (!image.data) {
        cout << "Could not open or find the image" << endl;
        return -1;
    }

    Mat gray_image;
    cvtColor(image, gray_image, CV_BGR2GRAY);
    imwrite("./gray.png", gray_image);

    namedWindow(argv[1], CV_WINDOW_AUTOSIZE);
    namedWindow("Gray Image", CV_WINDOW_AUTOSIZE);

    imshow(argv[1], image);
    imshow("Gray Image", gray_image);

    waitKey(0);
    return 0;
}
