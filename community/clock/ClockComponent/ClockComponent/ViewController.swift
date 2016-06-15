//
//  ViewController.swift
//  ClockComponent
//
//  Created by Rick Harris on 6/14/16.
//  Copyright © 2016 Rick Harris. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    // Developer Configurations
    var size: CGFloat = 200  // Width in pixels
    var clockType: String = "digital" // digital or analog
    var clockPrecision: String = "minute" // minute or second
    
    
    // Clock UI connections
    
    // Analog View Resources

    @IBOutlet var analogView: UIView!
    @IBOutlet var clockFace: UIView!
    @IBOutlet weak var hourHand: UIView!
    @IBOutlet weak var minuteHand: UIView!
    @IBOutlet weak var secondHand: UIView!
    @IBOutlet weak var clockHeight: NSLayoutConstraint!
    @IBOutlet weak var clockWidth: NSLayoutConstraint!
    @IBOutlet weak var hourHeight: NSLayoutConstraint!
    @IBOutlet weak var hourWidth: NSLayoutConstraint!
    @IBOutlet weak var minuteHeight: NSLayoutConstraint!
    @IBOutlet weak var minuteWidth: NSLayoutConstraint!
    @IBOutlet weak var secondHeight: NSLayoutConstraint!
    @IBOutlet weak var secondWidth: NSLayoutConstraint!
    @IBOutlet weak var clockTop: NSLayoutConstraint!
    @IBOutlet weak var clockLeft: NSLayoutConstraint!
    
    var f: CALayer {
        return clockFace.layer
    }
    
    var h: CALayer {
        return hourHand.layer
    }
    
    var m: CALayer {
        return minuteHand.layer
    }
    
    var s: CALayer {
        return secondHand.layer
    }
    
    // Digital View Resources
    @IBOutlet weak var digitalClock: UIView!
    @IBOutlet weak var digitalBack: UIImageView!
    @IBOutlet weak var hourDigit: UIImageView!
    @IBOutlet weak var minuteTen: UIImageView!
    @IBOutlet weak var minuteDigit: UIImageView!
    @IBOutlet weak var secondTen: UIImageView!
    @IBOutlet weak var secondDigit: UIImageView!
    @IBOutlet weak var ampm: UIImageView!
    @IBOutlet weak var digitalTop: NSLayoutConstraint!
    @IBOutlet weak var digitalLeft: NSLayoutConstraint!
    @IBOutlet weak var digitalHeight: NSLayoutConstraint!
    @IBOutlet weak var digitalWidth: NSLayoutConstraint!
    @IBOutlet weak var digitalBackWidth: NSLayoutConstraint!
    @IBOutlet weak var hourDigitWidth: NSLayoutConstraint!
    @IBOutlet weak var minuteTenWidth: NSLayoutConstraint!
    @IBOutlet weak var minuteDigitWidth: NSLayoutConstraint!
    @IBOutlet weak var secondTenWidth: NSLayoutConstraint!
    @IBOutlet weak var secondDigitWidth: NSLayoutConstraint!
    @IBOutlet weak var ampmWidth: NSLayoutConstraint!
    
    // Digital Layout
    @IBOutlet weak var x1: NSLayoutConstraint!
    @IBOutlet weak var y1: NSLayoutConstraint!
    @IBOutlet weak var y2: NSLayoutConstraint!
    @IBOutlet weak var x2: NSLayoutConstraint!
    @IBOutlet weak var y3: NSLayoutConstraint!
    @IBOutlet weak var x3: NSLayoutConstraint!
    @IBOutlet weak var x4: NSLayoutConstraint!
    @IBOutlet weak var y4: NSLayoutConstraint!
    @IBOutlet weak var y5: NSLayoutConstraint!
    @IBOutlet weak var x5: NSLayoutConstraint!
    @IBOutlet weak var x6: NSLayoutConstraint!
    @IBOutlet weak var y6: NSLayoutConstraint!
    
    // Default Information Variables
    var layoutGuide: CGFloat = 40
    let screenSize: CGRect = UIScreen.mainScreen().bounds
    var timer = NSTimer()
    
    override func viewWillAppear(animated: Bool) {
        // Prepares the compenent on app load
        super.viewWillAppear(animated)
        
        // Determines if requested size is larger than screen and adjusts if needed
        var smallest: CGFloat
        if screenSize.height < screenSize.width {
            smallest = screenSize.height - layoutGuide
        } else {
            smallest = screenSize.width - layoutGuide
        }
        
        if smallest < size {
            size = smallest
        }
        
        if clockType == "analog" {
            // Adjusts position to center of screen
            clockTop.constant = (screenSize.height - size - layoutGuide) / 2
            clockLeft.constant = (screenSize.width - size - layoutGuide) / 2
            
            // Hides digital clock and shows analog
            digitalClock.layer.opacity = 0.0
            clockFace.layer.opacity = 100.0
            
            // Sets image for each clock piece
            f.contents = UIImage(named: "clock-1")?.CGImage
            h.contents = UIImage(named: "hour-1")?.CGImage
            m.contents = UIImage(named: "minute-1")?.CGImage
            s.contents = UIImage(named: "second-1")?.CGImage
            
            // Adjusts sizing for all clock elements
            clockFace.autoresizesSubviews = true
            clockHeight.constant = size
            clockWidth.constant = size
            hourHeight.constant = size
            hourWidth.constant = size
            minuteHeight.constant = size
            minuteWidth.constant = size
            secondHeight.constant = size
            secondWidth.constant = size
            
            // Hides the second hand if precision is minute
            if clockPrecision == "minute" {
                secondHand.layer.opacity = 0.0
            }
        } else if clockType == "digital" {
            // Determines sizing ratio
            let ratio = size / 500
            
            // Sets digital element sizing
            digitalWidth.constant = size
            digitalBackWidth.constant = size
            hourDigitWidth.constant = hourDigitWidth.constant * ratio
            minuteTenWidth.constant = minuteTenWidth.constant * ratio
            minuteDigitWidth.constant = minuteDigitWidth.constant * ratio
            secondTenWidth.constant = secondTenWidth.constant * ratio
            secondDigitWidth.constant = secondDigitWidth.constant * ratio
            
            // Sets digital element positioning
            x1.constant = x1.constant * ratio
            x2.constant = x2.constant * ratio
            x3.constant = x3.constant * ratio
            x4.constant = x4.constant * ratio
            x5.constant = x5.constant * ratio
            x6.constant = x6.constant * ratio
            y1.constant = y1.constant * ratio
            y2.constant = y2.constant * ratio
            y3.constant = y3.constant * ratio
            y4.constant = y4.constant * ratio
            y5.constant = y5.constant * ratio
            y6.constant = y6.constant * ratio
            ampmWidth.constant = ampmWidth.constant * ratio

            // Shows the digital clock and hides the analog
            digitalClock.layer.opacity = 100.0
            clockFace.layer.opacity = 0.0
            
            // Hides the second count if precision is minute
            if clockPrecision == "minute" {
                secondTen.layer.opacity = 0.0
                secondDigit.layer.opacity = 0.0
            }
        }
        // Updates time information to be accurate on load
        rotateLayers()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setUpLayers()
        
        // Defines the timers based on precision
        if clockPrecision == "second" {
            timer = NSTimer.scheduledTimerWithTimeInterval(1, target:self, selector: Selector("rotateLayers"), userInfo: nil,repeats: true)
        } else if clockPrecision == "minute" {
            timer = NSTimer.scheduledTimerWithTimeInterval(60, target:self, selector: Selector("rotateLayers"), userInfo: nil, repeats: true)
        }
    }
    
    func setUpLayers() {
        // Removes layer backgrounds and creates shadow
        if clockType == "analog" {
            f.backgroundColor = UIColor.clearColor().CGColor
            f.shadowOpacity = 0.7
            f.shadowRadius = 10.0
            h.backgroundColor = UIColor.clearColor().CGColor
            m.backgroundColor = UIColor.clearColor().CGColor
            s.backgroundColor = UIColor.clearColor().CGColor
        }
    }
    
    func setClockValue(image: UIImageView, value: Int, type: String) {
        if type == "back" {
            // Updates digital clock back to show 1 or not
            if value == 0 {
                image.image = UIImage(named: "digital_clock")
            } else if value == 1 {
                image.image = UIImage(named: "digital_clock_one")
            }
        } else if type == "digit" {
            // Updates each digit element to show the correct number
            switch (value) {
            case 0:
                image.image = UIImage(named: "zero")
            case 1:
                image.image = UIImage(named: "one")
            case 2:
                image.image = UIImage(named: "two")
            case 3:
                image.image = UIImage(named: "three")
            case 4:
                image.image = UIImage(named: "four")
            case 5:
                image.image = UIImage(named: "five")
            case 6:
                image.image = UIImage(named: "six")
            case 7:
                image.image = UIImage(named: "seven")
            case 8:
                image.image = UIImage(named: "eight")
            case 9:
                image.image = UIImage(named: "nine")
            default:
                image.image = UIImage(named: "eight")
            }
        } else if type == "era" {
            // Updates am/pm to show the correct era
            if value == 0 {
                image.image = UIImage(named: "am")
            } else if value == 1 {
                image.image = UIImage(named: "pm")
            }
        }
    }
    
    func rotateLayers() {
        // Gathers variables relating to the current time
        let date = NSDate()
        let calendar = NSCalendar.currentCalendar()
        let components = calendar.components([ .Hour, .Minute, .Second, .Era], fromDate: date)
        var nowHour = components.hour
        let nowMinutes = components.minute
        let nowSeconds = components.second
        let nowEra = components.era
    
        if clockType == "analog" {
            // Converts degree to radians to properly rotate layers
            let degreesToRadians: (CGFloat) -> CGFloat = {
                return $0 / 180.0 * CGFloat(M_PI)
            }
        
            //Defines the degrees of rotation
            let hourRotation = 0.5 // Rotation per minute
            let minuteRotation = 0.1 // Rotation per second
            let secondRotation = 6 // Rotation per second
        
            // Hour Rotation
            let hourDegrees = CGFloat(Double((nowHour * 60) + nowMinutes) * hourRotation)
            let hours = CGAffineTransformMakeRotation(degreesToRadians(hourDegrees));
            hourHand.transform = hours
        
            // Minute Rotation
            let minuteDegrees = CGFloat(Double((nowMinutes * 60) + nowSeconds) * minuteRotation)
            let minutes = CGAffineTransformMakeRotation(degreesToRadians(minuteDegrees));
            minuteHand.transform = minutes
        
            // Second Rotation
            let secondDegrees = CGFloat(Double(nowSeconds) * Double(secondRotation))
            let seconds = CGAffineTransformMakeRotation(degreesToRadians(secondDegrees))
            secondHand.transform = seconds
            
        } else if clockType == "digital" {
            
            // Forces digital face to back
            digitalClock.sendSubviewToBack(digitalBack)
            
            // Converts military time to 12-hour clock if needed
            if nowHour > 12 {
                nowHour = nowHour - 12
            }
            
            // Obtains each digit in the time
            let hourTenValue = nowHour / 10
            let hourDigitValue = nowHour % 10
            let minuteTenValue = nowMinutes / 10
            let minuteDigitValue = nowMinutes % 10
            let secondTenValue = nowSeconds / 10
            let secondDigitValue = nowSeconds % 10
            
            // Initalizes function to set clock information
            setClockValue(self.digitalBack, value: hourTenValue, type: "back")
            setClockValue(self.hourDigit, value: hourDigitValue, type: "digit")
            setClockValue(self.minuteTen, value: minuteTenValue, type: "digit")
            setClockValue(self.minuteDigit, value: minuteDigitValue, type: "digit")
            setClockValue(self.ampm, value: nowEra, type: "era")
            if clockPrecision == "second" {
                // Only updates seconds if precision is second
                setClockValue(self.secondTen, value: secondTenValue, type: "digit")
                setClockValue(self.secondDigit, value: secondDigitValue, type: "digit")
            }
        }
    }
}

