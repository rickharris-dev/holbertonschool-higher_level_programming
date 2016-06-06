//
//  Entity.swift
//  TechCompanies
//
//  Created by Rick Harris on 6/6/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

enum EntityType:String {
    case None
    case School
    case TechCompany
}

class Entity {
    private var name:String
    private var town:String
    private var imageName:String
    private var type:EntityType
    
    init (name:String, town:String, imageName:String, type:EntityType = .None) {
        self.name = name
        self.town = town
        self.imageName  = imageName
        self.type = type
    }
    
    func getName() -> String {
        return self.name
    }
    
    func getEntityType() -> EntityType {
        return self.type
    }
    
    func getTown() -> String {
        return self.town
    }
    
    func getImageName() -> String {
        return self.imageName
    }
}