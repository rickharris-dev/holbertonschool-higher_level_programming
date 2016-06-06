//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Rick Harris on 6/6/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class TechCompaniesListViewController: UITableViewController {
    
    var schoolList:[Entity]!
    var techCompanyList:[Entity]!
    let techDetailSegue = "techDetailSegue"

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.title = "Entity list"
        self.techCompanyList = EntitiesHelper.getTechCompanies()
        self.schoolList = EntitiesHelper.getSchools()
        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 2
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        if section == 0 {
            return self.techCompanyList.count
        } else if section == 1 {
            return self.schoolList.count
        }
        return 0
    }
    
    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        switch (section) {
            case 0: return "Tech Companies"
            case 1: return "Schools"
            default: return ""
        }
    }


    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)

        if indexPath.section == 0 {
            cell.textLabel?.text = self.techCompanyList[indexPath.row].getName()
            if self.techCompanyList[indexPath.row].getEntityType() == EntityType.TechCompany {
                cell.detailTextLabel?.text = "I love working"
            } else if self.techCompanyList[indexPath.row].getEntityType() == EntityType.School {
                cell.detailTextLabel?.text = "I love studying"
            }
        } else if indexPath.section == 1 {
            cell.textLabel?.text = self.schoolList[indexPath.row].getName()
            if self.schoolList[indexPath.row].getEntityType() == EntityType.TechCompany {
                cell.detailTextLabel?.text = "I love working"
            } else if self.schoolList[indexPath.row].getEntityType() == EntityType.School {
                cell.detailTextLabel?.text = "I love studying"
            }
        }
        

        return cell
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == self.techDetailSegue {
            let detailView = segue.destinationViewController as! TechCompanyDetailViewController
            if let cell = sender as? UITableViewCell, let indexPath = tableView.indexPathForCell(cell) {
                print(indexPath.section)
                if indexPath.section == 0 {
                    detailView.entity = self.techCompanyList[indexPath.row]
                } else if indexPath.section == 1 {
                    detailView.entity = self.schoolList[indexPath.row]
                }
            } else {
                detailView.entity = nil
            }
        }
    }

    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
