//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Rick Harris on 6/6/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit


class MyCell: UITableViewCell {
    override func layoutSubviews() {
        super.layoutSubviews()
        
        let cvf: CGRect = self.contentView.frame;
        let top: Int = (Int(cvf.size.height)-30)/2
        self.imageView!.frame = CGRectMake(10.0,
            CGFloat(top),
            30,
            30);
        self.imageView!.contentMode = UIViewContentMode.ScaleAspectFit;
        
        var frame: CGRect = CGRectMake(cvf.size.height + 10,
            self.textLabel!.frame.origin.y,
            cvf.size.width - cvf.size.height - 2*10,
            self.textLabel!.frame.size.height);
        self.textLabel!.frame = frame;
        
        frame = CGRectMake(cvf.size.height + 10,
            self.detailTextLabel!.frame.origin.y,
            cvf.size.width - cvf.size.height - 2*10,
            self.detailTextLabel!.frame.size.height);
        self.detailTextLabel!.frame = frame;
        
        self.separatorInset = UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)
    
        
    }
}

class TechCompaniesListViewController: UITableViewController {
    
    var schoolList:[Entity]!
    var techCompanyList:[Entity]!
    var listSanFrancisco:[Entity]!
    var listMountainView:[Entity]!
    var listSunnyvale:[Entity]!
    var listCupertino:[Entity]!
    let techDetailSegue = "techDetailSegue"
    var toggle:Int = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.title = "Entity list"
        self.techCompanyList = EntitiesHelper.getTechCompanies()
        self.schoolList = EntitiesHelper.getSchools()
        self.listSanFrancisco = EntitiesHelper.getSanFranciscoEntities()
        self.listMountainView = EntitiesHelper.getMountainViewEntities()
        self.listSunnyvale = EntitiesHelper.getSunnyvaleEntities()
        self.listCupertino = EntitiesHelper.getCupertinoEntities()
        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func changeSegmentation(sender: UIBarButtonItem) {
        if self.toggle == 0 {
            self.toggle = 1
        } else {
            self.toggle = 0
        }
        self.tableView.reloadData()
    }
    
    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        if self.toggle == 0 {
            return 2
        } else if self.toggle == 1 {
            return 4
        }
        return 0
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        if section == 0 && self.toggle == 0 {
            return self.techCompanyList.count
        } else if section == 1 && self.toggle == 0 {
            return self.schoolList.count
        } else if section == 0 && self.toggle == 1 {
            return self.listSanFrancisco.count
        } else if section == 1 && self.toggle == 1 {
            return self.listMountainView.count
        } else if section == 2 && self.toggle == 1 {
            return self.listSunnyvale.count
        } else if section == 3 && self.toggle == 1 {
            return self.listCupertino.count
        }
        return 0
    }
    
    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        if self.toggle == 0 {
            switch (section) {
                case 0: return "Tech Companies"
                case 1: return "Schools"
                default: return ""
            }
        } else if self.toggle == 1 {
            switch (section){
            case 0: return "San Francisco"
            case 1: return "Mountain View"
            case 2: return "Sunnyvale"
            case 3: return "Cupertino"
            default: return ""
            }
        }
        return nil
    }


    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)
        var entity: Entity

        if indexPath.section == 0 && self.toggle == 0 {
            entity = self.techCompanyList[indexPath.row]
        } else if indexPath.section == 1 && self.toggle == 0 {
            entity = self.schoolList[indexPath.row]
        } else if indexPath.section == 0 && self.toggle == 1 {
            entity = self.listSanFrancisco[indexPath.row]
        } else if indexPath.section == 1 && self.toggle == 1 {
            entity = self.listMountainView[indexPath.row]
        }else if indexPath.section == 2 && self.toggle == 1 {
            entity = self.listSunnyvale[indexPath.row]
        }else {
            entity = self.listCupertino[indexPath.row]
        }
        cell.textLabel?.text = entity.getName()
        if entity.getEntityType() == EntityType.TechCompany {
            cell.detailTextLabel?.text = "I love working"
        } else if entity.getEntityType() == EntityType.School {
            cell.detailTextLabel?.text = "I love studying"
        }

        cell.imageView?.image = UIImage(named: entity.getImageName())
        
        return cell
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == self.techDetailSegue {
            let detailView = segue.destinationViewController as! TechCompanyDetailViewController
            if let cell = sender as? UITableViewCell, let indexPath = tableView.indexPathForCell(cell) {
                if indexPath.section == 0 && self.toggle == 0 {
                    detailView.entity = self.techCompanyList[indexPath.row]
                } else if indexPath.section == 1 && self.toggle == 0 {
                    detailView.entity = self.schoolList[indexPath.row]
                } else if indexPath.section == 0 && self.toggle == 1 {
                    detailView.entity = self.listSanFrancisco[indexPath.row]
                } else if indexPath.section == 1 && self.toggle == 1 {
                    detailView.entity = self.listMountainView[indexPath.row]
                } else if indexPath.section == 2 && self.toggle == 1 {
                    detailView.entity = self.listSunnyvale[indexPath.row]
                } else if indexPath.section == 3 && self.toggle == 1 {
                    detailView.entity = self.listCupertino[indexPath.row]
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
