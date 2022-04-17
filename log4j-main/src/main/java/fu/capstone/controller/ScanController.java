package fu.capstone.controller;

import fu.capstone.modedl.ScanCriteria;
import fu.capstone.service.scanService;
import org.apache.commons.validator.routines.UrlValidator;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@RequestMapping("/webScan")
@Controller
public class ScanController {
	@Autowired
	private scanService scanService;

	@PostMapping(value = "/scan", consumes = "application/JSON")
	public @ResponseBody int scanWeb(@RequestBody ScanCriteria scan)  {

		try{
			String web = scan.getWeb();
			UrlValidator urlValidator = new UrlValidator();
			if(!urlValidator.isValid(web)){
				return 0;
			}else if(urlValidator.isValid(web)){
				boolean check = scanService.scan(web);
				if(!check){
					return 1;
				}else{
					return 2;
				}
			}
		}catch (Exception e){
			return 404;
		}
		return 0;
	}

}
