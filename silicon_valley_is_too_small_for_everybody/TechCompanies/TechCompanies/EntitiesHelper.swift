//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by Rick Harris on 6/6/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

class EntitiesHelper {
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    
    static func getSchools() -> [Entity]! {
        if self.listOfSchool.count == 0 {
            self.listOfSchool.append(Entity(name: "Holberton", town: "San Francisco", imageName: "holberton", type: .School))
        }
        return self.listOfSchool
    }
    
    static func getTechCompanies() -> [Entity]! {
        if self.listOfTechCompany.count == 0 {
            listOfTechCompany.append(Entity(name: "Linkedin", town: "San Francisco", imageName: "linkedin", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Docker", town: "San Francisco", imageName: "docker", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Google", town: "Mountain View", imageName: "google", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Yahoo", town: "Sunnyvale", imageName: "yahoo", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Apple", town: "Cupertino", imageName: "apple", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Twitter", town: "San Francisco", imageName: "twitter", type: .TechCompany))
        }
        return self.listOfTechCompany
    }
}