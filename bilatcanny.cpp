#include <opencv2/opencv.hpp>
#include<iostream>
using namespace std;
using namespace cv;
// only the bilateral filter is working
int main() {
	Mat img = imread("face.png");
	if (!img.data) exit(1);
	Mat dst;
	bilateralFilter(img, dst, -1, 50, 7);
	Canny(dst, dst, 10, 50, 7);
	imwrite("out.png", dst);
	return 0;
}