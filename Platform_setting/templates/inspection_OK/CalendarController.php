<?php
class CalendarController extends ControllerBase
{
    public function indexAction()
    {
		include "incld/load.php";
		include "incld/insert.php";
		include "incld/update.php";
		include "incld/delete.php";
	  }
}