//
//  MyTVAppItem.swift
//  MyTVApp
//
//  Created by Rick Harris on 6/24/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class MyTVAppItem: NSObject {

    var name: String
    var url_stream: String
    
    init(name: String, url_stream: String) {
        self.name = name
        self.url_stream = url_stream
    }
}
