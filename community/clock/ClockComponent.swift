////
////  ClockComponent.swift
////  ClockComponent
////
////  Created by Rick Harris on 6/14/16.
////  Copyright © 2016 Holberton School. All rights reserved.
////
//
//import UIKit
//
//class ClockComponent: UIView {
//    
//    // MARK: Properties
//    
//    var rating = 0
//    var ratingButtons = [UIButton]()
//    let hourRotation = 0.5 // Rotation per minute
//    let minuteRotation = 0.1 // Rotation per second
//    let secondRotation = 6 // Rotation per second
//    let clockHeight = 250
//    let clockWidth = 250
//    let hourHandSize = 0.75
//    let minuteHandSize = 0.90
//    let secondHandSize = 0.90
//
//    // MARK: Initialization
//    
//    var timer = NSTimer()
//    var counter = 0
//    
//    
//    required init?(coder aDecoder: NSCoder) {
//        super.init(coder: aDecoder)
//        
//        let degreesToRadians: (CGFloat) -> CGFloat = {
//            return $0 / 180.0 * CGFloat(M_PI)
//        }
//        
//        let hourHandPosition = ((Double(clockWidth) - (Double(clockWidth) * hourHandSize))/2)
//        let minuteHandPosition = ((Double(clockWidth) - (Double(clockWidth) * 0.90))/2)
//        let secondHandPosition = ((Double(clockWidth) - (Double(clockWidth) * 0.90))/2)
//        
//        // Analog Clock
//        
//        // Clock Face
//        let face = UIImageView(frame: CGRect(x: 0, y: 0, width: clockWidth, height: clockHeight))
//        face.backgroundColor = UIColor.redColor()
//        addSubview(face)
//        
//        // Hour Hand
//        let hour = UIImageView(frame: CGRect(x: hourHandPosition, y: hourHandPosition, width: (Double(clockWidth) * hourHandSize), height: (Double(clockHeight) * hourHandSize)))
//        hour.backgroundColor = UIColor.blueColor()
//        addSubview(hour)
//        
//        // Minute Hand
//        let minute = UIImageView(frame: CGRect(x: minuteHandPosition, y: minuteHandPosition, width: (Double(clockWidth) * minuteHandSize), height: (Double(clockHeight) * minuteHandSize)))
//        minute.backgroundColor = UIColor.greenColor()
//        addSubview(minute)
//        
//        
//        // Second Hand
//        let second = UIImageView(frame: CGRect(x: secondHandPosition, y: secondHandPosition, width: (Double(clockWidth) * secondHandSize), height: (Double(clockHeight) * secondHandSize)))
//        second.backgroundColor = UIColor.purpleColor()
//        addSubview(second)
//        
//        // Calculate Rotation
//        
//        
//        
//        // Digital Clock
//
//    }
//    
//    var timer = NSTimer.scheduledTimerWithTimeInterval(1, target:self, selector: Selector("updateRotation"), userInfo: nil, repeats: true)
//    
//    func updateRotation() {
//        let date = NSDate()
//        let calendar = NSCalendar.currentCalendar()
//        let components = calendar.components([ .Hour, .Minute, .Second], fromDate: date)
//        let nowHour = components.hour
//        let nowMinutes = components.minute
//        let nowSeconds = components.second
//        
//        // Hour Rotation
//        let hourDegrees = CGFloat(Double((nowHour * 60) + nowMinutes) * hourRotation)
//        let h = CGAffineTransformMakeRotation(degreesToRadians(hourDegrees));
//        hour.transform = h
//        
//        // Minute Rotation
//        let minuteDegrees = CGFloat(Double((nowMinutes * 60) + nowSeconds) * minuteRotation)
//        let m = CGAffineTransformMakeRotation(degreesToRadians(minuteDegrees));
//        minute.transform = m
//        
//        // Second Rotation
//        let secondDegrees = CGFloat(Double(nowSeconds) * Double(secondRotation))
//        let s = CGAffineTransformMakeRotation(degreesToRadians(secondDegrees));
//        second.transform = s
//    }
//
//    override func intrinsicContentSize() -> CGSize {
//        return CGSize(width: clockWidth, height: clockHeight)
//    }
//}
