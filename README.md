```markdown```
# Action Slider :raised_hand:  
*A Gesture-Controlled Presentation Tool*  

Control PowerPoint/Google Slides with hand gestures – wave **left** or **right** to navigate slides seamlessly.  

## :sparkles: Features  
- **Intuitive Gesture Control**: Wave left/right to navigate slides.  
- **Camera Integration**: Works with any standard webcam.  
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.  
- **Customizable**: Adjust gesture sensitivity and slide delay.  

## :wrench: Installation  
1. **Clone the repository**:  
   ```bash  
   git clone (https://github.com/DheerajNair123/ActionSlider.git)
   cd ActionSlider  
   ```  

2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  
   *Dependencies include OpenCV, PyAutoGUI, and MediaPipe.*  

## :rocket: Usage  
1. **Start the application**:  
   ```bash  
   python main.py  
   ```  

2. **Position yourself**:  
   Stand 2-3 feet from your webcam with good lighting.  

3. **Navigate slides**:  
   - Wave hand **→ RIGHT** to go to next slide.  
   - Wave hand **← LEFT** to go back.  

4. **Exit**: Press `Q` to quit the application.  

## :bulb: How It Works  
- Uses **OpenCV** for real-time camera input.  
- **MediaPipe** for hand landmark detection.  
- **PyAutoGUI** to simulate keyboard inputs (Left/Right arrow keys).   

## :heart: Contributing  
PRs and issues are welcome!  
1. Fork the project.  
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).  
3. Commit changes (`git commit -m 'Add AmazingFeature'`).  
4. Push to branch (`git push origin feature/AmazingFeature`).  
5. Open a Pull Request.  

## :scroll: License  
Distributed under MIT License. See `LICENSE` for details.  

## :mailbox: Contact  
Dheeraj Nair - [dheerajnairp@gmail.com]  

---  
**Made with Python and ❤️**  
```
