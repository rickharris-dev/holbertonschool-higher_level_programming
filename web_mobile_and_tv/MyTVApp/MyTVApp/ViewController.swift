//
//  ViewController.swift
//  MyTVApp
//
//  Created by Rick Harris on 6/24/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit
import AVKit

class StreamCell: UICollectionViewCell {
    
    @IBOutlet weak var textLabel: UILabel!
    
}

class ViewController: UIViewController, UICollectionViewDataSource, UICollectionViewDelegate {
    
    var streamList: [MyTVAppItem] = [MyTVAppItem(name: "Bip", url_stream: "http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8"), MyTVAppItem(name: "Apple Keynote", url_stream: "http://qthttp.apple.com.edgesuite.net/1010qwoeiuryfg/sl.m3u8"),
        MyTVAppItem(name: "Big Buck Bunny", url_stream: "http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4")]
    let defaultFontSize = UIFontDescriptor(name: "System", size: 50)
    let focusFontSize = UIFontDescriptor(name: "System", size: 40)
    
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    func collectionView(collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return streamList.count
    }
    
    func collectionView(collectionView: UICollectionView, cellForItemAtIndexPath indexPath: NSIndexPath) -> UICollectionViewCell {
        
        let cell: StreamCell = collectionView.dequeueReusableCellWithReuseIdentifier("Cell", forIndexPath: indexPath) as! StreamCell
        cell.textLabel.text = streamList[indexPath.row].name
        
        return cell
    }
    
    override func didUpdateFocusInContext(context: UIFocusUpdateContext, withAnimationCoordinator coordinator: UIFocusAnimationCoordinator) {
        if let prev = context.previouslyFocusedView as? StreamCell {
            UIView.animateWithDuration(0.1, animations: { () -> Void in
                prev.textLabel.textColor = UIColor.blackColor()
                prev.textLabel.font = UIFont(descriptor: prev.textLabel.font.fontDescriptor(), size: 30.00)
            })
        }
        
        if let next = context.nextFocusedView as? StreamCell {
            UIView.animateWithDuration(0.1, animations: { () -> Void in
                next.textLabel.textColor = UIColor.redColor()
                next.textLabel.font = UIFont(descriptor: next.textLabel.font.fontDescriptor(), size: 40.00)
                
            })
        }
    }
    
    func collectionView(collectionView: UICollectionView, didSelectItemAtIndexPath indexPath: NSIndexPath) {
        performSegueWithIdentifier("streamViewSegue", sender: indexPath)
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        assert(sender as? NSIndexPath != nil, "sender is not a collection view")
        if segue.identifier == "streamViewSegue" {
            let videoController: AVPlayerViewController = segue.destinationViewController as! AVPlayerViewController
            if let videoURL: NSURL = NSURL(string: streamList[sender!.row].url_stream) {
                print(videoURL)
                let videoPlayer: AVPlayer = AVPlayer(URL: videoURL)
                videoController.player = videoPlayer
                videoController.player?.play()
//            self.presentViewController(videoController, animated: true) {
//                videoController.player?.play()
//            }
            }
        }
    }
    
    

    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    


}

