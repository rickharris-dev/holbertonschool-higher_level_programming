//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by Rick Harris on 6/6/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

class EntitiesHelper {
    // Type lists
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    
    // Location lists
    static var listOfSanFrancisco:[Entity]! = []
    static var listOfMountainView:[Entity]! = []
    static var listOfSunnyvale:[Entity]! = []
    static var listOfCupertino:[Entity]! = []
    
    
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
    
    static func getSanFranciscoEntities() -> [Entity]! {
        if self.listOfSanFrancisco.count == 0 {
            self.sortByCity()
        }
        return self.listOfSanFrancisco
    }
    
    static func getMountainViewEntities() -> [Entity]! {
        if self.listOfMountainView.count == 0 {
            self.sortByCity()
        }
        return self.listOfMountainView
    }
    
    static func getSunnyvaleEntities() -> [Entity]! {
        if self.listOfSunnyvale.count == 0 {
            self.sortByCity()
        }
        return self.listOfSunnyvale
    }
    
    static func getCupertinoEntities() -> [Entity]! {
        if self.listOfCupertino.count == 0 {
            self.sortByCity()
        }
        return self.listOfCupertino
    }
    
    static func sortByCity() {
        for entity in self.getTechCompanies() {
            switch (entity.getTown()){
            case "San Francisco":
                self.listOfSanFrancisco.append(entity)
            case "Mountain View":
                self.listOfMountainView.append(entity)
            case "Sunnyvale":
                self.listOfSunnyvale.append(entity)
            case "Cupertino":
                self.listOfCupertino.append(entity)
            default:
                print(entity.getTown())
            }
        }
        for entity in self.getSchools() {
            switch (entity.getTown()){
            case "San Francisco":
                self.listOfSanFrancisco.append(entity)
            case "Mountain View":
                self.listOfMountainView.append(entity)
            case "Sunnyvale":
                self.listOfSunnyvale.append(entity)
            case "Cupertino":
                self.listOfCupertino.append(entity)
            default:
                print(entity.getTown())
            }
        }
    }
}