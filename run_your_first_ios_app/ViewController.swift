//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    // Links to UI elements
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    @IBOutlet weak var message_text: UILabel!
    @IBOutlet weak var last_score: UILabel!
    @IBOutlet weak var high_score_label: UILabel!
    
    // Initializes class attributes
    var taps_done: Int = 0
    var taps_requested: Int = 0
    var start_time: Double = 0
    var end_time: Double = 0
    var elapsed_time: Double = 0
    var avg_tap_speed: Int = 0
    var speed_file: String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        // Resets taps and the game on load and retrieves the current high score
        label_taps.text = String(taps_done) + " taps"
        self.resetGame()
        self.high_score_label.text = "High Score: " + String(self.getHighScore())
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func clickPlayButton(sender: UIButton) {
        //Initializes gameplay
        let input = Int(self.textfield_number!.text!)
        if input != nil && input > 0 {
            self.taps_requested = input!
        }
        self.initGame()
    }
    
    @IBAction func clickCoinButton(sender: UIButton) {
        // Counts taps on the coin displays count
        taps_done += 1
        label_taps.text = String(taps_done) + " taps"
        
        // If game is complete calculates the score
        if taps_done >= taps_requested {
            self.end_time = NSDate.timeIntervalSinceReferenceDate()
            self.elapsed_time = self.end_time - self.start_time
            self.avg_tap_speed = Int(1 / (Float(self.elapsed_time) / Float(self.taps_requested)) * 131400 )
            
            // Retrieves the high score and adjust screen based on result
            let high_score: Int = self.getHighScore()
            if high_score < self.avg_tap_speed {
                self.message_text.text = "New High Score!"
                self.last_score.text = String(self.avg_tap_speed)
                self.high_score_label.text = ""
                self.setHighScore(String(self.avg_tap_speed))
            } else {
                self.message_text.text = "Try Again!"
                self.last_score.text = String(self.avg_tap_speed)
                self.high_score_label.text = "High Score: " + String(self.getHighScore())
            }
            // Resets the game to play again
            self.resetGame()
        }
    }
    
    func getFilePath() {
        // Creates file path screen
        let paths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)
        self.speed_file = paths[0] + "/best_taps_score.txt"
        return
    }
    
    func getHighScore() -> Int {
        // Retrieves the high score from a local file
        if self.speed_file == "" {
            self.getFilePath()
        }
        var best_speed: String = "0"
        do {
            best_speed = try String(NSString(contentsOfFile: self.speed_file, encoding: NSUTF8StringEncoding))
        }
        catch {}
        return Int(best_speed)!
    }
    
    func setHighScore(best_speed: String) {
        // Stores high score on local file
        if self.speed_file == "" {
            self.getFilePath()
        }
        do {
            try best_speed.writeToFile(self.speed_file, atomically: false, encoding: NSUTF8StringEncoding)
        }
        catch { print("ERROR: speed_file not written successfully") }
    }
    
    func initGame() {
        // Hide welcome screen
        self.image_tapper.hidden = true
        self.button_play.hidden = true
        self.textfield_number.hidden = true
        self.message_text.hidden = true
        self.last_score.hidden = true
        self.high_score_label.hidden = true
        // Show game screen
        self.label_taps.hidden = false
        self.button_coin.hidden = false
        // Reset game values and start timer
        self.taps_done = 0
        self.label_taps.text = String(taps_done) + " taps"
        self.start_time = NSDate.timeIntervalSinceReferenceDate()
    }
    
    func resetGame() {
        // Show welcome screen
        self.image_tapper.hidden = false
        self.button_play.hidden = false
        self.textfield_number.hidden = false
        self.message_text.hidden = false
        self.last_score.hidden = false
        self.high_score_label.hidden = false
        // Hide game screen
        self.label_taps.hidden = true
        self.button_coin.hidden = true
        // Reset user input
        self.taps_requested = 0
        self.textfield_number.text = ""
    }
}

